const fs=require('fs'),path=require('path'),vm=require('vm'),assert=require('assert/strict');
const s=fs.readFileSync(path.join(__dirname,'../../index.html'),'utf8'),c=vm.createContext({Math,hitchDe:()=>2});
for(const name of ['suivreSemi','placerSemiAttachee','contactRemorqueSemi','migrerParcSemi']){const a=s.indexOf('function '+name+'(');vm.runInContext(s.slice(a,s.indexOf('\n}',a)+2),c);}
const vec=(x=0,y=0,z=0)=>({x,y,z,set(x,y,z){this.x=x;this.y=y;this.z=z;}});
function rig(angle=.2){const v={pos:vec(4,0,2),vel:vec(0,6),cap:0,speed:6},T={semi:true,L:12,cap:angle,axle:{x:4-Math.sin(angle)*12,z:-Math.cos(angle)*12},group:{position:vec(4,0,0),rotation:{y:angle,z:0}},load:0,capacite:1000};T.attached=v;v.tool=T;return v;}
function check(v){const T=v.tool,H=T.group.position;assert(Math.abs(Math.hypot(H.x-T.axle.x,H.z-T.axle.z)-T.L)<1e-8);assert(Math.abs(H.x-(v.pos.x-Math.sin(v.cap)*2))<1e-8);assert(Math.abs(H.z-(v.pos.z-Math.cos(v.cap)*2))<1e-8);assert.equal(T.group.rotation.y,T.cap);}
let n=0;function test(name,f){f();n++;console.log('PASS',name);}
test('Side contact pivots the trailer and preserves tangential speed',()=>{for(const side of [-1,1]){const v=rig(),T=v.tool,old=T.cap,cap=v.cap,z=v.vel.y;c.contactRemorqueSemi(v,4,-10,side,0,.3);assert((T.cap-old)*side<0);assert.equal(v.cap,cap);assert.equal(v.vel.y,z);assert(Math.abs(v.pos.x-4)<.02);check(v);}});
test('A contact in the trailer axis stops penetration instead of sliding through',()=>{const v=rig(0);v.vel.y=-4;c.contactRemorqueSemi(v,4,-15,0,1,.2);assert.equal(v.vel.y,0);assert.equal(v.tool.cap,0);assert(Math.abs(v.pos.z-2.2)<1e-8);check(v);});
test('Corrected articulation survives the next tracking update at rest',()=>{const v=rig();c.contactRemorqueSemi(v,4,-10,1,0,.3);const a=v.tool.cap;c.placerSemiAttachee(v,1/60);assert.equal(v.tool.cap,a);check(v);});
test('Non-semi tools retain their original collision path',()=>{const v=rig();v.tool.semi=false;assert.equal(c.contactRemorqueSemi(v,0,0,1,0,.2),false);});
function wallRun(hz,side=1,reverse=false){const v=rig(side*.3);v.pos.x=side*3;v.vel.y=reverse?-4:6;const T=v.tool;T.group.position.x=v.pos.x;T.axle.x=v.pos.x-Math.sin(T.cap)*T.L;const start=v.pos.z;let contacts=0;
 for(let k=0;k<hz*5;k++){
  v.pos.z+=v.vel.y/hz;c.placerSemiAttachee(v,1/hz);
  for(let pass=0;pass<3;pass++)for(const d of [-13,-7,-1]){
   const x=T.group.position.x+Math.sin(T.cap)*d,z=T.group.position.z+Math.cos(T.cap)*d,pen=2-side*x;
   if(pen>0){contacts++;c.contactRemorqueSemi(v,x,z,side,0,pen);}
  }
  for(const d of [-13,-7,-1])assert(side*(T.group.position.x+Math.sin(T.cap)*d)>=2-.035);
  check(v);
 }
 assert(contacts>0);assert(Math.abs(v.pos.z-start)>19);assert(Math.abs(v.vel.y)>(reverse?3.9:5.9));return {x:v.pos.x,cap:T.cap,z:v.pos.z};
}
test('A trailer scrapes either wall while continuing forward or reversing',()=>{for(const side of [-1,1])for(const reverse of [false,true])wallRun(60,side,reverse);});
test('Wall sliding remains consistent at 30, 60 and 120 Hz',()=>{const r=[30,60,120].map(hz=>wallRun(hz));assert(Math.max(...r.map(q=>q.x))-Math.min(...r.map(q=>q.x))<.15);assert(Math.max(...r.map(q=>q.cap))-Math.min(...r.map(q=>q.cap))<.02);});
Object.assign(c,{TOOLS:['grumier','frigorifique','citerne'].map(key=>({key})),SEMI_PARC:{x:[464,475,486],z:-94}});
test('Old unused delivery places migrate once, including trailers bought backwards',()=>{const S={outils:[468,496,552].map(x=>({x,z:-93,cap:Math.PI,porteur:-1,load:23}))};assert.equal(c.migrerParcSemi(S),3);assert.deepEqual(S.outils.map(q=>q.x),[464,475,486]);assert(S.outils.every(q=>q.cap===0&&q.z===-94&&q.load===23));assert.equal(c.migrerParcSemi(S),0);});
test('Migration preserves attached trailers and trailers moved by the player',()=>{const S={outils:[{x:468,z:-93,porteur:2},{x:502,z:-93,porteur:-1}]},old=JSON.stringify(S.outils);assert.equal(c.migrerParcSemi(S),0);assert.equal(JSON.stringify(S.outils),old);});
console.log(n+' trailer contact and parking tests passed.');
