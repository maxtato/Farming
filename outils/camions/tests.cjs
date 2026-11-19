const fs=require('node:fs'),path=require('node:path'),vm=require('node:vm'),assert=require('node:assert/strict');
const s=fs.readFileSync(path.join(__dirname,'../../index.html'),'utf8');
const ctx=vm.createContext({Math});
for(const nom of ['chargeSemi','lacetRoutier','moteurSemi','suivreSemi']){const a=s.indexOf('function '+nom+'(');assert(a>=0);vm.runInContext(s.slice(a,s.indexOf('\n}',a)+2),ctx);}
let n=0;const test=(name,run)=>{run();n++;console.log('PASS',name);};
function truck(load=null){const v={vmax:19,turn:1.05,cap:0,gaz:0,conduiteLongue:{rayon:9.5,lateral:11}};if(load!==null)v.tool={semi:true,attached:v,load,capacite:1000,cap:0};return v;}
function run(v,seconds,throttle=1,hz=60,speed=0,brake=false){for(let i=0;i<seconds*hz;i++)speed=ctx.moteurSemi(v,1/hz,throttle,brake,speed,6.2)*Math.exp(-.16/hz);return speed;}
function trailer(){return {L:12,cap:0,axle:{x:0,z:-12},group:{rotation:{z:0}},load:0,capacite:1000};}
test('Refrigerated truck turns wider at low speed and matches van response on the road',()=>{const v={turn:1.8,conduiteLongue:{rayon:6.5,lateral:27}};assert.equal(3/ctx.lacetRoutier(v,1,3),6.5);assert.equal(ctx.lacetRoutier(v,1,12),1.8);assert(ctx.lacetRoutier(v,1,3)<ctx.lacetRoutier({turn:1.8},1,3));});
test('Long vehicles cannot pivot at rest and reverse steering direction',()=>{const v=truck();assert.equal(ctx.lacetRoutier(v,1,0),0);assert.equal(ctx.lacetRoutier(v,1,-3),-ctx.lacetRoutier(v,1,3));assert(19*ctx.lacetRoutier(v,1,19)<=11.0001);});
test('Automatic driving retains the steering expected by its route planner',()=>{for(const flag of ['auto','mission']){const v=truck();v[flag]=true;assert.equal(ctx.lacetRoutier(v,.8,4),.8*v.turn);}});
test('Throttle builds progressively and loaded trailers accelerate more slowly',()=>{const a=truck(),b=truck(0),c=truck(1000);assert(run(truck(),.5)<1);const speeds=[run(a,4),run(b,4),run(c,4)];assert(speeds[0]>speeds[1]&&speeds[1]>speeds[2]);assert(speeds[2]>5);});
test('Braking overrides held throttle and reversal must pass through a stop',()=>{const v=truck(1000);assert.equal(run(v,5,1,60,15,true),0);assert(ctx.moteurSemi(v,.1,-1,false,.2,6.2)>=0);assert(run(truck(),4,-1,60,0)<-1);});
test('Reverse speed is limited and a folded trailer stops reversing',()=>{assert(Math.abs(run(truck(),10,-1))<=4.2);const v=truck(0);v.tool.cap=1.35;assert.equal(run(v,3,-1,60,-2),0);assert(run(v,3,1)>1);});
test('Coasting retains momentum while braking remains effective',()=>{assert(run(truck(),1,0,60,15)>10);assert(run(truck(),1,0,60,15,true)<9);});
test('Trailer axle keeps the exact hitch distance and stays still at rest',()=>{const T=trailer();for(let i=0;i<600;i++){ctx.suivreSemi(T,0,i/10,1/60);assert(Math.abs(Math.hypot(T.axle.x,T.axle.z-i/10)-12)<1e-9);}const cap=T.cap,x=T.axle.x,z=T.axle.z;for(let i=0;i<120;i++)ctx.suivreSemi(T,0,59.9,1/60);assert.equal(T.cap,cap);assert.equal(T.axle.x,x);assert.equal(T.axle.z,z);});
test('A trailer cuts inside a curve and straightens through forward travel',()=>{const T=trailer(),R=20;for(let i=1;i<=240;i++){const a=i/240*Math.PI/2;ctx.suivreSemi(T,R*(1-Math.cos(a)),R*Math.sin(a),1/60);}assert(T.cap>0&&T.cap<Math.PI/2);for(let i=1;i<=1200;i++)ctx.suivreSemi(T,20+i*.1,20,1/60);assert(Math.abs(T.cap-Math.PI/2)<.001);});
test('Trailer tracking and acceleration remain consistent at 30, 60 and 120 Hz',()=>{const results=[];for(const hz of [30,60,120]){const T=trailer();for(let i=1;i<=hz*8;i++){const a=i/(hz*8)*Math.PI/2;ctx.suivreSemi(T,20*(1-Math.cos(a)),20*Math.sin(a),1/hz);}results.push({cap:T.cap,speed:run(truck(1000),8,1,hz)});}assert(Math.max(...results.map(r=>r.cap))-Math.min(...results.map(r=>r.cap))<.001);assert(Math.max(...results.map(r=>r.speed))-Math.min(...results.map(r=>r.speed))<.08);});
console.log(n+' truck tests passed.');
