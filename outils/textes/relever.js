// TOUS LES TEXTES DU JEU, releves DANS LE JEU et non recopies.
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const fs = require('fs'), http = require('http'), path = require('path');
const ICI = require('path').dirname(require('fs').realpathSync(__filename));
const RACINE = require('path').resolve(ICI, '..', '..');
// three.js : celui du dossier de travail des bancs, ou celui d'a cote.
const T3 = fs.readFileSync(process.env.THREE ||
  path.join(ICI, 'three.min.js'), 'utf8');
const JEU = path.join(RACINE, 'index.html'), G = fs.readFileSync(JEU, 'utf8');
const srv = http.createServer((q, r) => {
  if (q.url.indexOf('three') >= 0) { r.writeHead(200,{'Content-Type':'application/javascript'}); r.end(T3); }
  else if (/^\/(portraits1?4?|produits|pictos)\/[A-Za-z0-9_\-]+\.png$/.test(q.url.split('?')[0])) {
    const f = path.join(path.dirname(JEU), q.url.split('?')[0].slice(1));
    if (fs.existsSync(f)) { r.writeHead(200,{'Content-Type':'image/png'}); r.end(fs.readFileSync(f)); }
    else { r.writeHead(404); r.end('non'); }
  } else { r.writeHead(200,{'Content-Type':'text/html; charset=utf-8'}); r.end(G); }
});
(async () => {
  const PORT = +(process.env.PORT || 8811);
  await new Promise(r => srv.listen(PORT, r));
  const b = await chromium.launch({ executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
    args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--no-sandbox'] });
  const page = await b.newPage({ viewport:{width:1000, height:600} });
  await page.route('**/three*.js', r=>r.fulfill({status:200, contentType:'application/javascript', body:T3}));
  await page.goto('http://127.0.0.1:' + PORT + '/index.html', {waitUntil:'load'});
  await page.waitForTimeout(2400);
  const dump = await page.evaluate(`JSON.stringify({
    tuto: (function(){
       // Trois marches changent de texte selon le mode : on les lit DANS LES DEUX.
       var lire = function(E, k){ var v = E[k];
         return (typeof v === 'function') ? v() : (v || null); };
       var pour = function(libre){
         var av = MODE_LIBRE; MODE_LIBRE = libre;
         var r = TUTO.map(function(E, i){ return {i:i, cle:E.cle,
            titre:lire(E, 'titre'), txt:lire(E, 'txt'), ou:lire(E, 'ou'),
            engin:E.engin || null, outil:E.outil || null,
            fen:E.fen || null, onglet:E.onglet || null}; });
         MODE_LIBRE = av; return r; };
       var camp = pour(false), lib = pour(true);
       return camp.map(function(E, i){
         E.libre = (lib[i].txt !== E.txt || lib[i].titre !== E.titre)
                   ? {titre:lib[i].titre, txt:lib[i].txt, ou:lib[i].ou} : null;
         return E; });
     })(),
    lecons: LECONS.map(function(L, i){ return {i:i, cle:L.cle, titre:L.titre, txt:L.txt,
       ou:L.ou || null, mur:!!L.mur, tot:!!L.tot, fen:L.fen || null, onglet:L.onglet || null,
       quand: String(L.quand || '').replace(/\\s+/g, ' ')}; }),
    missions: MISSIONS.map(function(M, i){ return {i:i, niv:M.niv, lieu:M.lieu || null,
       texte:M.texte, prime:M.prime, xp:M.xp, faire:M.faire || null,
       lignes:(M.lignes || []).map(function(l){ return {cle:l.cle, need:l.need,
         nom:(PRODUITS[l.cle] || {}).nom || l.cle,
         unite:(typeof qteNom === 'function') ? qteNom(l.cle, l.need) : (l.need + ' ' + l.cle)}; }),
       nom:(typeof titreMission === 'function') ? titreMission(M) : null,
       court:M.court || null, fin:M.fin || null,
       apres:(M.apres || []).map(function(a){ return {titre:a.titre, txt:a.txt}; }),
       prep:(M.prep || []).map(function(E){ return {cle:E.cle, titre:E.titre, txt:E.txt,
              ou:E.ou || null, quand:String(E.fait || '').replace(/\s+/g, ' ')}; })}; }),
    niveaux: NIVEAUX.map(function(N, i){ return {n:i+1, nom:N.nom, resume:N.resume,
       cultures:N.cultures||null, outils:N.outils||null, engins:N.engins||null,
       modules:N.modules||null, especes:N.especes||null, sites:N.sites||null,
       parcelles:N.parcelles||null}; }),
    produits: (function(){ var o = {}; for(var k in PRODUITS) o[k] = PRODUITS[k].nom; return o; })(),
    especes: ESP_CLES.map(function(k){ return {cle:k, nom:ESPECES[k].nom,
       pluriel:ESPECES[k].pluriel, batiment:ESPECES[k].batiment}; }),
    accueil: (function(){
      var t = document.getElementById('acctitre'), s2 = document.getElementById('accsous');
      var btns = [].map.call(document.querySelectorAll('#accbtns .accbtn'),
                             function(e){ return e.textContent.trim(); });
      return {titre:t ? t.textContent.trim() : null,
              sous:s2 ? s2.innerText.trim() : null, boutons:btns}; })(),
    deblocages: (typeof MOTS_DEBLOC !== 'undefined') ? MOTS_DEBLOC : null
  })`);
  fs.writeFileSync(path.join(ICI, 'textes.json'), dump);
  console.log('ok, ' + (dump.length/1024).toFixed(1) + ' Ko');
  await b.close(); srv.close(); process.exit(0);
})();
