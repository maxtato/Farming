const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict'),path=require('node:path');
const source=fs.readFileSync(path.join(__dirname,'../../index.html'),'utf8');
function fn(name){const a=source.indexOf('function '+name+'(');assert(a>=0,name);return source.slice(a,source.indexOf('\n}',a)+2);}
function setup(){
 const c=vm.createContext({Math,MACHINES:[],TOOLS:[],CHANTIERS:[],CONTRATS:[],missionVisible:()=>null,chLot:[],planTaches:[],HALLE:{file:[]},cur:-1,MODE_LIBRE:false,CAMPAGNE:{tuto:10},TUTO_TERRE:5,
 CROPS:[{cle:'ble',nom:'Blé'},{cle:'mais',nom:'Maïs'},{cle:'avoine',nom:'Avoine'}],CROP_DE:{ble:0,mais:1,avoine:2},PARCELS:[{x:10,z:0},{x:30,z:0},{x:50,z:0}],
 CUVES:{graines:{ble:100,mais:100,avoine:100},engrais:100,max:1000},ET_LABOUR:'labour',ET_SEMIS:'semis',ET_ENGRAIS:'engrais',ET_MOISSON:'moisson',ET_FINI:'fini',ET_POUSSE:'pousse',
 NOM_ETAPE:{labour:'Labour',semis:'Semis',engrais:'Engrais',moisson:'Moisson'},
 EST_TRACTEUR:m=>m.key.startsWith('t'),cuveDe:(t,k)=>t.cuves[k]||0,siloPlein:()=>false,showHint(){},
 bacsDe:t=>t.seme?[{cuve:t,engrais:false,clef:['ble','mais','avoine'][t.crop||0],par:.1}]:[],aServi:(c,i)=>i,etapeChantier:c=>c.demande,etapeMarchandise:()=>null,
 grainesPlace:()=>Math.max(0,c.CUVES.max-Object.values(c.CUVES.graines).reduce((a,b)=>a+b,0)),
 toolOf:m=>m.v.tool,RES_GRAINE:{quai:{x:100,z:0},r:4},RES_ENGRAIS:{quai:{x:120,z:0},r:4},
 pointSortie:()=>null,hitchDe:()=>4,VIT_PIVOT:2,viser:()=>[0,1],
 suivreRoute:(v,x,z)=>Math.hypot(v.pos.x-x,v.pos.z-z)>1?[0,1]:null,quitterLieu(){},solderLecon(){},refreshCropButton(){},
 verifierObjectifsChantier:()=>false,pisteAuge(){},pisteProduits(){},pisteMarchandise(){},
 caisseDe:m=>m.v.cargo,accepteNature:(k,cle)=>!k.prend||k.prend.includes(cle),rentrerAuParc(){}});
 vm.runInContext(['objectifAutomatique','objectifsAutomatiques'].map(fn).join('\n'),c);
 const a=source.indexOf('const classeDe ='),b=source.indexOf('/* UN ENGIN EST LIBRE',a);
 const d=source.indexOf('const rentreAuParc ='),e=source.indexOf('/* ARMER UN ENGIN',d);
 vm.runInContext(source.slice(a,b)+source.slice(d,e)+['cuveCleDe','placeCuve','poserDansCuve','viderCuve','remplirCuve','dansLaCuve','autresSemences','blocageRotation','interrompreRavitaillement','ravitaillerOutil','ravitaillementChamp','repartirChantiers','combinePret','besoinEtape','blocageEtape','enginLePlusProche','outilReserve','enginPourOutil','armerEngin','tachesEtape','pisteTerre','armerPorteur','retirerChantiersTermines'].map(fn).join('\n'),c);
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
 assert.notEqual(a.enginTerre,b.enginTerre);
 assert.equal(c.MACHINES[a.enginTerre].v.mission.taches.at(-1).crop,0);
 assert.equal(c.MACHINES[b.enginTerre].v.mission.taches.at(-1).crop,1);
 assert.equal(c.TOOLS[1].crop,undefined,'The seed selection changes at the tank, not remotely');
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
test('Two tractors share three continuous crops without starving the waiting parcel',c=>{
 c.MACHINES[1].verrou=true;
 const jobs=['ble','mais','avoine'].map((_,p)=>{const C=chantier(c,p,'semis');C.crop=p;return C;});
 const served=[0,0,0];
 for(let cycle=0;cycle<6;cycle++){
  c.repartirChantiers(.5);
  const active=jobs.filter(C=>C.enginTerre>=0);
  assert.equal(active.length,2);
  assert.equal(new Set(active.map(C=>C.enginTerre)).size,2);
  for(const C of active){
   served[C.p]++;const m=c.MACHINES[C.enginTerre],tasks=m.v.mission.taches;
   assert.equal(tasks.at(-1).crop,C.crop);assert(tasks.some(t=>t.quoi==='reserve'&&t.crop===C.crop));
   m.v.auto=false;m.v.mission=null;
  }
 }
 assert(served.every(n=>n>=3),served.join(','));
});
test('All finished workers are released before a waiting parcel chooses its implement',c=>{
 c.TOOLS[3].verrou=true;
 const waiting=chantier(c,0),done=chantier(c,1,'pousse');
 done.enginTerre=0;c.TOOLS[0].attached=c.MACHINES[0].v;
 c.repartirChantiers(.5);assert.equal(waiting.enginTerre,0);assert.equal(done.enginTerre,-1);
});
test('Transport is assigned after every parcel has had a chance to use a tractor',c=>{
 const a=chantier(c,0,'pousse'),b=chantier(c,1,'semis');
 c.pisteMarchandise=C=>{if(C===a)assert(b.enginTerre>=0);};
 c.repartirChantiers(.5);
});
function seeder(c){
 const m=c.MACHINES[0],T=c.TOOLS[1];T.cuveMax=50;T.crop=0;T.attached=m.v;m.v.tool=T;m.v.speed=0;
 c.armerEngin(m,[{quoi:'reserve',nat:'graine',crop:1}]);return {m,T};
}
test('Seed change drives to the tank before changing or returning any seed',c=>{
 const {m,T}=seeder(c);T.cuves={ble:20,mais:50,engrais:10};const task=m.v.mission.taches[0];
 assert(c.ravitaillerOutil(m,task,.1));assert.equal(T.crop,0);assert.equal(T.cuves.ble,20);
 m.v.pos.x=100;m.v.speed=2;assert(c.ravitaillerOutil(m,task,.1));assert.equal(T.crop,0);
 m.v.speed=0;assert.equal(c.ravitaillerOutil(m,task,.1),null);
 assert.equal(T.crop,1);assert.equal(T.cuves.ble,undefined);assert.equal(T.cuves.mais,50);
 assert.equal(T.cuves.engrais,10);assert.equal(c.CUVES.graines.ble,120);
});
test('A full farm tank can exchange seed without losing stock',c=>{
 const {m,T}=seeder(c);c.CUVES.max=300;T.cuves={ble:20};m.v.pos.x=100;
 const total=()=>Object.values(c.CUVES.graines).reduce((a,b)=>a+b,0)+Object.values(T.cuves).reduce((a,b)=>a+b,0);
 const before=total();assert.equal(c.blocageRotation(T,'mais'),null);
 c.ravitaillerOutil(m,m.v.mission.taches[0],.1);assert.equal(T.crop,1);assert.equal(T.cuves.ble,undefined);assert.equal(total(),before);
});
test('Insufficient return space blocks clearly and keeps every seed',c=>{
 const {m,T}=seeder(c);c.CUVES.max=300;T.cuves={ble:40,mais:50};m.v.pos.x=100;
 assert.match(c.blocageRotation(T,'mais'),/PLEINE/);
 c.ravitaillerOutil(m,m.v.mission.taches[0],.1);
 assert.equal(T.cuves.ble,40);assert.equal(T.cuves.mais,50);assert.equal(m.v.auto,false);
});
test('An empty seeder refills mid-pass and returns to the same unfinished route',c=>{
 const {m,T}=seeder(c);T.cuves={ble:.1};const task={quoi:'parcelle',p:0,crop:0,et:'semis'};
 c.armerEngin(m,[task]);const plan={p:c.PARCELS[0],i:7,pts:[{x:1,z:1}],entre:true};m.v.plan=plan;
 assert(c.ravitaillementChamp(m,task,.1));assert.equal(m.v.plan,null);assert.equal(m.v.repriseRavitaillement,plan);
 assert.equal(T.cuves.ble,.1);m.v.pos.x=100;
 c.ravitaillementChamp(m,task,.1);assert.equal(T.cuves.ble,50);assert.equal(m.v.plan,plan);
 assert.equal(plan.i,7);assert.equal(plan.entre,false);assert.equal(plan.reprise.x,0);
 assert.equal(c.ravitaillementChamp(m,task,.1),null);
});
test('An empty farm reserve releases the tractor and resumes after restocking',c=>{
 const {m,T}=seeder(c);T.cuves={};c.CUVES.graines.ble=0;const task={quoi:'parcelle',p:0,crop:0,et:'semis'};
 c.armerEngin(m,[task]);c.ravitaillementChamp(m,task,.1);assert.equal(m.v.auto,false);assert.equal(m.v.mission,null);
 const C=chantier(c,0,'semis');c.TOOLS[3].verrou=true;lancer(c,C);assert.match(C.bloque,/SEMENCE/);
 c.CUVES.graines.ble=50;lancer(c,C);assert.equal(C.enginTerre,0);
});
test('A combined seeder fertilizes with an empty seed compartment',c=>{
 const {m,T}=seeder(c);T.key='combine';T.cuves={engrais:10};T.fertilise=true;
 c.bacsDe=t=>[{cuve:t,clef:'ble',par:.1},{cuve:t,engrais:true,option:true,par:.1}];
 const task={quoi:'parcelle',p:0,crop:0,et:'engrais'};
 assert.equal(c.ravitaillementChamp(m,task,.1),null);
 T.cuves.engrais=0;assert(c.ravitaillementChamp(m,task,.1));assert.equal(m.v.mission.reserveChamp.nat,'engrais');
});
test('Refilling leaves by a clear field edge before using the road grid',c=>{
 const {m,T}=seeder(c);T.cuves={};m.v.vmax=10;
 const task={quoi:'parcelle',p:0,crop:0,et:'semis'};c.armerEngin(m,[task]);
 m.v.plan={p:c.PARCELS[0],entre:true,pts:[],i:0};c.pointSortie=()=>({x:12,z:0});
 let routes=0;c.suivreRoute=()=>{routes++;return [0,1];};
 c.ravitaillementChamp(m,task,.1);assert.equal(routes,0);assert.equal(T.cuves.ble,undefined);
 m.v.pos.x=12;c.ravitaillementChamp(m,task,.1);assert.equal(routes,1);
});
test('An entrance blocked by a wall uses another visible access to the road',c=>{
 c.obstacles=[];c.boxObs=[{x:5,z:0,hw:1,hd:2}];c.GRILLE_V=[-10,10];c.GRILLE_H=[-10,10];
 c.PARCELS=[{owned:true,x:0,z:0,w:12,h:12}];c.voieDirecteChamp=()=>true;
 c.itineraire=(x,z,bx,bz)=>x===0&&z===0?[{x:10,z:0},{x:bx,z:bz}]:[{x,z:10},{x:bx,z:10},{x:bx,z:bz}];
 vm.runInContext(['voieLibre','itineraireReserve'].map(fn).join('\n'),c);
 const route=c.itineraireReserve(0,0,30,30);let x=0,z=0;
 for(const q of route){assert(c.voieLibre(x,z,q.x,q.z));x=q.x;z=q.z;}
 assert.equal(x,30);assert.equal(z,30);
});
test('A harvest change unloads even a tiny remainder at the silo before taking another crop',c=>{
 c.pasDeRecul=()=>null;c.desarmerRecul=()=>{};c.HOP_MAX=100;c.VIDE_TREMIE=.5;c.hopper=.3;
 c.SILO={x:200,z:0};c.changeDeCulture=()=>c.hopper>.01;c.siloRefuse=()=>false;c.planAuto=()=>null;
 vm.runInContext(fn('missionDrive')+fn('tacheSuivante'),c);
 const m={key:'moisson',nom:'Moissonneuse',v:{pos:{x:0,z:0},speed:0,tool:null}};
 c.armerEngin(m,[{quoi:'parcelle',p:1,crop:1,et:'moisson'}]);
 assert(c.missionDrive(m,.1));assert.equal(m.v.goSilo,true);assert.equal(c.hopper,.3);
 m.v.pos.x=200;c.missionDrive(m,.1);assert(m.v.mission,'Wait for the actual unload');assert.equal(m.v.sensVoulu,'vider');
 c.hopper=0;c.missionDrive(m,.1);assert.equal(m.v.goSilo,false);assert.equal(m.v.mission,null);
});
test('Fertilizer-only work does not wait for seeds or request a seed refill',c=>{
 const C=chantier(c,0,'engrais');c.CUVES.graines.ble=0;
 c.bacsDe=t=>[{cuve:t,clef:'ble',par:.1},{cuve:t,engrais:true,option:true,par:.1}];
 assert.equal(c.blocageEtape(C,'engrais',{classe:'tracteur',outil:3}),null);
 const tasks=c.tachesEtape(C,'engrais',{classe:'tracteur',outil:3});
 assert(!tasks.some(t=>t.nat==='graine'));assert(tasks.some(t=>t.nat==='engrais'));
});
console.log(n+' automation tests passed.');
