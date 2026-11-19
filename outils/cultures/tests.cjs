const fs=require('node:fs'),path=require('node:path'),vm=require('node:vm'),assert=require('node:assert/strict');
const source=fs.readFileSync(path.join(__dirname,'../../index.html'),'utf8');
function fn(name){const a=source.indexOf('function '+name+'(');assert(a>=0,name);return source.slice(a,source.indexOf('\n}',a)+2);}
let passed=0;function test(name,f){f();passed++;console.log('PASS',name);}
class V3{constructor(x,y,z){Object.assign(this,{x,y,z});}}
class Box3{constructor(min,max){Object.assign(this,{min,max});}}
const ctx=vm.createContext({Math,THREE:{Box3,Vector3:V3},PARCELS:[{x:0,z:0,w:40,h:30},{x:-90,z:-100,w:60,h:50}],NB_AGES:4,
  CROPS:[{haut:1.45,large:.66},{haut:1,large:1,rang:true}],CHAMP_GEO:Array.from({length:8},()=>({boundingBox:{min:{x:-2,y:-.1,z:-1},max:{x:1,y:4,z:3}}}))});
vm.runInContext(fn('secteurChamp')+'\n'+fn('bornesChamp'),ctx);
test('Sector keys stay inside their parcel and handle negative coordinates and seams',()=>{
 assert.deepEqual([[-1,-1],[0,-1],[-1,0],[0,0]].map(([x,z])=>ctx.secteurChamp({par:0,x,z})),[0,1,2,3]);
 assert.equal(ctx.secteurChamp({par:1,x:-89,z:-101}),5);
});
test('Sector bounds contain rotated, scaled crop geometry including row snapping',()=>{
 let seed=34;const rnd=()=>((seed=Math.imul(seed,1664525)+1013904223>>>0)/4294967296);
 for(let i=0;i<3000;i++){
  const par=i%2,p=ctx.PARCELS[par],b={par,x:p.x+(rnd()-.5)*p.w,z:p.z+(rnd()-.5)*p.h};
  const k=i%8,c=ctx.CROPS[Math.floor(k/4)],bb=ctx.CHAMP_GEO[k].boundingBox,B=ctx.bornesChamp(k,ctx.secteurChamp(b));
  const sc=(c.rang?1:1.45+rnd()*.5)*c.large,rot=c.rang?0:rnd()*Math.PI*2;
  const px=b.x+(c.rang?(rnd()-.5)*.55:0),pz=b.z+(c.rang?(rnd()-.5)*.55:0);
  for(const x of [bb.min.x,bb.max.x])for(const y of [bb.min.y,bb.max.y])for(const z of [bb.min.z,bb.max.z]){
   const X=px+(x*Math.cos(rot)+z*Math.sin(rot))*sc,Y=y*sc*c.haut,Z=pz+(-x*Math.sin(rot)+z*Math.cos(rot))*sc;
   assert(X>=B.min.x&&X<=B.max.x&&Y>=B.min.y&&Y<=B.max.y&&Z>=B.min.z&&Z<=B.max.z);
  }
 }
});
const makeMesh=(visible,loCount=80)=>({visible,count:loCount,instanceMatrix:{updateRange:{}},instanceColor:{updateRange:{}}});
vm.runInContext('var CHAMPS=[],champLo=[],champHi=[],CHAMP_BUDGET=10;'+fn('champsAJour')+'\n'+fn('champsEnAttente'),ctx);
test('Hidden crop changes remain pending until the sector returns',()=>{
 const m=makeMesh(false);ctx.CHAMPS=[[m]];ctx.champLo=[[4]];ctx.champHi=[[70]];
 ctx.champsAJour();assert.equal(ctx.champLo[0][0],4);assert.equal(m.instanceMatrix.needsUpdate,undefined);
 m.visible=true;m.reveilChamp=true;ctx.champsAJour();assert.equal(m.instanceMatrix.updateRange.offset,64);assert.equal(m.instanceMatrix.updateRange.count,67*16);assert.equal(ctx.champLo[0][0],undefined);
});
test('A newly visible sector refreshes fully even after the regular upload budget is spent',()=>{
 const a=makeMesh(true),b=makeMesh(true);b.reveilChamp=true;ctx.CHAMPS=[[a,b]];ctx.champLo=[[0,0]];ctx.champHi=[[39,59]];
 ctx.champsAJour();assert.equal(a.instanceMatrix.updateRange.count,160);assert.equal(ctx.champLo[0][0],10);
 assert.equal(b.instanceMatrix.updateRange.count,960);assert.equal(ctx.champLo[0][1],undefined);
});
test('Harvest compacts its own sector and frees an empty sector',()=>{
 ctx.CHAMPS_ACTIFS=new Set();ctx.wheatBase=[{par:0,x:-2,z:-2},{par:0,x:-1,z:-1},{par:0,x:3,z:3}];
 ctx.champCrop=[0,0,0];ctx.champSlot=[0,1,0];ctx.champRec=[[[0,1],null,null,[2]]];ctx._m4={};ctx._col={fromArray(){return this;}};ctx.scene={remove(m){m.removed=true;}};
 const mesh={count:2,instanceColor:{array:new Float32Array(6)},getMatrixAt(i,m){m.from=i;},setMatrixAt(i,m){this.copied=[i,m.from];},setColorAt(){},dispose(){this.disposed=true;}};
 const other={count:1};ctx.CHAMPS=[[mesh,null,null,other]];ctx.champLo=[[]];ctx.champHi=[[]];ctx.CHAMPS_ACTIFS.add(mesh);ctx.CHAMPS_ACTIFS.add(other);
 vm.runInContext(fn('salir')+'\n'+fn('retirerDuChamp'),ctx);ctx.retirerDuChamp(0);assert.equal(mesh.count,1);assert.equal(ctx.champSlot[1],0);assert.equal(ctx.champRec[0][0][0],1);assert.equal(other.count,1);
 ctx.retirerDuChamp(1);assert.equal(ctx.CHAMPS[0][0],null);assert(mesh.removed&&mesh.disposed);assert(!ctx.CHAMPS_ACTIFS.has(mesh));assert(ctx.CHAMPS_ACTIFS.has(other));
});
test('Maximum sharpness follows native DPR, with optional caps and hardware limit',()=>{
 const r={domElement:{style:{}},setSize(w,h){this.size=[w,h];}},rc=vm.createContext({Math,innerWidth:800,innerHeight:450,devicePixelRatio:1,RESOLUTION_LIMITE:8192,NETTETE:{i:0,choix:[{max:Infinity},{max:2}]},PIXEL:{px:1},PIXEL_MIN:1,PIXEL_MAX:4,renderer:r});
 vm.runInContext(fn('applyResolution'),rc);
 for(const dpr of [1,2,3,4]){rc.devicePixelRatio=dpr;rc.applyResolution();assert.deepEqual(r.size,[800*dpr,450*dpr]);}
 rc.NETTETE.i=1;rc.applyResolution();assert.deepEqual(r.size,[1600,900]);
 rc.NETTETE.i=0;rc.innerWidth=4000;rc.applyResolution();assert(r.size[0]<=8192&&r.size[1]<=8192);
});
console.log(passed+' crop tests passed.');
