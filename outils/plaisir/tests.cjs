// Le chapitre « plaisir de jouer » : défis du jour, série, primes, retour. On découpe ses
// fonctions dans le source comme le font les autres bancs, et on les fait tourner seules.
const fs=require('fs'),path=require('path'),vm=require('vm'),assert=require('assert/strict');
const source=fs.readFileSync(path.join(__dirname,'../../index.html'),'utf8');
const debut=source.indexOf('/* ---------- 29 bis. LE PLAISIR DE JOUER ---------- */'),fin=source.indexOf('/* ---------- 30. BOUCLE ---------- */');
assert(debut>0&&fin>debut,'chapitre introuvable');
const chapitre=source.slice(debut,fin);
let tests=0;function test(nom,f){f();tests++;console.log('PASS',nom);}
function monde(o={}){
 const boite={};
 const el=()=>({addEventListener(){},textContent:'',className:'',classList:{add(){},remove(){},toggle(){},contains:()=>false},offsetWidth:0});
 const c=vm.createContext(Object.assign({Math,JSON,Date,String,Object,Array,console,setTimeout:()=>{},
  localStorage:{getItem:k=>k in boite?boite[k]:null,setItem:(k,v)=>{boite[k]=String(v);}},
  navigator:{},window:{addEventListener(){}},document:{hidden:false,addEventListener(){},getElementById:el},
  money:0,cur:0,demarre:true,MODE_LIBRE:false,CAMPAGNE:{niveau:1,mission:0,xp:0},NIVEAUX:Array(20).fill({nom:'Palier'}),
  STAT:{moisson:0,mill:0,lait:0,oeufs:0,miel:0,laine:0,grumes:0,peche:0,ventes:0},MACHINES:[{v:{speed:0}}],CONTRATS:[],ONGLETS:[{id:'campagne'}],
  growingList:[],grow:()=>{},flushTint:()=>{},lireSauvegarde:()=>null,clefCourante:()=>'k',
  AUDIO:{bip(){}},el:{money:el()},hints:[],pages:[],xp:0,
  eur:v=>Math.round(v)+' €',kg:v=>Math.round(v)+' kg',litres:v=>Math.round(v)+' L',dec:(v,n)=>v.toFixed(n),caisseTxt:()=>'',
  texteSiChange(){},pluiePieces(){},titre(){},article:()=>({classList:{add(){}}}),tutoActif:()=>false},o));
 vm.runInContext('function showHint(t){hints.push(t);}function annoncerFenetre(p){pages.push(p);}function gagnerXp(n){xp+=n;}'+
  'function encaisser(n){if(!(n>0))return 0;money+=n;return n;}function solderContrat(k){CONTRATS[k]=null;}',c);
 vm.runInContext(chapitre.replace(/^const /gm,'var '),c);
 c.boite=boite;return c;
}
const run=(c,code)=>vm.runInContext(code,c);

