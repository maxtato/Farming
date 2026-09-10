const fs=require('fs'),vm=require('vm'),assert=require('assert/strict'),path=require('path');
const source=fs.readFileSync(path.join(__dirname,'../../index.html'),'utf8');
function fn(name){const a=source.indexOf('function '+name+'(');assert(a>=0,name);return source.slice(a,source.indexOf('\n}',a)+2);}
function setup(){
 let seed=8123;const math=Object.create(Math);math.random=()=>((seed=Math.imul(seed,1664525)+1013904223>>>0)/4294967296);
 const c=vm.createContext({Math:math,Number,Infinity,PORT:{spots:[{x:-310,z:-10,cle:'poisson'},{x:-370,z:55,cle:'poisson'},{x:-240,z:105,cle:'crustaces'}],spotR:8,jetee:{x:-280,w:12,z1:-12},marina:{x0:-236,z:-2}},EAU:{x0:-417,x1:-200,z0:-56,z1:172},MACHINES:[],NATURE_JOBS:[],cur:0,STAT:{peche:0},messages:[],jumps:0,
  natureJob:()=>null,naturesDe:K=>K.load?[K.type]:[],siSouvent:()=>false,bullePeche:()=>{},puff:()=>{},solderLecon:()=>{},nomDe:k=>k,kg:q=>q,
 });
 c.showHint=t=>c.messages.push(t);c.sautPoisson=()=>c.jumps++;c.ajouterCharge=(K,k,q)=>{K.type=k;K.load+=q;};
 vm.runInContext(['spotPecheProche','dansSpot','positionSpotValide','poserReperePeche','deplacerSpotPeche','initialiserSpotsPeche','majSpotsPeche','sauverSpotsPeche','chargerSpotsPeche','travailPeche','changerPhaseNature'].map(fn).join('\n'),c);
 return c;
}
let n=0;function test(name,f){f(setup());n++;console.log('PASS '+name);}
function boat(c,cle,S){const m={key:cle==='crustaces'?'caseyeur':'barque',bateau:true,verrou:false,peche:{cle,duree:1,lot:5},v:{speed:0,pos:{x:S.x,z:S.z},cargo:{load:0,capacite:50}}};c.MACHINES.push(m);return m;}
test('Thousands of renewed positions remain offshore, separated and away from the marina and pier',c=>{
 const positions=new Set();for(let i=0;i<1000;i++){c.initialiserSpotsPeche();for(const S of c.PORT.spots){assert(c.positionSpotValide(S.x,S.z,c.PORT.spots.filter(P=>P!==S)));assert(S.t>=180&&S.t<=300);positions.add(S.x.toFixed(1)+','+S.z.toFixed(1));}}
 assert(positions.size>2900);assert.equal(c.PORT.spots.filter(S=>S.cle==='poisson').length,2);assert.equal(c.PORT.spots.filter(S=>S.cle==='crustaces').length,1);
});
test('Renewal chooses a meaningfully different position without creating more spots',c=>{c.initialiserSpotsPeche();const S=c.PORT.spots[0],old={...S};assert(c.deplacerSpotPeche(S));assert(Math.hypot(S.x-old.x,S.z-old.z)>=45);assert.equal(c.PORT.spots.length,3);});
test('A quiet zone expires and moves after its timer',c=>{c.initialiserSpotsPeche();const S=c.PORT.spots[0],x=S.x;S.t=.1;c.majSpotsPeche(.5);assert.notEqual(S.x,x);assert(S.t>=180);});
test('A boat fishing on a zone prevents renewal even after expiry',c=>{c.initialiserSpotsPeche();const S=c.PORT.spots[0],x=S.x;boat(c,'poisson',S);S.t=0;S.utilise=true;c.majSpotsPeche(600);assert.equal(S.x,x);});
test('An automatic boat travelling to a reserved zone keeps the destination stable',c=>{c.initialiserSpotsPeche();const S=c.PORT.spots[0],x=S.x;S.t=0;c.NATURE_JOBS.push({key:'barque',phase:'aller',cible:0});c.majSpotsPeche(600);assert.equal(S.x,x);});
test('A harvested zone renews after the boat leaves and frees its reservation',c=>{c.initialiserSpotsPeche();const S=c.PORT.spots[0],m=boat(c,'poisson',S),x=S.x;S.utilise=true;S.t=200;const J={key:'barque',phase:'aller',cible:0};c.NATURE_JOBS.push(J);c.changerPhaseNature(J,'vider');assert.equal(J.cible,-1);m.v.pos={x:-220,z:-45};c.majSpotsPeche(.5);assert.notEqual(S.x,x);assert(!S.utilise);});
test('Renewal never places a zone beneath another boat',c=>{c.initialiserSpotsPeche();const m=boat(c,'crustaces',{x:-250,z:90});for(let i=0;i<100;i++){c.PORT.spots.forEach(S=>S.t=0);c.majSpotsPeche(1);for(const S of c.PORT.spots)assert(Math.hypot(S.x-m.v.pos.x,S.z-m.v.pos.z)>=28);}});
test('An unlucky random generator terminates promptly and keeps the previous valid point',c=>{const S=c.PORT.spots[0],x=S.x,z=S.z;let tries=0;assert(!c.deplacerSpotPeche(S,()=>{tries++;return 0;},()=>false));assert(tries<=240);assert.equal(S.x,x);assert.equal(S.z,z);});
test('Saving restores positions, timers and harvest state without replacing marker objects',c=>{c.initialiserSpotsPeche();c.PORT.spots[0].utilise=true;const saved=JSON.parse(JSON.stringify(c.sauverSpotsPeche())),S=c.PORT.spots[0];c.initialiserSpotsPeche();c.chargerSpotsPeche(saved);assert.equal(c.PORT.spots[0],S);assert.equal(JSON.stringify(c.sauverSpotsPeche()),JSON.stringify(saved));});
test('Invalid or legacy spot saves cannot put fishing on land or mix resource types',c=>{c.initialiserSpotsPeche();const before=JSON.stringify(c.sauverSpotsPeche());c.chargerSpotsPeche(undefined);let bad=JSON.parse(before);bad[0].x=0;c.chargerSpotsPeche(bad);assert.equal(JSON.stringify(c.sauverSpotsPeche()),before);bad=JSON.parse(before);bad[0].cle='crustaces';c.chargerSpotsPeche(bad);assert.equal(JSON.stringify(c.sauverSpotsPeche()),before);});
test('Nearest-spot guidance only returns the requested resource',c=>{const v={pos:{x:-240,z:105}};assert.equal(c.spotPecheProche('crustaces',v),c.PORT.spots[2]);assert.equal(c.spotPecheProche('poisson',v).cle,'poisson');assert.equal(c.dansSpot(v,'poisson'),null);});
test('Manual fishing cannot harvest the wrong resource and explains the mismatch once',c=>{const m=boat(c,'poisson',c.PORT.spots[2]);for(let i=0;i<10;i++)c.travailPeche(m,1);assert.equal(m.v.cargo.load,0);assert.equal(c.messages.length,1);assert.match(c.messages[0],/CASEYEUR/);m.v.pos={x:c.PORT.spots[0].x,z:c.PORT.spots[0].z};c.travailPeche(m,1);assert.equal(m.v.cargo.load,5);assert(c.PORT.spots[0].utilise);});
test('The potting boat catches only crustaceans and creates no jumping fish',c=>{const m=boat(c,'crustaces',c.PORT.spots[2]);c.travailPeche(m,1);assert.equal(m.v.cargo.type,'crustaces');assert.equal(m.v.cargo.load,5);assert.equal(c.jumps,0);m.v.pos={x:c.PORT.spots[0].x,z:c.PORT.spots[0].z};c.travailPeche(m,1);assert.equal(m.v.cargo.load,5);});
test('Both ring meshes and their interaction coordinates follow each move',c=>{const mesh=()=>({position:{x:0,z:0},updateMatrix(){this.updated=true;}}),S=c.PORT.spots[0];S.repere={anneau:mesh(),centre:mesh()};c.deplacerSpotPeche(S);for(const m of [S.repere.anneau,S.repere.centre]){assert.equal(m.position.x,S.x);assert.equal(m.position.z,S.z);assert(m.updated);assert(m.matrixWorldNeedsUpdate);}assert.equal(S.repere.x,S.x);assert.equal(S.repere.z,S.z);});
console.log(n+' fishing spot tests passed.');
