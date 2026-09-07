// node outils/arcade/tests.cjs -- no dependencies; executes the actual game functions.
const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict'),path=require('node:path');
const source=fs.readFileSync(path.join(__dirname,'../../index.html'),'utf8');
function fn(name){const a=source.indexOf('function '+name+'(');assert(a>=0,name);const line=source.slice(a,source.indexOf('\n',a));return line.trimEnd().endsWith('}')?line:source.slice(a,source.indexOf('\n}',a)+2);}
const noise=Object.create(Math);noise.random=()=>1;
const ctx=vm.createContext({Math:noise,WeakMap,mondePret:true,INTRO:{actif:false},SUSP_LIM:{r:.17,p:.1},ECART_VOIE_MAX:3.5,tempsTrafic:10,
 _gabA:[],_gabB:[],_gabT:[],MACHINES:[],cur:0,TRAFIC:[],obstacles:[],boxObs:[],fantomeAuto:()=>false,SELLETTE_TRAFIC:2,TIMON_TRAFIC:12,impacts:[],AUDIO:{impact(...args){ctx.impacts.push(args);}},secouer(){},siSouvent:()=>false,puff(){}});
const choc=source.slice(source.indexOf('const CHOC ='),source.indexOf('};',source.indexOf('const CHOC ='))+2);
vm.runInContext(choc+'\n'+source.match(/const ETAT_REPOS =[^;]+;/)[0]+'\nconst SON_CIBLES=new WeakMap();\n'+['borner','suspension','directionArcade','enginAuRepos','segSeg','prochesGabarits','right','pivotChoc','choquerEngins','choquerTrafic','freinCarrefour','sonCible','angleTrafic','reprendreVolant','tournerAuChoc','passageReprise','conduireReprise','surItineraire'].map(fn).join('\n'),ctx);
function capsule(x,z,r=1){return {x1:x,z1:z,x2:x,z2:z,r};}
function car(x,z,vx=0,vz=0){return {pos:{x,z},vel:{x:vx,y:vz},cap:0,grip:5,vmax:15,fwd:()=>({x:0,z:1}),right:()=>({x:1,z:0})};}
ctx.gabarits=v=>v.caps||[capsule(v.pos.x,v.pos.z)];
ctx.gabaritsTrafic=t=>{if(!t.m)t.m={position:{x:t.x,z:t.z}};t.avant??=2;t.arriere??=2;return [capsule(t.m.position.x,t.m.position.z)];};
let passed=0;
function test(name,body){body();passed++;console.log('PASS',name);}
test('All inline JavaScript parses',()=>{for(const m of source.matchAll(/<script\b[^>]*>([\s\S]*?)<\/script>/g))new vm.Script(m[1]);});
test('Frontal collision dissipates energy and conserves momentum',()=>{
 for(const speed of [1,5,15,25]){let a=car(0,0,speed),b=car(1.5,0,-speed/2);ctx.MACHINES=[{v:a}];ctx.choquerEngins(a,b);
 assert(Math.hypot(b.pos.x-a.pos.x,b.pos.z-a.pos.z)>=2-1e-9);
 assert(Math.abs(a.vel.x+b.vel.x-speed/2)<1e-9);assert(a.vel.x*a.vel.x+b.vel.x*b.vel.x<=1.25*speed*speed);}
});
test('Separating contacts create neither impulse nor sound',()=>{let a=car(0,0,-5),b=car(1,0,5);ctx.MACHINES=[{v:a}];ctx.impacts=[];ctx.choquerEngins(a,b);assert.equal(a.vel.x,-5);assert.equal(b.vel.x,5);assert.equal(ctx.impacts.length,0);});
test('Coincident capsules separate using a finite unit normal',()=>{let a=car(0,0),b=car(0,0);ctx.MACHINES=[{v:a}];ctx.choquerEngins(a,b);assert.equal(Math.hypot(b.pos.x-a.pos.x,b.pos.z-a.pos.z),2);});
test('Grazing preserves tangential movement',()=>{let a=car(0,0,.02,15),b=car(1.9,0,0,15);ctx.MACHINES=[{v:a}];ctx.impacts=[];ctx.choquerEngins(a,b);assert.equal(a.vel.y,15);assert.equal(b.vel.y,15);assert.equal(ctx.impacts.length,0);});
test('Broad phase keeps every real overlap, including long tools',()=>{
 let seed=92;const rnd=()=>((seed=Math.imul(seed,1664525)+1013904223>>>0)/4294967296);
 for(let i=0;i<10000;i++){const a={x1:rnd()*60,z1:rnd()*60,x2:rnd()*60,z2:rnd()*60,r:rnd()*3},b={x1:rnd()*60,z1:rnd()*60,x2:rnd()*60,z2:rnd()*60,r:rnd()*3};
 const p=ctx.segSeg(a.x1,a.z1,a.x2,a.z2,b.x1,b.z1,b.x2,b.z2);if(Math.hypot(p.x2-p.x1,p.z2-p.z1)<a.r+b.r)assert(ctx.prochesGabarits([a],[b]));}
 assert(ctx.prochesGabarits([capsule(0,0),{x1:0,z1:5,x2:15,z2:5,r:1}],[capsule(14,5)]));
});
test('Repeated traffic contact cannot catapult the player',()=>{const a=car(0,0,15);const t={x:1,z:0,ox:0,oz:0,vox:0,voz:0,vit:0,fx:0,fz:1,choc:0,rollV:0,pitchV:0};ctx.MACHINES=[{v:a}];ctx.impacts=[];
 for(let i=0;i<120;i++){ctx.choquerTrafic(a,t);assert(Number.isFinite(a.speed));assert(Math.hypot(a.vel.x,a.vel.y)<=15+1e-9);assert(Math.hypot(t.ox,t.oz)<=3.5+1e-9);}
 assert.equal(ctx.impacts.length,1);
});
test('Traffic separating from the player is silent',()=>{const a=car(0,0,-5),t={x:1,z:0,ox:0,oz:0,vox:5,voz:0,vit:0,fx:0,fz:1,choc:0,rollV:0,pitchV:0};ctx.MACHINES=[{v:a}];ctx.impacts=[];ctx.choquerTrafic(a,t);assert.equal(a.vel.x,-5);assert.equal(t.vox,5);assert.equal(ctx.impacts.length,0);});
test('Suspension at 30, 60 and 120 Hz remains consistent and settles',()=>{
 const outputs=[];for(const hz of [30,60,120]){const o={roll:0,rollV:0,pitch:0,pitchV:0,heave:0,heaveV:0,bump:0},s={k:22,d:4.6,roll:.052,pitch:.032,rough:0};
 for(let i=0;i<hz;i++)ctx.suspension(o,s,1/hz,2,1,0);outputs.push(o.roll);assert(o.roll>0&&o.pitch<0);
 for(let i=0;i<hz*5;i++)ctx.suspension(o,s,1/hz,0,0,0);assert(Math.abs(o.roll)<.001);}
 assert(Math.max(...outputs)-Math.min(...outputs)<1e-9);
});
test('Steering responds quickly, returns to centre, preserves autopilot grip',()=>{const a=car(0,0);let d;for(let i=0;i<6;i++)d=ctx.directionArcade(a,1/60,1,15);assert(d.steer>.88);assert(d.grip<5&&d.grip>4);for(let i=0;i<30;i++)d=ctx.directionArcade(a,1/60,0,15);assert.equal(d.steer,0);a.auto=true;assert.equal(ctx.directionArcade(a,1/60,-1,15).grip,5);assert.equal(a.braquage,-1);});
test('Parked machines wake for movement, suspension, work and autopilot',()=>{const a=car(0,0);assert(ctx.enginAuRepos(a));for(const [key,value] of [['auto',true],['mission',{}],['bateau',true],['coupe',true],['augerOut',true],['rollV',.01],['cLacet',.01]]){a[key]=value;assert(!ctx.enginAuRepos(a),key);delete a[key];}a.vel.x=.05;assert(!ctx.enginAuRepos(a));});
test('Intersection yields to an occupied crossing then releases',()=>{const a={s:80,avant:2,arriere:2,v:10,vit:10,t0:2,actif:true,route:{croix:[{iC:1,h:true,sIn:100,sOut:110}]}},b={s:102,avant:2,arriere:2,v:10,vit:10,t0:1,actif:true,route:{croix:[{iC:1,h:false,sIn:100,sOut:110}]}};ctx.TRAFIC=[a,b];a.s=94;assert(ctx.freinCarrefour(a)<1);b.s=115;assert.equal(ctx.freinCarrefour(a),1);b.s=94;assert.equal(ctx.freinCarrefour(b),1);assert(ctx.freinCarrefour(a)<1);});
test('Audio avoids duplicate automation and always allows silence',()=>{let calls=[];const p={setTargetAtTime:(...v)=>calls.push(v)};ctx.sonCible(p,.5,0,.1);for(let i=1;i<60;i++)ctx.sonCible(p,.5,i/60,.1);assert.equal(calls.length,1);ctx.sonCible(p,.6,1,.1);ctx.sonCible(p,0,1.001,.1);assert.equal(calls.at(-1)[0],0);ctx.sonCible(p,.6,1.1,.1);assert.equal(calls.at(-1)[0],.6);});
function traffic(x=0,cap=0){return {m:{position:{x,z:50}},s:50,route:{legs:[{t:'d',x:0,z:0,dx:0,dz:1,L:1000}],L:1000},cap,fx:Math.sin(cap),fz:Math.cos(cap),t0:0,v:12,vit:0,ox:x,oz:0,vox:0,voz:0,avant:3,arriere:3,choc:0,k:0};}
function drive(t,seconds,hz=60){let reverse=false,maxYaw=0;for(let i=0;i<seconds*hz;i++){ctx.tempsTrafic+=1/hz;const cap=t.cap;if(t.reprise)ctx.conduireReprise(t,1/hz,1);reverse||=t.vit<-.05;maxYaw=Math.max(maxYaw,Math.abs(ctx.angleTrafic(t.cap-cap)));}return {reverse,maxYaw};}
test('Rear corner impact rotates opposite corners in opposite directions',()=>{for(const side of [-1,1]){const t=traffic();ctx.tournerAuChoc(t,side*1.5,47,0,1,9);assert(Math.sign(t.reprise.lacet)===-side);assert(Math.abs(t.reprise.lacet)>.3);}});
test('A displaced stationary car never slides back toward its lane',()=>{const t=traffic(3);ctx.MACHINES=[];ctx.TRAFIC=[];ctx.reprendreVolant(t);t.choc=1;for(let i=0;i<120;i++)ctx.conduireReprise(t,1/60,0);assert.equal(t.m.position.x,3);assert.equal(t.m.position.z,50);});
test('Recovery motion follows the heading, then rejoins the lane',()=>{ctx.MACHINES=[];ctx.TRAFIC=[];const t=traffic(3,.6);ctx.reprendreVolant(t);let changed=0;for(let i=0;i<1800&&t.reprise;i++){const x=t.m.position.x,z=t.m.position.z,a=t.cap;ctx.tempsTrafic+=1/60;ctx.conduireReprise(t,1/60,1);const mid=(a+t.cap)/2;assert(Math.abs((t.m.position.x-x)*Math.cos(mid)-(t.m.position.z-z)*Math.sin(mid))<1e-8);changed=Math.max(changed,Math.abs(t.cap-.6));}assert(changed>.5);assert(Math.abs(t.m.position.x)<.04);assert(Math.abs(t.cap)<.015);assert.equal(t.reprise,null);});
test('A car spun across the lane reverses and drives back into alignment',()=>{const t=traffic(3,1.7);ctx.reprendreVolant(t);const result=drive(t,45);assert(result.reverse);assert(result.maxYaw<.1);assert(Math.abs(t.m.position.x)<.04);assert.equal(t.reprise,null);});
test('Recovery refuses to reverse through another vehicle',()=>{const t=traffic(3,1.7);ctx.reprendreVolant(t);const obstacle=car(t.m.position.x-Math.sin(t.cap)*2,t.m.position.z-Math.cos(t.cap)*2);ctx.MACHINES=[{v:obstacle}];const x=t.m.position.x,z=t.m.position.z;assert.equal(ctx.passageReprise(t,x-Math.sin(t.cap)*.2,z-Math.cos(t.cap)*.2,t.cap),false);ctx.MACHINES=[];});
test('Recovery is consistent at 30 / 60 / 120 Hz',()=>{const positions=[];for(const hz of [30,60,120]){const t=traffic(3,.7);ctx.reprendreVolant(t);drive(t,10,hz);positions.push(t.m.position.x);assert(Number.isFinite(t.cap));}assert(Math.max(...positions)-Math.min(...positions)<.05);});
test('An aligned articulated truck rejoins without a one-frame axle lag',()=>{const t=traffic();t.lourd=true;t.tcap=0;t.vit=6;ctx.MACHINES=[];ctx.TRAFIC=[];ctx.reprendreVolant(t);ctx.conduireReprise(t,1/60,1);assert.equal(t.reprise,null);});
console.log(`${passed} tests passed.`);
