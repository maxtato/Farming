const fs=require('fs'),path=require('path'),vm=require('vm'),assert=require('assert/strict');
const source=fs.readFileSync(path.join(__dirname,'../../index.html'),'utf8');
function fn(name){const start=source.indexOf('function '+name+'(');assert(start>=0,name);return source.slice(start,source.indexOf('\n}',start)+2);}
function table(name,end){const start=source.indexOf('const '+name+' = ');assert(start>=0,name);return source.slice(start,source.indexOf(end,start)+end.length).replace('const ','var ');}
function constant(name,end=';'){const start=source.indexOf('const '+name+' ');assert(start>=0,name);return source.slice(start,source.indexOf(end,start)+end.length).replace('const ','var ');}
function load(c,names){for(const name of names)vm.runInContext(fn(name),c,{filename:name+'.js'});}
const clone=x=>JSON.parse(JSON.stringify(x));
let tests=0;function test(name,f){f();tests++;console.log('PASS',name);}
function context(){
 let seed=83731;const math=Object.create(Math);math.random=()=>((seed=Math.imul(seed,1664525)+1013904223>>>0)/4294967296);
 const c=vm.createContext({Math:math,console,Number,Set,Infinity,mondePret:true,MODE_LIBRE:false,TOUT_OUVERT:false,
  CAMPAGNE:{mission:37,prise:false,faits:[],xp:100000,niveau:20,clientsPresentes:[]},SITES_ANNONCE:[],CONTRATS:[],SITES:[],MACHINES:[],TOOLS:[],CROPS:[],PATURES:[],PARCELS:[{owned:true,cellules:1000}],
  ESPECES:{},ESP_CLES:[],ATELIER_MODULES:[],siloStock:{},HALLE:{stock:{},modules:[]},DEPOT_BOIS:{stock:0,quai:{x:1,z:2}},QUAI_PECHE:{stock:{}},
  PORT:{charge:{x:3,z:4},debarque:{x:5,z:6},chantierQuai:{x:7,z:8},spots:[{x:9,z:10,cle:'poisson'},{x:12,z:14,cle:'crustaces'}]},FORET:{x0:10,x1:30,z0:40,z1:60},
  offreT:8,CONTRAT_MAX:4,OFFRE_MAX:3,RENOM_MIN:-6,RENOM_MAX:10,OFFRE_ATTENTE:55,OFFRE_VIE:180,ECH_PRIX:4,money:0,STAT:{ventes:0},ELEVAGE:{debit:40},hopper:100,delivered:0,
  TREMIE_SITE_MAX:335,bravoPages:[],contratVu:null,contratEl:{style:{}},telDecroche:-1,LECONS:[],leconsDites:[],leconActive:null,
  MISSIONS_REECRITS:[8,9],TUTO_INSERE:4,TUTO_INSERE3:5,TUTO_INSERE4:6,TUTO_INSERE4B:7,NIVEAUX:Array(20).fill({}),SITES_ANCIENS_NOMS:{},
  gagnerXp:()=>{},pluiePieces:()=>{},showHint:()=>{},rafraichirEcran:()=>{},annoncerFenetre:()=>{},solderLecon:()=>{},gainContinu:()=>{},compter:()=>{},puff:()=>{},viderType:()=>{},siSouvent:()=>false,
  relacherCommandes:()=>{},rendreContrat:()=>{},eur:n=>n+' €',nomDe:k=>k,nomHaut:k=>k.toUpperCase(),teinteDe:()=>0,
  niveauPourXp:()=>20,etapeTuto:()=>null,missionAPrendre:()=>null,etapeAvantMission:()=>null,
  ouvert:()=>true,siteOuvert:s=>!!s&&!s.verrou,EST_TRACTEUR:m=>m.key==='tracteur',outilVerrou:()=>false,
  toolOf:m=>m.v.tool||null,caisseDe:m=>m.v.tool||m.v.cargo||null,chargeDe:(t,k)=>t?.lots?.[k]||0,entrepotStock:()=>0,halleStock:()=>0,
  accepteNature:(t,k)=>(!t.prend||t.prend.includes(k))&&(!t.refuse||!t.refuse.includes(k)),
  retirerCharge:(t,k,q)=>{t.lots[k]-=q;t.load-=q;},siloMax:()=>1000,siloTotal:()=>0,
 });
 vm.runInContext(table('PRODUITS','\n};'),c);
 vm.runInContext(constant('SENS_VIDER'),c);
 vm.runInContext('var fournissable=k=>!PRODUITS[k].interne;var recetteEntrees=k=>typeof PRODUITS[k].de===\'string\'?{[PRODUITS[k].de]:1}:PRODUITS[k].de;',c);
 for(const name of ['parKgDe','enUnites','u2kg','prixUnite'])vm.runInContext(constant(name),c);
 c.prixDe=k=>c.PRODUITS[k].brut||c.PRODUITS[k].tarif||10;c.prime=k=>c.prixDe(k)*2;
 vm.runInContext(table('MISSIONS','\n];'),c);vm.runInContext(table('NEGOCE','\n};'),c);
 c.SITES=Object.entries(c.NEGOCE).map(([nom,n])=>({...n,nom,dropX:1,dropZ:2,offre:null,offreT:0,renom:0,reste:{},tremie:{},stock:{},achete:n.achete||[],accepte:[...new Set((n.fabrique||[]).flatMap(k=>Object.keys(c.recetteEntrees(k))))]}));
 c.SITES.push({nom:'Garage',dropX:70,dropZ:80,achete:[],accepte:[],tremie:{},reste:{},offreT:0});
 c.atelierA=k=>c.HALLE.modules.includes(k);c.terreCultivable=()=>c.PARCELS.reduce((n,p)=>n+(p.owned&&!p.pature?p.cellules:0),0);
 c.encaisser=q=>{c.money+=q;};c.prixChez=()=>2;
 for(const name of ['campagneFinie','contratsOuverts','commandesObligatoires','venteLibreOuverte','pasCommande','coefRenom','attenteRenom','offresEnCours','contratChez'])vm.runInContext(constant(name),c);
 vm.runInContext(constant('placeChez','\n};'),c);
 vm.runInContext(source.split('\n').find(l=>l.startsWith('const totalTremieSite =')).replace('const ','var '),c);
 return c;
}
// Use complete declarations for arrow functions containing internal semicolons.
function ready(){
 const c=context();
 load(c,['lectureEnCours','quantitePreparation','limiteActionAutomatique','resteObjectifAutomatique','spotPecheProche']);
 load(c,['produitsOuverts','capaciteFerme','tirerLigne','tirerCommande','stockFermeCommande','transportCommande','avanceChez','resteCommande','resteContrat','livraison','solderContrat','poserOffre','accepterOffre','refuserOffre','libelleRenom','remplirCommandes','chargerCampagne','quantiteMax','executer','entamerEtal','objectifNature','testerFaire','demandeTelephone','ouvrirContrat','capaciteBetail','updateBetail']);
 c.missionVisible=()=>!c.MODE_LIBRE&&c.CAMPAGNE.prise?c.MISSIONS[c.CAMPAGNE.mission]||null:null;
 return c;
}
const cargo=(cles,lots={})=>({prend:cles,lots,load:Object.values(lots).reduce((a,b)=>a+b,0),capacite:1000,cargo:true});
const machine=(key,C,extra={})=>({key,verrou:false,v:{cargo:C},...extra});
function equipped(c){
 c.CROPS=['ble','orge','avoine','mais','colza','raisin','olives'].map(cle=>({cle,kg:1,perenne:['raisin','olives'].includes(cle)}));
 c.MACHINES=[machine('moisson'),machine('enjambeuse'),machine('abatteuse',cargo(['grumes'])),machine('porteur',cargo(['grumes'])),machine('frigo',cargo(['poisson','crustaces'])),machine('fourgon',cargo(Object.keys(c.PRODUITS))),machine('barque',cargo(['poisson']),{bateau:true,peche:{cle:'poisson',lot:10,duree:8}}),machine('caseyeur',cargo(['crustaces']),{bateau:true,peche:{cle:'crustaces',lot:8,duree:8}})];
 c.ESPECES={vache:{produit:'lait',parSec:.4},brebis:{produit:'laine',parSec:.2,second:{cle:'laitBrebis',parSec:.2}},poule:{produit:'oeufs',parSec:.05},abeille:{produit:'miel',parSec:.03}};
 c.ESP_CLES=Object.keys(c.ESPECES);c.PATURES=c.ESP_CLES.map(espece=>({espece,produit:10,produit2:10,betes:[{},{}]}));
 c.HALLE.modules=['farine','huile','huileOlive','vin','biere','fromage','fromageBrebis'];c.ATELIER_MODULES=c.HALLE.modules.map(cle=>({cle}));return c;
}
const order=(site,cle='ble',need=10,fait=0)=>({lieu:site.nom,type:'combinee',prime:50,xp:10,temps:0,lignes:[{cle,need,fait}]});
if(require.main===module){
test('Seven new missions preserve the thirty existing ranks and cover every new character',()=>{
 const c=ready();assert.equal(c.MISSIONS.length,37);assert.equal(c.MISSIONS[29].lieu,'Restaurant');
 assert.deepEqual(Array.from(c.MISSIONS.slice(30),m=>m.lieu||m.qui),['Scierie','Menuisier','Comptoir des pêcheurs','Criée','Poissonnerie','Conserverie',"Entrepôt d'export"]);
 for(const m of c.MISSIONS.slice(30)){if(m.faire)continue;const s=c.SITES.find(s=>s.nom===m.lieu);assert(m.lignes.length>=2);for(const l of m.lignes)assert(s.achete.includes(l.cle)||s.accepte.includes(l.cle));}
 assert(c.MISSIONS.at(-1).apres[0].txt.includes('téléphone'));assert(!c.MISSIONS[29].apres[0].txt.includes('terminée'));
});
test('Boat mission requires two fishing capabilities and refrigerated road delivery',()=>{const c=equipped(ready());assert(c.testerFaire('flotte'));for(const key of ['frigo','caseyeur']){const m=c.MACHINES.find(m=>m.key===key);m.verrou=true;assert(!c.testerFaire('flotte'));m.verrou=false;}});
test('5000 generated orders vary customers and quantities, with compatible unique and achievable products',()=>{
 const c=equipped(ready()),clients=new Set(),volumes=new Set();
 for(let i=0;i<5000;i++){const o=c.tirerCommande();assert(o);clients.add(o.lieu);const site=c.SITES.find(s=>s.nom===o.lieu);assert(o.lignes.length<=4);assert.equal(new Set(o.lignes.map(l=>l.cle)).size,o.lignes.length);assert.equal(o.temps,0);
  for(const l of o.lignes){assert(site.achete.includes(l.cle)||site.accepte.includes(l.cle));assert(l.need>0);assert(l.need<=c.capaciteFerme(l.cle)*.55+1e-8);assert(Math.abs(c.enUnites(l.cle,l.need)-Math.round(c.enUnites(l.cle,l.need)))<1e-7);volumes.add(l.cle+':'+l.need);}
  if(['Scierie','Menuisier','Conserverie','Criée','Poissonnerie'].includes(o.lieu))assert(o.lignes.length>=2);
 }
 for(const site of ['Scierie','Menuisier','Conserverie','Criée','Poissonnerie',"Entrepôt d'export"])assert(clients.has(site),site);assert(clients.size>=15);assert(volumes.size>80);
});
test('Accepted and pending quantities reserve capacity across clients',()=>{const c=equipped(ready());for(const s of c.SITES){s.offreT=100;}const s=c.SITES.find(s=>s.nom==='Coopérative');s.offreT=0;for(const k of c.produitsOuverts()){c.CONTRATS.push({lieu:'Elsewhere',lignes:[{cle:k,need:c.capaciteFerme(k)*.55,fait:0}]});}assert.equal(c.tirerCommande(),null);c.CONTRATS.length=0;const r=c.SITES.find(s=>s.nom==='Restaurant');r.offre={lignes:c.produitsOuverts().map(cle=>({cle,need:c.capaciteFerme(cle)*.55,fait:0}))};assert.equal(c.tirerCommande(),null);});
test('No random order needs unowned transport, boats or crop harvesting machinery',()=>{const c=equipped(ready());for(const m of c.MACHINES)m.verrou=true;assert.equal(c.tirerCommande(),null);assert.equal(c.capaciteFerme('ble'),0);assert.equal(c.capaciteFerme('poisson'),0);assert.equal(c.transportCommande('grumes'),false);c.MACHINES.find(m=>m.key==='abatteuse').verrou=false;assert.equal(c.transportCommande('grumes'),false);c.MACHINES.find(m=>m.key==='barque').verrou=false;assert.equal(c.transportCommande('poisson'),false);});
test('A detached trailer is usable only with an owned compatible tractor',()=>{const c=ready();c.TOOLS=[cargo(['grumes'])];assert(!c.transportCommande('grumes'));c.MACHINES=[machine('tracteur')];assert(c.transportCommande('grumes'));c.TOOLS[0].pourEngin='semi';assert(!c.transportCommande('grumes'));c.MACHINES.push(machine('semi'));assert(c.transportCommande('grumes'));});
test('Stock accounting includes wood depot, quay and cargo without counting attached trailers twice',()=>{const c=ready(),t=cargo(['grumes'],{grumes:30});c.siloStock.grumes=10;c.DEPOT_BOIS.stock=20;c.TOOLS=[t];c.MACHINES=[{verrou:false,v:{tool:t}}];assert.equal(c.stockFermeCommande('grumes'),60);c.QUAI_PECHE.stock.poisson=12;assert.equal(c.stockFermeCommande('poisson'),12);});
test('Tiny egg capacity rounds in eggs and never exceeds its ceiling',()=>{const c=ready();c.capaciteFerme=()=>.18;const l=c.tirerLigne('oeufs',100,0);assert.equal(c.enUnites('oeufs',l.need),1);assert(l.need<=.18*.55);c.capaciteFerme=()=>.05;assert.equal(c.tirerLigne('oeufs',100,0).need,0);});
for(const sens of ['vendre','verser','tremieVente','tremieLivraison'])test(sens+': stale manual/autopilot action stops exactly at requested amount',()=>{
 const c=ready(),s=c.SITES.find(s=>s.nom==='Coopérative'),m=machine('fourgon',cargo(['ble'],{ble:100})),o=order(s,'ble',10,7);c.CONTRATS.push(o);const a={sens,S:s,cle:'ble',commande:false};assert.equal(c.quantiteMax(m,a),3);for(let i=0;i<10;i++)c.executer(m,a,1);assert.equal(c.STAT.ventes,3);assert.equal(c.money,56);assert.equal(c.CONTRATS.length,0);assert.equal(c.quantiteMax(m,a),0);assert.equal(sens.startsWith('tremie')?c.hopper:m.v.cargo.load,97);
});
test('An unanswered offer never authorizes unloading',()=>{const c=ready(),s=c.SITES[0],m=machine('fourgon',cargo(['ble'],{ble:100}));s.offre=order(s);for(const sens of ['vendre','verser','tremieVente','tremieLivraison']){const a={sens,S:s,cle:'ble'};assert.equal(c.quantiteMax(m,a),0);c.executer(m,a,1);}assert.equal(c.money,0);assert.equal(m.v.cargo.load,100);assert.equal(c.hopper,100);});
test('A multi-product contract pays its bonus once, after its last product',()=>{const c=ready(),s=c.SITES[0],o=order(s);o.lignes.push({cle:'orge',need:5,fait:0});c.CONTRATS.push(o);c.livraison(s.nom,'ble',100);assert.equal(c.money,0);assert.equal(c.CONTRATS.length,1);c.livraison(s.nom,'orge',5);assert.equal(c.money,50);c.livraison(s.nom,'orge',5);assert.equal(c.money,50);assert.equal(c.CONTRATS.length,0);assert(c.offreT<=37);});
test('One delivery cannot be counted twice against overlapping saved commitments',()=>{const c=ready(),s=c.SITES[0];c.CONTRATS.push(order(s),order(s));assert.equal(c.resteCommande(s.nom,'ble'),20);c.livraison(s.nom,'ble',12);assert.equal(c.CONTRATS.length,1);assert.equal(c.CONTRATS[0].lignes[0].fait,2);assert.equal(c.resteCommande(s.nom,'ble'),8);assert.equal(c.money,50);});
test('Free mode and campaign retain their existing selling economy',()=>{const c=ready(),s=c.SITES[0],m=machine('fourgon',cargo(['ble'],{ble:100}));c.MODE_LIBRE=true;assert(c.venteLibreOuverte());c.executer(m,{sens:'vendre',S:s,cle:'ble'},1);assert.equal(c.STAT.ventes,40);c.MODE_LIBRE=false;c.CAMPAGNE.mission=10;assert(c.venteLibreOuverte());c.executer(m,{sens:'vendre',S:s,cle:'ble'},1);assert.equal(c.STAT.ventes,80);c.CAMPAGNE.mission=0;assert(!c.venteLibreOuverte());});
test('Factory capacity is respected by both the displayed maximum and actual delivery',()=>{const c=ready(),s=c.SITES[0],m=machine('fourgon',cargo(['ble'],{ble:100}));s.tremie.orge=334;c.CONTRATS.push(order(s));const a={sens:'verser',S:s,cle:'ble'};assert.equal(c.quantiteMax(m,a),1);c.executer(m,a,1);assert.equal(c.totalTremieSite(s),335);assert.equal(c.CONTRATS[0].lignes[0].fait,1);});
test('Offers keep coming over simulated play time with bounded pending and active counts',()=>{const c=equipped(ready());let completed=0;for(let i=0;i<2500;i++){c.remplirCommandes(5);assert(c.offresEnCours()<=3);assert(c.CONTRATS.length<=4);for(const s of c.SITES)if(s.offre){assert(c.accepterOffre(s));const o=c.CONTRATS.find(o=>o.lieu===s.nom);for(const l of [...o.lignes])c.livraison(s.nom,l.cle,l.need);completed++;}}assert(completed>100);assert.equal(c.CONTRATS.length,0);});
test('Campaign suppresses new offers without deleting legacy accepted contracts',()=>{const c=equipped(ready()),s=c.SITES[0];c.CAMPAGNE.mission=30;c.CONTRATS.push(order(s));c.remplirCommandes(100);assert.equal(c.offresEnCours(),0);assert.equal(c.CONTRATS.length,1);assert(!c.poserOffre());c.MODE_LIBRE=true;c.remplirCommandes(0);assert.equal(c.CONTRATS.length,0);});
test('A full order book, pending limit and client cooldown prevent extra offers',()=>{const c=equipped(ready());for(let i=0;i<4;i++)c.CONTRATS.push(order(c.SITES[i]));assert(!c.poserOffre());c.CONTRATS.length=0;for(let i=0;i<3;i++)c.SITES[i].offre=order(c.SITES[i]);assert(!c.poserOffre());for(const s of c.SITES){s.offre=null;s.offreT=20;}assert.equal(c.tirerCommande(),null);});
test('Phone prioritizes unread calls; reading and accepting an offer do not duplicate it',()=>{const c=ready(),a=c.SITES[0],b=c.SITES[1];a.offre={...order(a),lu:true};b.offre=order(b);assert.equal(c.demandeTelephone(),b);c.ouvrirContrat(b.offre,b,true);assert(b.offre.lu);assert.equal(c.contratEl.style.display,'block');assert(c.accepterOffre(b));assert(!c.accepterOffre(b));assert.equal(c.CONTRATS.length,1);assert.equal(c.demandeTelephone(),null);c.contratVu=null;assert.equal(c.demandeTelephone(),a);});
test('Old completed campaign continues at the new chapter without replaying thirty missions',()=>{const c=ready();c.chargerCampagne({campagne:{mv:2,tv:4,xp:100000,niveau:20,mission:30,prise:true,faits:[999],contrats:[]}});assert.equal(c.CAMPAGNE.mission,30);assert.equal(c.CAMPAGNE.prise,false);assert.equal(c.CAMPAGNE.faits.length,0);assert.equal(c.offresEnCours(),0);});
test('Version two progress in an unchanged mission survives migration',()=>{const c=ready();c.chargerCampagne({campagne:{mv:2,tv:4,xp:1234,niveau:10,mission:8,prise:true,faits:[12]}});assert.equal(c.CAMPAGNE.mission,8);assert.equal(c.CAMPAGNE.prise,true);assert.equal(c.CAMPAGNE.faits[0],12);});
test('Post-campaign save restores accepted progress, calls, read state and cooldowns',()=>{const c=ready(),a=c.SITES[0],b=c.SITES.find(s=>s.nom==='Criée');const data={campagne:{mv:3,tv:4,xp:100000,niveau:20,mission:37,contrats:[order(a,'ble',10,4)],appels:[{lieu:b.nom,offre:{...order(b,'poisson',12),lu:true,attente:77}}],appelsT:44,delaisAppels:{[a.nom]:23}}};c.chargerCampagne(clone(data));assert.equal(c.CONTRATS[0].lignes[0].fait,4);assert.equal(b.offre.lignes[0].need,12);assert.equal(b.offre.attente,77);assert.equal(b.offre.lu,true);assert.equal(c.offreT,44);assert.equal(a.offreT,23);});
test('Corrupt, incompatible or already completed legacy orders do not occupy a slot forever',()=>{const c=ready(),s=c.SITES[0];c.chargerCampagne({campagne:{mv:3,tv:4,xp:100000,mission:37,contrats:[order(s,'poisson'),order(s,'ble',-1),order(s,'ble',10,400)]}});assert.equal(c.CONTRATS.length,0);});
test('Wood and fishing guidance uses reachable loading points and directs gear purchases',()=>{const c=ready(),s=c.SITES.find(s=>s.nom==='Scierie');assert.equal(c.objectifNature('grumes',10,s).lieu,'Garage');c.MACHINES.push(machine('porteur',cargo(['grumes'])));assert.equal(c.objectifNature('grumes',10,s).lieu,'Garage');c.MACHINES.push(machine('abatteuse'));assert.equal(c.objectifNature('grumes',10,s).lieu,'Forêt');c.DEPOT_BOIS.stock=10;assert.equal(c.objectifNature('grumes',10,s).x,c.DEPOT_BOIS.quai.x);c.MACHINES.push(machine('frigo',cargo(['poisson','crustaces'])));assert.equal(c.objectifNature('poisson',10,s).lieu,'Comptoir des pêcheurs');c.QUAI_PECHE.stock.poisson=10;assert.equal(c.objectifNature('poisson',10,s).x,c.PORT.charge.x);c.QUAI_PECHE.stock.poisson=0;c.MACHINES.push(machine('barque',cargo(['poisson'],{poisson:10}),{bateau:true,peche:{cle:'poisson'}}));assert.equal(c.objectifNature('poisson',10,s).z,c.PORT.debarque.z);});
test('Expired or declined calls release reservations so later offers remain possible',()=>{const c=equipped(ready()),s=c.SITES[0];c.veillerMission=()=>{};c.fermerContrat=()=>{c.contratVu=null;};load(c,['updateCommandes']);s.offre={...order(s),attente:1};c.offreT=50;c.updateCommandes(2);assert.equal(s.offre,null);assert(s.offreT>0);s.offre={...order(s),attente:100};assert(c.refuserOffre(s));assert.equal(s.offre,null);assert.equal(s.renom,0);assert(s.offreT>0);for(let i=0;i<50;i++)c.updateCommandes(5);assert(c.offresEnCours()>0);});
test('Every buying shop and factory can request at least two different farm products',()=>{const c=equipped(ready());for(const s of c.SITES){if(!s.achete.length&&!s.accepte.length)continue;assert(new Set([...s.achete,...s.accepte]).size>=2,s.nom);}});
test('Livestock orders reserve whole owned animals and use livestock-compatible transport',()=>{const c=ready();c.PATURES=[{espece:'cochon',betes:Array(6).fill({})}];c.MACHINES=[machine('frigo',cargo(['poisson']))];assert(!c.transportCommande('betail_cochon'));c.MACHINES.push(machine('pickup',cargo(['ble'])));assert(!c.transportCommande('betail_cochon'));c.MACHINES.push(machine('fourgon',cargo(['ble'])));assert(c.transportCommande('betail_cochon'));for(let i=0;i<30;i++){const l=c.tirerLigne('betail_cochon',1,0);assert(Number.isInteger(l.need));assert(l.need>=1&&l.need<=3);}assert.equal(c.tirerLigne('betail_cochon',10000,3).need,0);});
test('Butcher sells exactly the ordered animals and preserves others on board',()=>{const c=ready(),s=c.SITES.find(s=>s.nom==='Boucherie');Object.assign(c,{BOUCHERIE:s,PALIER:{FINI:2},aQuai:()=>true});const m=machine('fourgon');Object.assign(m.v,{betail:4,betailEspece:'cochon',betailPrix:820,speed:0});c.MACHINES=[m];c.STAT={betes:0,porcs:0};c.updateBetail(2);assert.equal(m.v.betail,4);assert.equal(c.money,0);c.CONTRATS.push(order(s,'betail_cochon',2));for(let i=0;i<8;i++)c.updateBetail(2);assert.equal(m.v.betail,2);assert.equal(c.STAT.porcs,2);assert.equal(c.money,3330);assert.equal(c.CONTRATS.length,0);c.MODE_LIBRE=true;c.updateBetail(2);assert.equal(m.v.betail,1);});
console.log(tests+' campaign and contract tests passed.');
}
module.exports={ready,load,constant,table,equipped,machine,cargo,order,source};
