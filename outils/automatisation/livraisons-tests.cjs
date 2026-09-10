const fs=require('fs'),vm=require('vm'),assert=require('assert/strict'),path=require('path');
const source=fs.readFileSync(path.join(__dirname,'../../index.html'),'utf8');
function fn(n){const a=source.indexOf('function '+n+'(');assert(a>=0,n);return source.slice(a,source.indexOf('\n}',a)+2);}
function setup(){
 const c=vm.createContext({console,Math,Date,Number,Set,Map,JSON,Infinity,CONTRATS:[],CAMPAGNE:{mission:3,faits:[]},M:null,
  MACHINES:[],CHANTIERS:[],PARCELS:[{owned:true},{owned:true,pature:true},{owned:false}],planEl:{style:{display:'none'}},messages:[],chLot:[],chContinu:false,
  FORET:{arbres:[{etat:0,x:10,z:10}]},DEPOT_BOIS:{stock:80},QUAI_PECHE:{stock:{poisson:50,crustaces:30}},
  SITES:[{nom:'Scierie',achete:['grumes'],accepte:[]},{nom:'Criée',achete:['poisson','crustaces'],accepte:[]}],
  armerEngin(m,t){m.v.auto=true;m.v.mission={taches:t,i:0,etape:0};},arreterMission(m){m.v.auto=false;m.v.mission=null;},
  enginLibre:m=>!m.verrou&&!m.v.mission&&!m.v.auto,caisseDe:m=>m.v.cargo,chargeDe:(K,k)=>K.lots[k]||0,
  accepteNature:(K,k)=>!K.prend||K.prend.includes(k),nomDe:k=>k,modeDe:A=>A.sens==='vendre'?'vider':'remplir',
  lieuPrend:n=>c.SITES.find(S=>S.nom===n)?.achete||[],lieuPoint:n=>({x:0,z:0,cle:n}),demandeChez:()=>true,
  quantiteAuLieu:(a,k)=>a==='depotBois'?c.DEPOT_BOIS.stock:c.QUAI_PECHE.stock[k]||0,
  chantierDe:i=>c.CHANTIERS.find(C=>C.p===i),retirerChantier:i=>{c.CHANTIERS.splice(c.CHANTIERS.findIndex(C=>C.p===i),1);},
 });
 c.missionVisible=()=>c.M;c.showHint=t=>c.messages.push(t);
 for(const key of ['abatteuse','barque','caseyeur','frigo','porteur'])c.MACHINES.push({key,nom:key,verrou:false,peche:['barque','caseyeur'].includes(key)?{cle:key==='caseyeur'?'crustaces':'poisson'}:null,v:{auto:false,mission:null,cargo:{load:0,capacite:100,lots:{},prend:key==='frigo'?['poisson','crustaces']:['grumes']}}});
 vm.runInContext(source.slice(source.indexOf('function objectifAutomatique('),source.indexOf('function natureLibre('))+'\nthis.jobs=NATURE_JOBS;',c);
 vm.runInContext(['parcelleDisponible','choisirCategorie'].map(fn).join('\n')+'\nvar planCategorie=null,planNatureDest=null,planTaches=[];',c);
 c.armerPorteur=(J,champ,ou,faire)=>{const t=faire();const m=c.MACHINES.find(m=>['frigo','porteur'].includes(m.key)&&c.enginLibre(m)&&c.accepteNature(m.v.cargo,t[0].cle));if(!m)return false;J[champ]=c.MACHINES.indexOf(m);c.armerEngin(m,t);return true;};
 return c;
}
let n=0;function test(name,f){f(setup());n++;console.log('PASS '+name);}
function commande(c,lieu='Criée',cle='poisson',need=50){const C={lieu,lignes:[{cle,need,fait:0}]};c.CONTRATS.push(C);return C;}
test('An unaccepted shop request cannot start a nature delivery',c=>{assert.equal(c.poserNature('barque',true,{dest:'Criée'}),null);assert.equal(c.jobs.length,0);});
test('Campaign objectives bind only the current accepted mission',c=>{c.M={lieu:'Criée',lignes:[{cle:'poisson',need:60}]};c.CAMPAGNE.faits=[10];const O=c.objectifAutomatique('Criée','poisson');assert.equal(c.resteObjectifAutomatique(O),50);c.CAMPAGNE.mission++;assert.equal(c.resteObjectifAutomatique(O),0);});
test('A completed contract never reconnects to a later identical order',c=>{commande(c);const O=c.objectifAutomatique('Criée','poisson');c.CONTRATS.length=0;commande(c);assert.equal(c.resteObjectifAutomatique(O),0);});
test('Two accepted commitments are both counted, but other products are excluded',c=>{commande(c);commande(c,'Criée','poisson',20);commande(c,'Criée','crustaces',90);assert.equal(c.resteObjectifAutomatique(c.objectifAutomatique('Criée','poisson')),70);});
test('A delivery uses a compatible road vehicle and leaves its producer active',c=>{commande(c);const J=c.poserNature('barque',true,{dest:'Criée'});c.majLivraisonsNature();assert.equal(J.enginPort,3);assert(c.MACHINES[1].v.auto);assert.equal(c.MACHINES[3].v.mission.taches[0].a,'quaiPeche');});
test('Wood and fishing deliveries run in parallel without sharing a worker',c=>{commande(c);commande(c,'Scierie','grumes');c.poserNature('barque',true,{dest:'Criée'});c.poserNature('abatteuse',true,{dest:'Scierie'});c.majLivraisonsNature();assert.deepEqual(c.jobs.map(J=>J.enginPort).join(','),'3,4');});
test('Cancelling a boat also cancels its delivery, leaving the forestry team running',c=>{commande(c);commande(c,'Scierie','grumes');c.poserNature('barque',true,{dest:'Criée'});c.poserNature('abatteuse',true,{dest:'Scierie'});c.majLivraisonsNature();c.retirerNature('barque');assert(!c.MACHINES[3].v.auto);assert(c.MACHINES[4].v.auto);assert(c.MACHINES[0].v.auto);});
test('A stale delivery index never cancels a reassigned vehicle',c=>{commande(c);const J=c.poserNature('barque',true,{dest:'Criée'});J.enginPort=3;c.armerEngin(c.MACHINES[3],[{quoi:'navette',nature:'caseyeur'}]);c.retirerNature('barque');assert(c.MACHINES[3].v.auto);});
test('A manually fulfilled demand stops continuous production and delivery with one notice',c=>{const C=commande(c);c.poserNature('barque',true,{dest:'Criée'});c.majLivraisonsNature();C.lignes[0].fait=50;c.majLivraisonsNature();c.majLivraisonsNature();assert.equal(c.jobs.length,0);assert(!c.MACHINES[1].v.auto);assert(!c.MACHINES[3].v.auto);assert.equal(c.messages.filter(t=>t.includes('AUTOMATISATION ARRÊTÉE')).length,1);});
test('A full commerce pauses delivery without declaring the contract fulfilled',c=>{commande(c);const J=c.poserNature('barque',true,{dest:'Criée'});c.demandeChez=()=>false;c.majLivraisonsNature();assert.equal(c.jobs.length,1);assert.equal(J.enginPort,-1);assert.match(J.livraison,/plein/);});
test('An unavailable compatible transporter leaves an explicit waiting state',c=>{commande(c);c.MACHINES[3].verrou=true;const J=c.poserNature('barque',true,{dest:'Criée'});c.majLivraisonsNature();assert.match(J.livraison,/indisponible/);assert.equal(J.enginPort,-1);});
test('One-off production remains visible until its last load is delivered',c=>{commande(c);const J=c.poserNature('barque',false,{dest:'Criée'});c.finirProductionNature(J);assert(J.productionFinie);c.majLivraisonsNature();assert.equal(c.jobs.length,1);assert.equal(J.enginPort,3);});
test('Saving and resuming retains the destination, quota identity and loaded transporter',c=>{commande(c);const J=c.poserNature('barque',false,{dest:'Criée'});c.majLivraisonsNature();c.MACHINES[3].v.cargo.lots.poisson=20;const S=JSON.parse(JSON.stringify(c.sauverNature()));c.chargerNature(S);const R=c.jobs[0];assert.equal(R.dest,'Criée');assert.equal(R.enginPort,3);assert.equal(c.MACHINES[3].v.mission.etape,1);assert.equal(c.resteObjectifAutomatique(R.objectif),50);});
test('Loading reserves cargo in other trucks and never loads beyond the current demand',c=>{commande(c);const O=c.objectifAutomatique('Criée','poisson');for(const m of c.MACHINES.slice(3))c.armerEngin(m,[{quoi:'navette',a:'quaiPeche',b:'Criée',cle:'poisson',objectif:O}]);c.MACHINES[3].v.cargo.lots.poisson=20;c.MACHINES[4].v.cargo.lots.poisson=10;assert.equal(c.limiteActionAutomatique(c.MACHINES[3],{sens:'prendrePeche',cle:'poisson'}),20);});
test('Unloading is limited to the exact product and requested destination',c=>{const C=commande(c);C.lignes[0].fait=49;const O=c.objectifAutomatique('Criée','poisson'),m=c.MACHINES[3];c.armerEngin(m,[{quoi:'navette',b:'Criée',cle:'poisson',objectif:O}]);m.v.mission.etape=1;assert.equal(c.limiteActionAutomatique(m,{sens:'vendre',cle:'poisson',S:{nom:'Criée'}}),1);assert.equal(c.limiteActionAutomatique(m,{sens:'vendre',cle:'poisson',S:{nom:'Poissonnerie'}}),0);});
test('Livestock keeps its other product running when one requested product is fulfilled',c=>{const C=commande(c,'Laiterie','lait',20);commande(c,'Scierie','laine',10);const J={p:1,dest:{lait:'Laiterie',laine:'Scierie'},enginPort:-1};J.objectifs=c.objectifsAutomatiques(J.dest);c.CHANTIERS.push(J);C.lignes[0].fait=20;assert.equal(c.verifierObjectifsChantier(J),false);assert.equal(J.dest.lait,undefined);assert.equal(J.dest.laine,'Scierie');c.CONTRATS.length=0;assert(c.verifierObjectifsChantier(J));});
test('Available parcel selection respects ownership, activity and existing workers',c=>{vm.runInContext("planCategorie='culture'",c);assert(c.parcelleDisponible(0));assert(!c.parcelleDisponible(1));assert(!c.parcelleDisponible(2));c.CHANTIERS.push({p:0});assert(!c.parcelleDisponible(0));vm.runInContext("planCategorie='elevage'",c);assert(c.parcelleDisponible(1));});
test('Real loading and unloading finish a 50 kg order exactly without fractional deadlock',()=>{
 const {ready,load,machine,cargo}=require('../contrats/tests.cjs'),c=ready();
 load(c,['objectifAutomatique','limiteActionAutomatique','resteObjectifAutomatique']);
 c.modeDe=A=>A.sens==='vendre'?'vider':'remplir';c.majPileDepot=()=>{};
 c.ajouterCharge=(K,k,q)=>{K.lots[k]=(K.lots[k]||0)+q;K.load+=q;};
 const S=c.SITES.find(S=>S.nom==='Scierie'),C={lieu:S.nom,lignes:[{cle:'grumes',need:50,fait:0},{cle:'planches',need:10,fait:0}],prime:0,xp:0};
 c.CONTRATS.push(C);const m=machine('porteur',cargo(['grumes']));c.MACHINES=[m];c.DEPOT_BOIS.stock=80;
 m.v.mission={i:0,etape:0,taches:[{quoi:'navette',a:'depotBois',b:S.nom,cle:'grumes',objectif:c.objectifAutomatique(S.nom,'grumes')}]};
 for(let i=0;i<100;i++)c.executer(m,{sens:'prendreBois',cle:'grumes'},.1);
 assert.equal(m.v.cargo.load,50);assert.equal(c.DEPOT_BOIS.stock,30);
 m.v.mission.etape=1;for(let i=0;i<100;i++)c.executer(m,{sens:'vendre',cle:'grumes',S},.1);
 assert.equal(C.lignes[0].fait,50);assert.equal(m.v.cargo.load,0);assert.equal(c.resteObjectifAutomatique(m.v.mission.taches[0].objectif),0);
});
console.log(n+' automation delivery tests passed.');