test('Le même jour tire les mêmes trois défis, un autre jour en tire d’autres dans la même réserve',()=>{
 const c=monde();
 const a=run(c,"JSON.stringify(plaisirTirer('2026-11-15'))"),b=run(c,"JSON.stringify(plaisirTirer('2026-11-15'))");
 assert.equal(a,b);assert.equal(JSON.parse(a).length,3);
 assert.equal(new Set(JSON.parse(a).map(D=>D.id)).size,3);
});
test('Aucun défi de produit sans que la ferme en ait déjà sorti, et un seul au plus ensuite',()=>{
 const c=monde();
 for(let j=1;j<=28;j++){const T=run(c,`plaisirTirer('2026-02-${String(j).padStart(2,'0')}')`);
  for(const D of T)assert(!run(c,`!!PLAISIR_DEFIS['${D.id}'].produit`),D.id);}
 run(c,'STAT.lait=10;STAT.oeufs=4;STAT.peche=9;');
 for(let j=1;j<=28;j++){const T=run(c,`plaisirTirer('2026-03-${String(j).padStart(2,'0')}')`);
  assert.equal(T.filter(D=>run(c,`!!PLAISIR_DEFIS['${D.id}'].produit`)).length,1);}
});
test('Le mode libre ne propose jamais de commande à honorer : il n’en a pas',()=>{
 const c=monde({MODE_LIBRE:true});
 for(let j=1;j<=28;j++)assert(!run(c,`plaisirTirer('2026-04-${String(j).padStart(2,'0')}')`).some(D=>D.id==='commande'));
});
test('Les cibles et les primes suivent le palier',()=>{
 const c=monde();const bas=run(c,"plaisirTirer('2026-05-01')");
 run(c,'CAMPAGNE.niveau=12;');const haut=run(c,"plaisirTirer('2026-05-01')");
 bas.forEach((D,i)=>{assert.equal(haut[i].id,D.id);assert(haut[i].prime>D.prime);assert(haut[i].cible>=D.cible);assert(D.prime>=30);});
});
test('Un défi rempli ne paie rien tant qu’on ne l’a pas encaissé soi-même',()=>{
 const c=monde();run(c,'plaisirLancer();PLAISIR.e.defis=[{id:"gains",cible:200,fait:0,prime:40,xp:4,paye:false}];');
 const D=run(c,'PLAISIR.e.defis[0]');
 const avant=c.money;
 run(c,`encaisser(${D.cible});`);
 assert.equal(c.money,avant+D.cible,'seule la vente est entrée en caisse');
 assert.equal(c.xp,0);
 assert(c.hints.some(t=>/DÉFI REMPLI/.test(t)));
 assert.equal(run(c,'plaisirAPrendre()'),1);
 run(c,'plaisirPayer(PLAISIR.e.defis.find(D=>D.id==="gains").prime,3);');
 assert.equal(c.money,avant+D.cible+D.prime);
});
test('La série avance d’un jour sur l’autre, retombe après un jour manqué, et la prime attend le deuxième jour',()=>{
 const c=monde();
 run(c,'plaisirJourNouveau();');assert.equal(run(c,'PLAISIR.e.serie'),1);assert.equal(run(c,'plaisirAPrendre()'),0);
 run(c,'PLAISIR.e.dernier=plaisirJour(new Date(Date.now()-86400000));plaisirJourNouveau();');
 assert.equal(run(c,'PLAISIR.e.serie'),2);assert.equal(run(c,'primeFidelite()'),40);assert.equal(run(c,'plaisirAPrendre()'),1);
 run(c,'PLAISIR.e.dernier=plaisirJour(new Date(Date.now()-3*86400000));plaisirJourNouveau();');
 assert.equal(run(c,'PLAISIR.e.serie'),1);assert.equal(run(c,'PLAISIR.e.serieMax'),2);
 run(c,'PLAISIR.e.serie=30;');assert.equal(run(c,'primeFidelite()'),140,'plafonnée au septième jour');
});
test('Pendant le tutoriel : ni défis, ni prime, ni page de retour',()=>{
 const c=monde({tutoActif:()=>true,lireSauvegarde:()=>({quand:Date.now()-5*3600*1000})});
 run(c,'PLAISIR.e.dernier=plaisirJour(new Date(Date.now()-86400000));PLAISIR.e.serie=4;');
 c.localStorage.setItem('moisson.plaisir.v1',JSON.stringify(run(c,'PLAISIR.e')));
 run(c,'plaisirLancer();');
 assert.equal(run(c,'PLAISIR.e.defis.length'),0);assert.equal(run(c,'plaisirAPrendre()'),0);assert.equal(c.pages.length,0);
});
test('Au retour les cultures poussent, vingt minutes au plus, et la page ne vient qu’après une demi-heure',()=>{
 let pousse=[];
 const c=monde({growingList:[1,2,3],grow:dt=>pousse.push(dt),lireSauvegarde:()=>({quand:Date.now()-10*60*1000})});
 run(c,'plaisirLancer();');
 assert.equal(pousse.length,1);assert(Math.abs(pousse[0]-600)<5);assert.equal(c.pages.length,0);
 pousse=[];
 const d=monde({growingList:[1,2,3],grow:dt=>pousse.push(dt),lireSauvegarde:()=>({quand:Date.now()-9*3600*1000})});
 run(d,'plaisirLancer();');
 assert.equal(pousse[0],1200);assert.equal(d.pages.length,1);assert.equal(d.pages[0].titre,'BON RETOUR');
});
test('Une partie neuve ne reçoit ni pousse ni page',()=>{
 let n=0;const c=monde({growingList:[1],grow:()=>n++});run(c,'plaisirLancer();');
 assert.equal(n,0);assert.equal(c.pages.length,0);assert.equal(c.money,0);
});
test('Un record ne s’annonce que s’il y en avait un à battre',()=>{
 const c=monde();run(c,'plaisirLancer();encaisser(300);plaisirFinRafale();');
 assert.equal(run(c,'PLAISIR.e.records.vente'),300);assert(!c.hints.some(t=>/RECORD/.test(t)));
 run(c,'encaisser(500);plaisirFinRafale();');
 assert.equal(run(c,'PLAISIR.e.records.vente'),500);assert(c.hints.some(t=>/RECORD DE VENTE/.test(t)));
});
test('L’étiquette cumule une rafale, et repart de zéro quand le signe change',()=>{
 const c=monde();run(c,'plaisirLancer();money+=40;plaisirCaisse(0.016);money+=60;plaisirCaisse(0.016);');
 assert.equal(run(c,'PLAISIR.chipSomme'),100);
 run(c,'money-=650;plaisirCaisse(0.016);');assert.equal(run(c,'PLAISIR.chipSomme'),-650);
 run(c,'for(let i=0;i<120;i++)plaisirCaisse(0.016);');assert.equal(run(c,'PLAISIR.vu'),c.money,'le chiffre se pose exactement sur le solde');
});
test('Un état abîmé ou étranger se relit sans rien casser',()=>{
 const c=monde();c.localStorage.setItem('moisson.plaisir.v1','{"defis":[{"id":"inconnu","cible":5},{"id":"gains","cible":-1},null],"serie":"x","records":7}');
 run(c,'plaisirLire();');assert.equal(run(c,'PLAISIR.e.defis.length'),0);assert.equal(run(c,'PLAISIR.e.serie'),0);
 c.localStorage.setItem('moisson.plaisir.v1','{pas du json');run(c,'plaisirLire();');
});
test('Le chapitre n’écrit rien dans la sauvegarde de la partie',()=>{
 const f=source.slice(source.indexOf('function etatJeu('),source.indexOf('function sauvegarder('));
 assert(!/PLAISIR|plaisir/.test(f));
 assert(!/PLAISIR|plaisir/.test(source.slice(source.indexOf('function chargerPartie('),source.indexOf('function chargerPartie(')+40000)));
});
console.log(tests+' plaisir tests passed.');
