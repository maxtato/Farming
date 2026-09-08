const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict'),path=require('node:path');
const source=fs.readFileSync(path.join(__dirname,'../../index.html'),'utf8');
function fn(name){const a=source.indexOf('function '+name+'(');assert(a>=0,name);return source.slice(a,source.indexOf('\n}',a)+2);}
function setup(){
 const c=vm.createContext({Math,MACHINES:[],TOOLS:[],CHANTIERS:[],chLot:[],planTaches:[],HALLE:{file:[]},cur:-1,MODE_LIBRE:false,CAMPAGNE:{tuto:10},TUTO_TERRE:5,
 CROPS:[{cle:'ble',nom:'Blé'},{cle:'mais',nom:'Maïs'}],PARCELS:[{x:10,z:0},{x:30,z:0},{x:50,z:0}],
 CUVES:{graines:{ble:100,mais:100},engrais:100},ET_LABOUR:'labour',ET_SEMIS:'semis',ET_ENGRAIS:'engrais',ET_MOISSON:'moisson',ET_FINI:'fini',ET_POUSSE:'pousse',
 NOM_ETAPE:{labour:'Labour',semis:'Semis',engrais:'Engrais',moisson:'Moisson'},
 EST_TRACTEUR:m=>m.key.startsWith('t'),cuveDe:(t,k)=>t.cuves[k]||0,siloPlein:()=>false,showHint(){},
 bacsDe:t=>t.seme?[{engrais:false}]:[],aServi:(c,i)=>i,etapeChantier:c=>c.demande,etapeMarchandise:()=>null,
 caisseDe:m=>m.v.cargo,accepteNature:(k,cle)=>!k.prend||k.prend.includes(cle),rentrerAuParc(){}});
 const a=source.indexOf('const classeDe ='),b=source.indexOf('/* UN ENGIN EST LIBRE',a);
 const d=source.indexOf('const rentreAuParc ='),e=source.indexOf('/* ARMER UN ENGIN',d);
 vm.runInContext(source.slice(a,b)+source.slice(d,e)+['combinePret','besoinEtape','blocageEtape','enginLePlusProche','outilReserve','enginPourOutil','armerEngin','tachesEtape','pisteTerre','armerPorteur','retirerChantiersTermines'].map(fn).join('\n'),c);
 c.MACHINES.push(...['t1','t2','t4','pickup','fourgon'].map((key,i)=>({key,verrou:false,v:{pos:{x:i*2,z:0},auto:false,mission:null,cargo:i>=3?{capacite:100,load:0}:null}})));
 c.TOOLS.push(...['labour','semis','engrais','combine','benne'].map(key=>({key,nom:key,verrou:false,attached:null,cuves:{},seme:key==='semis'||key==='combine',fertilise:key==='engrais'||key==='combine',pourEngin:key==='combine'?'t4':null,cargo:key==='benne'})));
 return c;
}
let n=0;
function test(name,f){f(setup());n++;console.log('PASS '+name);}
function chantier(c,p,demande='labour'){const C={p,crop:0,demande,enginTerre:-1,enginPort:-1,continu:true};c.CHANTIERS.push(C);return C;}
function lancer(c,C){c.pisteTerre(C,c.CHANTIERS.indexOf(C));}
test('Two simultaneous ploughing parcels use the combine and the ordinary plough',c=>{
 const a=chantier(c,0),b=chantier(c,1);lancer(c,a);lancer(c,b);
 assert.equal(a.enginTerre,2);assert(b.enginTerre>=0&&b.enginTerre!==2);
 assert.equal(c.MACHINES[a.enginTerre].v.mission.taches[0].t,3);
 assert.equal(c.MACHINES[b.enginTerre].v.mission.taches[0].t,0);
 assert.equal(c.MACHINES[a.enginTerre].v.mission.taches.at(-1).p,0);
 assert.equal(c.MACHINES[b.enginTerre].v.mission.taches.at(-1).p,1);
});
test('An unattached tool is reserved while its tractor travels to collect it',c=>{
 c.TOOLS[3].verrou=true;const a=chantier(c,0),b=chantier(c,1);lancer(c,a);lancer(c,b);
 assert(a.enginTerre>=0);assert.equal(b.enginTerre,-1);assert(c.outilReserve(0));
});
test('Cancelling a task frees its uncollected tool for another parcel',c=>{
 c.TOOLS[3].verrou=true;const a=chantier(c,0),b=chantier(c,1);lancer(c,a);
 const m=c.MACHINES[a.enginTerre];m.v.mission=null;m.v.auto=false;c.CHANTIERS.splice(0,1);
 lancer(c,b);assert(b.enginTerre>=0);
});
test('A busy attached implement is neither stolen nor assigned to a second tractor',c=>{
 c.TOOLS[0].attached=c.MACHINES[0].v;c.MACHINES[0].v.auto=true;
 assert.equal(c.enginPourOutil('tracteur',c.PARCELS[0],0),-1);
 c.MACHINES[0].v.auto=false;assert.equal(c.enginPourOutil('tracteur',c.PARCELS[0],0),0);
});
test('A free simple implement can work when the combine lacks seed',c=>{
 c.CUVES.graines.ble=0;const a=chantier(c,0);lancer(c,a);
 assert(a.enginTerre>=0);assert.equal(c.MACHINES[a.enginTerre].v.mission.taches[0].t,0);
});
test('Parallel sowing retains the separate crop choice of both tools',c=>{
 const a=chantier(c,0,'semis'),b=chantier(c,1,'semis');b.crop=1;lancer(c,a);lancer(c,b);
 assert.notEqual(a.enginTerre,b.enginTerre);assert.equal(c.TOOLS[3].crop,0);assert.equal(c.TOOLS[1].crop,1);
});
test('Fertilizing never dispatches an empty combine when no fertilizer is available',c=>{
 c.CUVES.engrais=0;const a=chantier(c,0,'engrais');lancer(c,a);
 assert.equal(a.enginTerre,-1);assert.match(a.bloque,/ENGRAIS/);
});
test('Three different available implements can work on separate parcels together',c=>{
 c.TOOLS[3].verrou=true;const jobs=['labour','semis','engrais'].map((e,i)=>chantier(c,i,e));
 jobs.forEach(C=>lancer(c,C));assert.equal(new Set(jobs.map(C=>C.enginTerre)).size,3);assert(jobs.every(C=>C.enginTerre>=0));
});
test('Revisiting an active parcel never starts an additional worker',c=>{
 const a=chantier(c,0);lancer(c,a);const i=a.enginTerre;const mission=c.MACHINES[i].v.mission;
 for(let j=0;j<8;j++)lancer(c,a);assert.equal(c.MACHINES[i].v.mission,mission);assert.equal(c.MACHINES.filter(m=>m.v.mission).length,1);
});
test('A vehicle returning to the parking can take new work immediately',c=>{
 c.TOOLS[0].attached=c.MACHINES[0].v;c.armerEngin(c.MACHINES[0],[{quoi:'parc'}]);
 assert.equal(c.enginPourOutil('tracteur',c.PARCELS[0],0),0);
});
test('Two deliveries use different available vehicles and different destinations',c=>{
 const a=chantier(c,0),b=chantier(c,1);
 assert(c.armerPorteur(a,'enginPort',c.PARCELS[0],()=>[{quoi:'navette',a:'silo',b:'boulangerie',cle:'ble'}]));
 assert(c.armerPorteur(b,'enginPort',c.PARCELS[1],()=>[{quoi:'navette',a:'entrepot',b:'epicerie',cle:'farine'}]));
 assert.notEqual(a.enginPort,b.enginPort);
});
test('Transport skips boats and incompatible cargo instead of blocking the right vehicle',c=>{
 c.MACHINES[3].v.bateau=true;const a=chantier(c,0);
 assert(c.armerPorteur(a,'enginPort',c.PARCELS[0],()=>[{quoi:'navette',cle:'lait'}]));assert.equal(a.enginPort,4);
 const b=chantier(c,1);c.MACHINES[3].v.bateau=false;c.MACHINES[3].v.cargo.prend=['grumes'];
 assert(c.armerPorteur(b,'enginPort',c.PARCELS[1],()=>[{quoi:'navette',cle:'lait'}]));assert(b.enginPort<3);
});
test('Two tractor deliveries cannot reserve the same loose trailer',c=>{
 c.MACHINES[3].verrou=c.MACHINES[4].verrou=true;const a=chantier(c,0),b=chantier(c,1);
 const faire=()=>[{quoi:'navette',a:'silo',b:'epicerie',cle:'ble'}];
 assert(c.armerPorteur(a,'enginPort',c.PARCELS[0],faire));assert.equal(c.armerPorteur(b,'enginPort',c.PARCELS[1],faire),false);
});
test('A finished one-off task disappears from both the list and selected map parcels',c=>{
 const a=chantier(c,0,'fini');a.continu=false;c.chLot=[0,1];c.planTaches=[{quoi:'parcelle',p:0},{quoi:'parcelle',p:1}];
 assert(c.retirerChantiersTermines());assert.equal(c.CHANTIERS.length,0);
 assert.equal(c.chLot.join(','),'1');assert.equal(c.planTaches.length,1);assert.equal(c.planTaches[0].p,1);
 assert.equal(c.retirerChantiersTermines(),false);
});
test('A completed harvest finishes without starting another growing cycle',c=>{
 const a=chantier(c,0,'labour');a.continu=false;a.etape='moisson';
 assert(c.retirerChantiersTermines());assert.equal(a.recolte,true);
});
test('A delivery in progress keeps the task until its vehicle finishes',c=>{
 const a=chantier(c,0,'fini');a.continu=false;a.enginPort=3;c.armerEngin(c.MACHINES[3],[{quoi:'navette',cle:'ble'}]);
 assert.equal(c.retirerChantiersTermines(),false);c.MACHINES[3].v.mission=null;
 assert(c.retirerChantiersTermines());
});
test('Queued production and remaining merchandise keep unfinished tasks visible',c=>{
 const a=chantier(c,0,'fini');a.continu=false;a.produit='farine';c.HALLE.file.push({cle:'farine'});
 assert.equal(c.retirerChantiersTermines(),false);c.HALLE.file.length=0;c.etapeMarchandise=()=>({et:'livrer'});
 assert.equal(c.retirerChantiersTermines(),false);c.etapeMarchandise=()=>null;assert(c.retirerChantiersTermines());
});
test('A blocked destination does not erase undelivered work',c=>{
 const a=chantier(c,0,'fini');a.continu=false;c.etapeMarchandise=()=>({mal:'Destination pleine'});
 assert.equal(c.retirerChantiersTermines(),false);
});
test('Continuous jobs and crops still growing remain in the automation window',c=>{
 chantier(c,0,'fini');const b=chantier(c,1,'pousse');b.continu=false;
 assert.equal(c.retirerChantiersTermines(),false);assert.equal(c.CHANTIERS.length,2);
});
test('Returning to parking does not keep a completed task visible',c=>{
 const a=chantier(c,0,'fini');a.continu=false;a.enginTerre=0;c.armerEngin(c.MACHINES[0],[{quoi:'parc'}]);
 assert(c.retirerChantiersTermines());assert.equal(c.MACHINES[0].v.mission.taches[0].quoi,'parc');
});
test('A one-off livestock task disappears only after its delivery ends',c=>{
 const a=chantier(c,0);a.continu=false;a.quoi='elevage';assert.equal(c.retirerChantiersTermines(),false);
 a.livre=true;assert(c.retirerChantiersTermines());
});
test('Free mode dispatches both owned tractors even before the tutorial ends',c=>{
 c.MODE_LIBRE=true;c.CAMPAGNE.tuto=0;const a=chantier(c,0),b=chantier(c,1);lancer(c,a);lancer(c,b);
 assert(a.enginTerre>=0&&b.enginTerre>=0);assert.notEqual(a.enginTerre,b.enginTerre);
});
test('Campaign still teaches individual tools before the combine',c=>{
 c.CAMPAGNE.tuto=0;assert.equal(c.combinePret(),false);
});
test('Adding a parcel to an identical active lot preserves its worker and mission',c=>{
 vm.runInContext(fn('poserChantier'),c);
 const a=c.poserChantier(0,{continu:true});a.demande='labour';lancer(c,a);
 const worker=a.enginTerre,mission=c.MACHINES[worker].v.mission;
 assert.equal(c.poserChantier(0,{continu:false}),a);assert.equal(a.enginTerre,worker);assert.equal(a.continu,false);
 const b=c.poserChantier(1,{continu:true});b.demande='labour';lancer(c,b);
 assert(b.enginTerre>=0&&b.enginTerre!==worker);assert.equal(c.MACHINES[worker].v.mission,mission);
});
test('Changing a parcel configuration cancels its old orders before replacing it',c=>{
 c.arreterMission=m=>{m.v.mission=null;m.v.auto=false;};c.aRentrer=()=>{};
 vm.runInContext(fn('poserChantier')+fn('retirerChantier'),c);
 const a=c.poserChantier(0,{continu:true});a.demande='labour';lancer(c,a);const worker=a.enginTerre;
 const b=c.poserChantier(0,{continu:true,crop:1});assert.notEqual(b,a);assert.equal(c.MACHINES[worker].v.mission,null);
 b.demande='labour';lancer(c,b);assert(b.enginTerre>=0);
});
console.log(n+' automation tests passed.');
