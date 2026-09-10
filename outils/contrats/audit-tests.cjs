const assert=require('assert/strict');
const {ready,load,equipped,order,source}=require('./tests.cjs');
let count=0;function test(name,f){f();count++;console.log('PASS',name);}
function windows(){
 const c=ready(),els=new Map();const el=()=>({style:{},classList:{add(){},remove(){},toggle(){}},setAttribute(k,v){this[k]=v;},scrollTop:10});
 Object.assign(c,{bravoI:0,bravoT:0,bravoEl:el(),document:{getElementById(k){if(!els.has(k))els.set(k,el());return els.get(k);}},poserVisage(){}});
 load(c,['montrerBravo','fermerBravo','peindreBravo','suivantBravo','annoncerFenetre','updateCommandes']);c.veillerMission=()=>{};return c;
}
test('An informational page ignores its old duration and advances only on explicit next',()=>{
 const c=windows();c.annoncerFenetre({titre:'A',duree:.1});c.annoncerFenetre({titre:'B',duree:1});
 for(let i=0;i<100;i++)c.updateCommandes(10);
 assert.equal(c.bravoT,0);assert.equal(c.bravoI,0);assert.equal(c.document.getElementById('brtitre').textContent,'A');
 c.suivantBravo();assert.equal(c.document.getElementById('brtitre').textContent,'B');assert.equal(c.document.getElementById('brdefile').scrollTop,0);
 c.suivantBravo();assert.equal(c.bravoPages.length,0);assert.equal(c.bravoEl.style.display,'none');
 assert(!/bravoT\s*-=|bravoT\s*-\s*dt/.test(source));
 assert(source.includes("getElementById('brgo').addEventListener('click'"));
});
test('Reading freezes offer expiry, accepted deadlines and the next campaign call',()=>{
 const c=windows(),S=c.SITES[0];S.offre={...order(S),attente:50};c.CONTRATS.push({...order(c.SITES[1]),temps:60});c.CAMPAGNE.retard=30;c.offreT=20;
 c.annoncerFenetre({titre:'Bilan'});c.updateCommandes(300);
 assert.equal(S.offre.attente,50);assert.equal(c.CONTRATS[0].temps,60);assert.equal(c.CAMPAGNE.retard,30);assert.equal(c.offreT,20);
 c.suivantBravo();c.updateCommandes(1);assert.equal(S.offre.attente,49);assert.equal(c.CONTRATS[0].temps,59);
});
test('Unread pages survive campaign reload in their existing order',()=>{
 const c=windows();c.chargerCampagne({campagne:{mv:4,tv:4,xp:100000,mission:37,lectures:[{titre:'Reçu'},{titre:'Catalogue'}]}});
 assert.equal(c.document.getElementById('brtitre').textContent,'Reçu');c.suivantBravo();assert.equal(c.document.getElementById('brtitre').textContent,'Catalogue');
 assert(source.includes('lectures:bravoPages.slice(bravoI)'));
});
test('Premium preparation requires 184 kg without double counting its production and inventory',()=>{
 const c=ready();c.HALLE.modules=['alimentPlus'];c.STAT.alimentPlus=100;c.entrepotStock=()=>100;
 assert.equal(c.quantitePreparation(),100);assert(!c.testerFaire('alimentPlus'));c.STAT.alimentPlus=184;assert(c.testerFaire('alimentPlus'));
 c.STAT.alimentPlus=0;c.entrepotStock=()=>184;assert(c.testerFaire('alimentPlus'));c.HALLE.modules=[];assert(!c.testerFaire('alimentPlus'));
});
test('Refusing an unsigned offer preserves the client relationship and releases the order',()=>{
 const c=ready(),S=c.SITES[0];S.renom=5;S.offre=order(S);assert(c.refuserOffre(S));assert.equal(S.renom,5);assert.equal(S.offre,null);
});
test('Recurring offers contain all three volume formats without imposing deadlines',()=>{
 const c=equipped(ready()),formats=new Set();for(let i=0;i<1000;i++){const C=c.tirerCommande();assert(C);formats.add(C.texte.split(' · ')[0]);assert.equal(C.temps,0);for(const l of C.lignes)assert(l.need<=c.capaciteFerme(l.cle)*.55+1e-8);}
 assert.deepEqual([...formats].sort(),['Commande régulière','Gros lot','Réassort'].sort());
});
test('Wool discovery takes under ten minutes with the four recommended sheep',()=>{
 const c=ready();assert.equal(c.MISSIONS[16].lignes[0].need,12);assert.equal(c.MISSIONS[19].lignes[0].need,40);
 assert(12/(4*2/300)<600);assert(source.includes("16:{cle:'mouton',n:4}"));
});
test('A partial final ration produces only the corresponding fraction of an animal cycle',()=>{
 function run(dt){const c=ready();c.ESPECES={poule:{rationCycle:1,ration:1,parSec:2,produit:'oeufs',statique:true,maturite:300}};c.PATURES=[{espece:'poule',betes:[{age:1}],grain:.5,produit:0,produitMax:100}];c.ABEILLES=[];c.majTasAuge=()=>{};load(c,['updateElevage']);for(let t=0;t<10;t+=dt)c.updateElevage(dt);return c.PATURES[0];}
 const a=run(10),b=run(.1);assert(Math.abs(a.produit-1)<1e-9);assert(Math.abs(a.produit-b.produit)<1e-9);assert.equal(a.grain,0);
});
test('Truck deliveries inside the quay use a local obstacle-avoiding route',()=>{
 const c=ready();Object.assign(c,{FORET:{x0:300,z0:-50,z1:100},PORT:{routeFin:-166,cale:{z1:14}},PISTE_BOIS:{x:364},ROAD_N:-75,ROAD_W:14});let road=0;
 c.cheminNature=(v,p)=>[{x:v.pos.x,z:-72},p];c.itineraire=()=>{road++;return [];};load(c,['itineraireLivraison']);const r=c.itineraireLivraison({pos:{x:-247,z:-70}},-265,-86);assert.equal(road,0);assert.equal(r.at(-1).x,-265);
});
test('A completed mission appends its receipt without discarding an unread tutorial',()=>{
 const c=windows();c.titreMission=()=> 'Test';load(c,['ouvrirBravo']);c.annoncerFenetre({titre:'Tutoriel non lu'});
 c.ouvrirBravo({lieu:'Moi',prime:100,xp:0},{},20);assert.equal(c.bravoPages.length,2);assert.equal(c.document.getElementById('brtitre').textContent,'Tutoriel non lu');
 c.suivantBravo();assert.equal(c.document.getElementById('brtitre').textContent,'CONTRAT TERMINÉ');
});
test('Food oil is never ordered by the sawmill or textile workshop, but remains useful for canned fish',()=>{
 const c=equipped(ready());assert.deepEqual(Array.from(c.NEGOCE.Scierie.achete),['grumes']);assert(!c.SITES.find(s=>s.nom==='Atelier textile').achete.includes('huile'));
 assert(c.NEGOCE.Conserverie.achete.includes('huile'));assert.equal(c.MISSIONS[30].lignes.length,1);assert.equal(c.MISSIONS[30].lignes[0].need,300);assert(!c.MISSIONS[30].texte.includes('huile'));
 let seen=0;for(let i=0;i<1500;i++){const C=c.tirerCommande();if(['Scierie','Atelier textile'].includes(C.lieu)){seen++;assert(!C.lignes.some(l=>l.cle==='huile'));}}assert(seen>50);
});
test('An old mixed industrial order keeps its delivered goods, promised bonus and automation identity',()=>{
 const c=ready(),original={autoId:'delivery-7',lieu:'Scierie',prime:1000,xp:30,lignes:[{cle:'grumes',need:300,fait:120},{cle:'huile',need:20,fait:5}]};
 c.chargerCampagne({campagne:{mv:4,tv:4,xp:100000,mission:37,contrats:[original]}});const C=c.CONTRATS[0];assert(C);assert.equal(C.lignes.length,1);assert.equal(C.lignes[0].fait,120);assert.equal(C.prime,1000);assert.equal(C.autoId,'delivery-7');assert.equal(original.lignes.length,2);
});
test('A migrated industrial order already fulfilled in wood pays once instead of disappearing unpaid',()=>{
 const c=ready();c.veillerMission=()=>{};load(c,['updateCommandes']);const D={lieu:'Scierie',prime:1000,xp:30,lignes:[{cle:'grumes',need:300,fait:300},{cle:'huile',need:20,fait:0}]};
 c.chargerCampagne({campagne:{mv:4,tv:4,xp:100000,mission:37,contrats:[D]}});assert(c.CONTRATS[0].soldeMetier);
 const saved=JSON.parse(JSON.stringify(c.CONTRATS));c.chargerCampagne({campagne:{mv:4,tv:4,xp:100000,mission:37,contrats:saved}});assert.equal(c.CONTRATS.length,1);
 c.updateCommandes(0);assert.equal(c.money,1000);assert.equal(c.CONTRATS.length,0);c.updateCommandes(0);assert.equal(c.money,1000);
});
test('An old pending textile offer keeps wool and drops food oil without becoming a signed contract',()=>{
 const c=ready(),S=c.SITES.find(s=>s.nom==='Atelier textile');c.chargerCampagne({campagne:{mv:4,tv:4,xp:100000,mission:37,appels:[{lieu:S.nom,offre:{lieu:S.nom,prime:300,lignes:[{cle:'laine',need:12,fait:0},{cle:'huile',need:10,fait:0}]}}]}});
 assert.equal(S.offre.lignes.length,1);assert.equal(S.offre.lignes[0].cle,'laine');assert.equal(c.CONTRATS.length,0);
});
test('Unrelated food orders and existing sawmill campaign progress are preserved',()=>{
 const c=ready(),D={lieu:'Conserverie',lignes:[{cle:'huile',need:24,fait:12}]};assert.equal(c.corrigerCommandeMetier(D),D);
 c.chargerCampagne({campagne:{mv:4,tv:4,xp:100000,mission:30,prise:true,faits:[140,8]}});assert.equal(c.CAMPAGNE.mission,30);assert.equal(c.CAMPAGNE.faits[0],140);assert(c.CAMPAGNE.prise);
});
console.log(count+' audit regression tests passed.');
