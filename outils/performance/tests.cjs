const fs=require('node:fs'),path=require('node:path'),vm=require('node:vm'),assert=require('node:assert/strict');
const root=path.resolve(__dirname,'../..'),source=fs.readFileSync(path.join(root,'index.html'),'utf8');
const ctx=vm.createContext({Map,Set,Proxy,Reflect,Math});
vm.runInContext(source.slice(source.indexOf('const INDEX_DECOR ='),source.indexOf('const obstacles =')),ctx);
let passed=0;function test(name,f){f();console.log('PASS',name);passed++;}
const cap=(x,z,r=1)=>({x1:x,z1:z,x2:x,z2:z,r});
test('Spatial lookup never excludes an overlapping circle or rectangle',()=>{
 let seed=915;const rnd=()=>((seed=Math.imul(seed,1664525)+1013904223>>>0)/4294967296);
 const list=ctx.listeDecor();for(let i=0;i<1200;i++)list.push(i%2?{x:rnd()*600-300,z:rnd()*600-300,r:rnd()*4}:{x:rnd()*600-300,z:rnd()*600-300,hw:rnd()*30,hd:rnd()*30});
 for(let j=0;j<1500;j++){
  const c=cap(rnd()*600-300,rnd()*600-300,rnd()*3);c.x2+=rnd()*30-15;c.z2+=rnd()*30-15;
  const candidates=ctx.candidatsDecor(list,c);assert.deepEqual([...candidates],[...new Set(candidates)].sort((a,b)=>a-b));const got=new Set(candidates);
  for(let i=0;i<list.length;i++){const o=list[i],rx=o.hw??o.r,rz=o.hd??o.r;
   if(o.x+rx>=Math.min(c.x1,c.x2)-c.r-.15&&o.x-rx<=Math.max(c.x1,c.x2)+c.r+.15&&o.z+rz>=Math.min(c.z1,c.z2)-c.r-.15&&o.z-rz<=Math.max(c.z1,c.z2)+c.r+.15)assert(got.has(i),`missing ${i}`);
  }
 }
});
test('Added, removed and grown scenery invalidate the index',()=>{
 const l=ctx.listeDecor();l.push({x:150,z:0,r:1});assert.equal(ctx.candidatsDecor(l,cap(0,0)).length,0);
 l.push({x:0,z:0,r:1});assert(ctx.candidatsDecor(l,cap(0,0)).includes(1));l.splice(1,1);assert.equal(ctx.candidatsDecor(l,cap(0,0)).length,0);
 l[0].r=151;ctx.invaliderDecor();assert(ctx.candidatsDecor(l,cap(0,0)).includes(0));l.length=0;assert.equal(ctx.candidatsDecor(l,cap(0,0)).length,0);
});
test('Tree regrowth stays inside its reserved extent without rebuilding the grid',()=>{
 const l=ctx.listeDecor(),tree={x:22,z:0,r:.5,rIndex:4};l.push(tree);
 assert(ctx.candidatsDecor(l,cap(18,0)).includes(0));ctx.regrowthList=l;const before=vm.runInContext('INDEX_DECOR.get(regrowthList)',ctx);
 tree.r=4;assert(ctx.candidatsDecor(l,cap(18,0)).includes(0));assert.equal(vm.runInContext('INDEX_DECOR.get(regrowthList)',ctx),before);
});
test('Resolving a contact refreshes candidates without changing collision order',()=>{
 const l=ctx.listeDecor();for(const x of [0,80,40,40])l.push({x,z:0,r:1});let c=cap(0,0),seen=[];
 for(const o of ctx.decorProche(l,()=>c)){seen.push(l.indexOf(o));if(seen.length===1)c=cap(40,0);}
 assert.deepEqual(seen,[0,2,3]);
});
test('Large water boxes and negative cell boundaries are included',()=>{
 const l=ctx.listeDecor();l.push({x:0,z:0,hw:400,hd:3},{x:-20,z:-20,r:1});
 assert(ctx.candidatsDecor(l,cap(399,0)).includes(0));assert(ctx.candidatsDecor(l,cap(-22,-20,1.01)).includes(1));
});
test('Real capsule collision resolution matches a complete decor scan',()=>{
 const start=source.indexOf('  decorGabarits(){'),end=source.indexOf('\n  /* UN CONTACT',start);
 const method=source.slice(start,end);
 vm.runInContext('var optimized=({'+method+'}).decorGabarits;var reference=({'+method.replace('decorProche(obstacles,()=>cap)','obstacles').replace('decorProche(boxObs,()=>cap)','boxObs')+'}).decorGabarits;',ctx);
 let seed=882;const rnd=()=>((seed=Math.imul(seed,1664525)+1013904223>>>0)/4294967296);
 ctx._gabA=[];ctx.obstacles=ctx.listeDecor();ctx.boxObs=ctx.listeDecor();
 for(let i=0;i<300;i++)ctx.obstacles.push({x:rnd()*120-60,z:rnd()*120-60,r:.5+rnd()*3,tronc:.3,arbre:i%3===0,bas:i%7===0});
 for(let i=0;i<25;i++)ctx.boxObs.push({x:rnd()*120-60,z:rnd()*120-60,hw:rnd()*6,hd:rnd()*6,eau:i%4===0});
 ctx.gabarits=(v,out)=>{out.length=0;for(const offset of [0,-7])out.push({x1:v.x+Math.sin(v.angle)*(offset-2),z1:v.z+Math.cos(v.angle)*(offset-2),x2:v.x+Math.sin(v.angle)*(offset+2),z2:v.z+Math.cos(v.angle)*(offset+2),r:1,part:offset?'outil':'corps'});return out;};
 const vehicle=(x,z,angle,abatteuse,bateau)=>({x,z,angle,abatteuse,bateau,hits:[],contact(px,pz,nx,nz,pen){this.hits.push([px,pz,nx,nz,pen]);this.x+=nx*pen;this.z+=nz*pen;this.angle+=(px-this.x)*nz*.01;},buter(...a){this.contact(...a);},franchir(o){this.hits.push(['bas',o.x,o.z]);}});
 for(let i=0;i<1200;i++){const a=vehicle(rnd()*120-60,rnd()*120-60,rnd()*6.28,i%4===0,i%5===0),b=vehicle(a.x,a.z,a.angle,a.abatteuse,a.bateau);ctx.optimized.call(a);ctx.reference.call(b);assert.equal(a.x,b.x);assert.equal(a.z,b.z);assert.equal(a.angle,b.angle);assert.deepEqual(a.hits,b.hits);}
});
test('Autonomous machines retain ordered contacts after position corrections',()=>{
 const l=ctx.listeDecor();for(const x of [0,80,40])l.push({x,z:0,r:1});const pos={x:0,z:0},seen=[];
 for(const o of ctx.decorAuPoint(l,pos,1.5)){seen.push(l.indexOf(o));pos.x=40;}assert.deepEqual(seen,[0,2]);
});
const listeners={};let draws=0;
Object.assign(ctx,{champsEnAttente:()=>false,champsAJour(){}});
Object.assign(ctx,{addEventListener:(e,f)=>listeners[e]=f,paused:false,camera:{position:{x:0,y:50,z:0},zoom:1},camTarget:{x:0,z:0},scene:{},renderer:{domElement:{width:1200,height:800,addEventListener(){}},render(){draws++;}}});
vm.runInContext(source.slice(source.indexOf('const IMAGE_REPOS='),source.indexOf('function loop(now){')),ctx);
test('Active play renders every frame at the same canvas size',()=>{
 for(let i=0;i<120;i++)ctx.rendreImage(i*1000/60);assert.equal(draws,120);assert.equal(ctx.renderer.domElement.width,1200);
});
test('Settled pause renders at most four times a second and wakes for input',()=>{
 ctx.paused=true;draws=0;for(let i=120;i<240;i++)ctx.rendreImage(i*1000/60);assert(draws<=8);const n=draws;
 listeners.pointerdown();ctx.rendreImage(4000);ctx.rendreImage(4010);ctx.rendreImage(4020);assert.equal(draws,n+3);
 ctx.camera.position.x++;ctx.rendreImage(4030);assert.equal(draws,n+4);ctx.renderer.domElement.width++;ctx.rendreImage(4040);assert.equal(draws,n+5);
 ctx.paused=false;ctx.rendreImage(4050);assert.equal(draws,n+6);
});
test('Crop uploads are consumed only by frames actually rendered, including pause',()=>{
 let uploads=0;draws=0;ctx.paused=true;ctx.champsEnAttente=()=>true;ctx.champsAJour=()=>uploads++;
 for(let i=0;i<120;i++)ctx.rendreImage(5000+i*1000/60);
 assert(draws>0&&draws<=8);assert.equal(uploads,draws);
});

test('Delivered scripts parse and graphics assets are copied byte for byte',()=>{
 const built=fs.readFileSync(path.join(root,'dist/index.html'),'utf8');for(const m of built.matchAll(/<script\b[^>]*>([\s\S]*?)<\/script>/g))new vm.Script(m[1]);
 assert(Buffer.byteLength(built)<Buffer.byteLength(source)*.65);
 for(const dir of ['pictos','portraits','portraits14','produits'])for(const file of fs.readdirSync(path.join(root,dir))){if(fs.statSync(path.join(root,dir,file)).isFile())assert(fs.readFileSync(path.join(root,dir,file)).equals(fs.readFileSync(path.join(root,'dist',dir,file))),file);}
 const outside=s=>s.replace(/<script\b([^>]*)>([\s\S]*?)<\/script>/g,(_,attrs)=>'<script'+attrs+'></script>');assert.equal(outside(built),outside(source));
 assert.deepEqual(built.match(/[A-Za-z0-9+/=]{1000,}/g),source.match(/[A-Za-z0-9+/=]{1000,}/g),'embedded media payloads');
});
console.log(`${passed} performance tests passed.`);
