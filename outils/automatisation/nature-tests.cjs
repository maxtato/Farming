const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict'),path=require('node:path');
const source=fs.readFileSync(path.join(__dirname,'../../index.html'),'utf8');
const block=source.slice(source.indexOf('function objectifAutomatique('),source.indexOf('function combinePret('));
function setup(){
 const c=vm.createContext({Math,Map,Set,Number,JSON,Infinity,planEl:{style:{display:'none'}},showHint(){},chLot:[],chContinu:false,
  FORET:{x0:-20,x1:100,z0:-20,z1:100,arbres:[{x:6,z:0,kg:10,etat:0},{x:20,z:10,kg:20,etat:0}]},obstacles:[],boxObs:[],EAU:{x0:-100,x1:100,z0:-100,z1:100},
  DEPOT_BOIS:{stock:0,max:100},PORT:{spots:[{x:20,z:20},{x:40,z:40},{x:60,z:60}],debarque:{x:0,z:0},spotR:8},QUAI_PECHE:{stock:{},max:100},
  MACHINES:[],enginLibre:m=>!m.verrou&&!m.v.mission&&!m.v.auto,armerEngin(m,t){m.v.mission={taches:t};m.v.auto=true;},arreterMission(m){m.v.mission=null;m.v.auto=false;},
  arbreAPortee:()=>null,lancerCoupe:()=>true,viser:()=>[0,.5],pasDeRecul:()=>null,suivreRoute:()=>[0,.5],naturesDe:K=>K.load>0?[K.type||'poisson']:[]});
 c.depotPrend=a=>c.DEPOT_BOIS.stock+a.kg<=c.DEPOT_BOIS.max;c.quaiPecheTotal=()=>Object.values(c.QUAI_PECHE.stock).reduce((a,b)=>a+b,0);
 for(const key of ['abatteuse','barque','chalutier','caseyeur','t1'])c.MACHINES.push({key,nom:key,verrou:false,bateau:['barque','chalutier','caseyeur'].includes(key),peche:['barque','chalutier','caseyeur'].includes(key)?{cle:'poisson'}:null,v:{pos:{x:0,z:0},vmax:8,speed:0,cargo:{load:0,capacite:60},mission:null,auto:false}});
 vm.runInContext(block+'\nthis.jobs=NATURE_JOBS;this.natureJob=natureJob;',c);return c;
}
let n=0;function test(name,f){f(setup());n++;console.log('PASS '+name);}
test('Only owned forestry and fishing machines can start these jobs',c=>{c.MACHINES[0].verrou=true;assert.equal(c.poserNature('abatteuse',false),null);assert.equal(c.poserNature('t1',false),null);assert.equal(c.jobs.length,0);});
test('A working vehicle cannot receive another job or be stolen',c=>{c.MACHINES[1].v.mission={taches:[{quoi:'navette'}]};assert.equal(c.poserNature('barque',false),null);});
test('Starting twice changes continuous mode without duplicating a worker',c=>{const J=c.poserNature('barque',false),M=c.MACHINES[1].v.mission;assert.equal(c.poserNature('barque',true),J);assert.equal(c.jobs.length,1);assert(J.continu);assert.equal(c.MACHINES[1].v.mission,M);});
test('A woodcutting round keeps only the mature trees present at launch',c=>{c.FORET.arbres[1].etat=2;const J=c.poserNature('abatteuse',false);assert.equal(J.arbres.join(','),'0');c.FORET.arbres[1].etat=0;assert.equal(J.arbres.length,1);});
test('A completed one-off wood job disappears; a continuous one waits for regrowth',c=>{c.FORET.arbres.forEach(a=>a.etat=1);c.poserNature('abatteuse',false);c.conduireNature(c.MACHINES[0],.1);assert.equal(c.jobs.length,0);const J=c.poserNature('abatteuse',true);c.conduireNature(c.MACHINES[0],.1);assert.equal(c.jobs.length,1);assert.match(J.statut,/repousse/);});
test('Full timber storage pauses without cutting or dropping the job',c=>{c.DEPOT_BOIS.stock=100;const J=c.poserNature('abatteuse',false);assert.equal(c.conduireNature(c.MACHINES[0],.1).join(','),'0,0');assert.match(J.statut,/plein/);assert.equal(J.arbres.length,2);assert.equal(c.DEPOT_BOIS.stock,100);});
test('Three simultaneous fishing boats reserve three different spots',c=>{for(const m of c.MACHINES.slice(1,4)){c.poserNature(m.key,true);c.conduireNature(m,.1);}assert.equal(new Set(c.jobs.map(J=>J.cible)).size,3);});
test('A full fishing hold returns to the quay and waits if the quay is full',c=>{const m=c.MACHINES[1];m.v.cargo.load=60;const J=c.poserNature(m.key,false);c.QUAI_PECHE.stock.poisson=100;c.conduireNature(m,.1);assert.equal(J.phase,'vider');assert.match(J.statut,/plein/);assert.equal(m.v.cargo.load,60);assert.equal(c.jobs.length,1);});
test('A continuous fishing job restarts only after its hold is empty',c=>{const m=c.MACHINES[1],J=c.poserNature(m.key,true);J.phase='vider';c.conduireNature(m,.1);assert.equal(J.phase,'aller');assert.equal(c.jobs.length,1);});
test('An incompatible partial hold is unloaded before more fishing',c=>{const m=c.MACHINES[1];m.v.cargo.load=10;m.v.cargo.type='crustaces';const J=c.poserNature(m.key,false);c.conduireNature(m,.1);assert.equal(J.phase,'vider');});
test('Cancel removes its mission and row without removing the other workers',c=>{c.poserNature('barque',true);c.poserNature('abatteuse',true);c.retirerNature('barque');assert.equal(c.jobs.length,1);assert.equal(c.MACHINES[1].v.auto,false);assert(c.MACHINES[0].v.auto);});
test('Saving copies remaining trees and restores unloading and continuous mode',c=>{const J=c.poserNature('abatteuse',true);c.poserNature('barque',true).phase='vider';const S=c.sauverNature();J.arbres.pop();assert.equal(S[0].arbres.length,2);c.chargerNature(S);assert.equal(c.jobs.length,2);assert.equal(c.natureJob('barque').phase,'vider');assert(c.natureJob('barque').continu);});
test('Legacy saves without nature jobs remain valid',c=>{c.poserNature('barque',true);c.chargerNature(undefined);assert.equal(c.jobs.length,0);});
test('Navigation goes around a solid obstruction instead of translating through it',c=>{c.boxObs.push({x:15,z:0,hw:3,hd:12});const v={pos:{x:0,z:0},bateau:true},goal={x:30,z:0};const P=c.cheminNature(v,goal);assert(P&&P.length>1);let a=v.pos;for(const b of P){assert(c.natureSegment(a,b,true));a=b;}assert.equal(a.x,goal.x);assert.equal(a.z,goal.z);});
test('Boat paths cannot cross the coast or leave the water',c=>{assert.equal(c.natureLibre(110,0,true),false);assert.equal(c.natureLibre(0,-99,true),false);assert.equal(c.cheminNature({pos:{x:0,z:0},bateau:true},{x:120,z:0}),null);});
test('The cutter can target an in-range tree even when its neighbour is closer',c=>{
 const a=source.indexOf('function lancerCoupe(');c.PORTEE_ABATTAGE=5.5;c.effaroucherForet=()=>{};c.RAYON_EFFAROUCHE=14;
 vm.runInContext(source.slice(a,source.indexOf('\n}',a)+2),c);
 const m=c.MACHINES[0];m.v.fwd=()=>({x:1,z:0});c.arbreAPortee=()=>c.FORET.arbres[0];
 const target={x:8,z:0,kg:20,etat:0};assert(c.lancerCoupe(m,target));assert.equal(m.v.coupe.a,target);
 m.v.coupe=null;assert.equal(c.lancerCoupe(m,{x:40,z:0,kg:20,etat:0}),false);assert.equal(m.v.coupe,null);
});
console.log(n+' nature automation tests passed.');
