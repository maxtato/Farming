/* OU LE JEU POSE SES IMAGES, ET A QUELLE TAILLE. MESURE, PAS SUPPOSE.
   C est l instrument dont depend tout le reste de outils/portraits : fabriquer.py ne
   choisit pas la taille d une planche, il la CALCULE — la boite ou le jeu la pose, divisee
   par PX_JEU. Encore faut-il connaitre la boite, et la lire dans le CSS ne suffit pas :
   une regle peut etre surchargee, une fenetre peut n exister qu au moment ou elle
   s ouvre, et une animation d entree ment sur la taille pendant un tiers de seconde.
   On mesure donc sur une session COMPLETE.

     PORTRAITS_BANCS=<dossier> node poses.js ../../index.html

   PORTRAITS_BANCS designe le dossier qui contient node_modules (playwright et three) ; il
   vaut ce dossier-ci par defaut. PORTRAITS_POSES dit ou ecrire le releve complet en JSON.

   DEUX INSTRUMENTS, parce que le jeu pose ses images de deux facons.
     - drawImage sur un contexte 2D : on releve la taille de destination AVEC la matrice
       courante appliquee, pas les unites internes. Resultat a ce jour : ZERO source. Le jeu
       ne pose aucune image par cette voie — les portraits sont des <img> du document et le
       monde est en WebGL. L instrument reste, parce que le jour ou une planche de tuiles
       arrivera il faudra le savoir tout de suite.
     - les <img> du document : on echantillonne la boite APRES la fin des animations a
       nombre de tours fini (celles qui bouclent — clignotants, respiration des appels — ne
       finissent jamais, on ne les attend pas), et on lit offsetWidth plutot que
       getBoundingClientRect. LA LECON EST LA : la premiere version lisait le rectangle,
       donc la boite MULTIPLIEE par la matrice d entree, et rapportait 172 x 212 pour un
       visage de 192 x 240. On aurait taille quarante et une planches sur ce chiffre.
       Le rectangle est quand meme releve, et signale entre crochets s il depasse la boite.

   LA COUVERTURE FAIT PARTIE DE LA MESURE. La session ouvre le contrat, l ecran de gain et
   le refus de CHAQUE commerce, puis les guichets et leurs onglets — et le compte rendu
   compare aux fichiers livres. Une planche jamais posee est une planche dont on ne sait
   rien : la premiere version en laissait sept de cote (les refus des commerces sans liste
   achete) et croyait avoir tout vu.

   LE VERDICT, ENFIN, EST UNE LISTE D ECARTS. Pour chaque pose : largeur affichee divisee
   par largeur de planche, comparee a PX_JEU. Ce qui ne tombe pas juste est nomme.
*/
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const fs = require('fs'), http = require('http'), path = require('path');
const S = process.env.PORTRAITS_BANCS || __dirname;
const T3 = fs.readFileSync(S + '/node_modules/three/build/three.min.js', 'utf8');
const JEU = path.resolve(process.argv[2] || path.join(__dirname, '..', '..', 'index.html'));
const G = fs.readFileSync(JEU, 'utf8');
const srv = http.createServer((q, r) => {
  if (q.url.indexOf('three') >= 0) { r.writeHead(200,{'Content-Type':'application/javascript'}); r.end(T3); return; }
  const m = /^\/(portraits\/[A-Za-z0-9_\-]+\.png)$/.exec(q.url.split('?')[0]);
  if (m) { const f = path.join(path.dirname(JEU), m[1]);
           if (fs.existsSync(f)) { r.writeHead(200,{'Content-Type':'image/png'}); r.end(fs.readFileSync(f)); }
           else { r.writeHead(404); r.end('non'); } return; }
  r.writeHead(200,{'Content-Type':'text/html; charset=utf-8'}); r.end(G);
});
const PORT = +(process.env.PORT || 9820);
(async () => {
  await new Promise(r => srv.listen(PORT, r));
  const b = await chromium.launch({ executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
    args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--no-sandbox'] });
  const page = await b.newPage({ viewport:{width:900, height:620} });
  await page.addInitScript(`(function(){
    window.__POSES = {img:{}, draw:{}};
    const P = CanvasRenderingContext2D.prototype, vrai = P.drawImage;
    P.drawImage = function(){
      try{
        const a = arguments, s = a[0];
        let dw, dh;
        if(a.length >= 9){ dw = a[7]; dh = a[8]; }
        else if(a.length >= 5){ dw = a[3]; dh = a[4]; }
        else { dw = s.width || s.videoWidth || 0; dh = s.height || s.videoHeight || 0; }
        const m = this.getTransform ? this.getTransform() : null;
        const kx = m ? Math.hypot(m.a, m.b) : 1, ky = m ? Math.hypot(m.c, m.d) : 1;
        const nom = (s && (s.src || s.__nom)) ? String(s.src || s.__nom).split('/').pop()
                  : (s && s.tagName ? s.tagName.toLowerCase() + ':' + (s.width||0) + 'x' + (s.height||0) : '?');
        const n = (s && s.naturalWidth) || (s && s.width) || 0;
        const d = window.__POSES.draw;
        const e = d[nom] || (d[nom] = {n:0, w:0, h:0, appels:0});
        e.appels++; e.n = Math.max(e.n, n);
        e.w = Math.max(e.w, dw*kx); e.h = Math.max(e.h, dh*ky);
      }catch(err){}
      return vrai.apply(this, arguments);
    };
    window.__relever = function(){
      const o = window.__POSES.img;
      const T = document.querySelectorAll('img');
      for(const im of T){
        if(!im.src) continue;
        const cs = getComputedStyle(im);
        if(cs.display === 'none' || cs.visibility === 'hidden') continue;
        const bw = im.offsetWidth, bh = im.offsetHeight;   /* la BOITE, hors animation d entree */
        if(bw < 1 || bh < 1) continue;
        const r  = im.getBoundingClientRect();             /* la boite AVEC la matrice courante */
        const nw = im.naturalWidth, nh = im.naturalHeight;
        /* object-fit: contain — la surface reellement peinte, pas la boite */
        let pw = bw, ph = bh;
        if(cs.objectFit === 'contain' && nw && nh){
          const k = Math.min(bw/nw, bh/nh); pw = nw*k; ph = nh*k;
        }
        const nom = im.src.split('/').pop();
        const cle = nom + ' @#' + (im.id || im.className);
        const e = o[cle] || (o[cle] = {fichier:nom, n:0, t:0, w:0, h:0, bw:0, bh:0, rw:0, rendu:cs.imageRendering, id:im.id, fit:cs.objectFit, vus:0});
        e.n = nw; e.t = nh; e.vus++;
        if(pw > e.w){ e.w = pw; e.h = ph; }
        e.bw = Math.max(e.bw, bw); e.bh = Math.max(e.bh, bh);
        e.rw = Math.max(e.rw, r.width);
        e.rendu = cs.imageRendering; e.id = im.id || e.id;
      }
      return 1;
    };
  })()`);
  await page.route('**/three*.js', r=>r.fulfill({status:200, contentType:'application/javascript', body:T3}));
  await page.goto('http://127.0.0.1:' + PORT + '/index.html', {waitUntil:'load'});
  await page.waitForTimeout(2600);
  await (await page.$('.accbtn.pri')).click();
  await page.waitForTimeout(800);
  const ev = (js)=> page.evaluate('(function(){' + js + '})()');
  /* On echantillonne APRES la fin des animations d entree : la boite est mesuree hors
     matrice (offsetWidth) mais on releve aussi la boite transformee, pour dire si le
     jeu depasse la taille de repos a un moment. */
  const rel = async ()=>{
    await page.evaluate(`(async function(){
      try{
        /* Les animations EN BOUCLE du jeu (clignotants, respiration des appels) ne
           finissent jamais : on n attend que celles a nombre de tours fini, et jamais
           plus d une demi-seconde. */
        const fini = document.getAnimations().filter(function(a){
          const t = a.effect && a.effect.getTiming ? a.effect.getTiming() : null;
          return t && t.iterations !== Infinity;
        }).map(a=>a.finished.catch(()=>0));
        await Promise.race([Promise.all(fini), new Promise(r=>setTimeout(r, 500))]);
      }catch(e){}
    })()`);
    await page.evaluate('window.__relever()');
  };
  await ev("for(let k=0;k<4;k++){const b=Array.prototype.slice.call(document.querySelectorAll('.accbtn')).filter(function(x){return x.offsetParent!==null;})[0]; if(!b)break; b.click();} return 1;");
  await page.waitForTimeout(400);
  await ev('fermerBravo(); CAMPAGNE.tuto = 99; CAMPAGNE.niveau = NIVEAUX.length; return 1;');
  await rel();
  /* --- toutes les poses de portrait, commerce par commerce --- */
  const noms = await page.evaluate('Object.keys(PORTRAITS)');
  for(const n of noms){
    await ev(`const S = SITES.find(function(x){ return x.nom === ${JSON.stringify(n)}; });
      const f = ficheDe(${JSON.stringify(n)});
      if(f && f.h.indexOf('neutre') >= 0 && S)
        ouvrirContrat({lieu:S.nom, type:CMD_TYPES[0].cle, prime:900, xp:120,
          lignes:[{cle:'ble', need:40}]}, S, true, {texte:'Essai.'});
      return 1;`);
    await page.waitForTimeout(620); await rel();
    await ev('fermerContrat(); return 1;');
    await ev(`const f = ficheDe(${JSON.stringify(n)});
      if(f && f.h.indexOf('bravo') >= 0)
        ouvrirBravo({lieu:${JSON.stringify(n)}, lignes:[{cle:'ble', need:40}], prime:900, xp:120,
                     fin:'Merci.'}, null, CAMPAGNE.niveau - 1);
      return 1;`);
    await page.waitForTimeout(620); await rel();
    await ev('fermerBravo(); return 1;');
    await ev(`const S = SITES.find(function(x){ return x.nom === ${JSON.stringify(n)}; });
      const f = ficheDe(${JSON.stringify(n)});
      if(S && f && f.h.indexOf('refus') >= 0){
        /* Certains commerces n ont pas de liste achete : on leur pose quand meme le
           refus avec une marchandise valide, sinon leur planche -refus n est jamais
           mesuree et la couverture du releve est fausse. */
        const c = (S.achete && S.achete.length) ? S.achete[0]
                : (S.prend && S.prend.length) ? S.prend[0] : Object.keys(PRODUITS)[0];
        S.reste = S.reste || {}; S.reste[c] = 0;
        montrerRefus(S, c, 60);
      }
      return 1;`);
    await page.waitForTimeout(620); await rel();
    await ev('fermerBravo(); return 1;');
  }
  /* --- les guichets : comptoir (trois rayons) et garage (deux fenetres) --- */
  for(const f of ['comptoir', 'achat', 'amelio', 'stockage']){
    await ev(`try{ ouvrirFenetre(${JSON.stringify(f)}); }catch(e){}
      return 1;`);
    await page.waitForTimeout(620); await rel();
    const onglets = await page.evaluate("Array.prototype.slice.call(document.querySelectorAll('#fenongs .ong, #fentete .ong')).length");
    for(let i = 0; i < onglets; i++){
      await page.evaluate(`(function(){const o=document.querySelectorAll('#fenongs .ong, #fentete .ong')[${i}]; if(o) o.dispatchEvent(new PointerEvent('pointerdown',{bubbles:true}));})()`);
      await page.waitForTimeout(420); await rel();
    }
    await ev('try{ fermerFenetre(); }catch(e){} return 1;');
  }
  await rel();
  const out = await page.evaluate('JSON.stringify(window.__POSES)');
  fs.writeFileSync(process.env.PORTRAITS_POSES || '/tmp/poses.json', out);
  const P = JSON.parse(out);
  const im = Object.keys(P.img).sort();
  console.log('=== IMAGES DU DOCUMENT (' + im.length + ' poses) ===');
  console.log('fichier                        elem       planche   boite     peint     PX_JEU  rendu');
  for(const k of im){
    const e = P.img[k];
    console.log(e.fichier.padEnd(31) + ('#'+(e.id||'?')).padEnd(11)
      + (e.n + 'x' + e.t).padEnd(10)
      + (Math.round(e.bw) + 'x' + Math.round(e.bh)).padEnd(10)
      + (Math.round(e.w) + 'x' + Math.round(e.h)).padEnd(10)
      + (e.w ? (e.w/e.n).toFixed(4) : '—').padEnd(8) + e.rendu
      + (e.rw > e.bw + 0.5 ? '  [matrice max ' + Math.round(e.rw) + ']' : ''));
  }
  /* LE VERDICT DU POINT 6 : image par image, largeur affichee / largeur de planche, et
     l ECART a PX_JEU. On liste les ecarts, on ne dit pas que c est fait. */
  const PX_JEU = 1/3;
  const ecarts = [];
  for(const k of im){
    const e = P.img[k];
    const r = e.w/e.n;
    if(Math.abs(r - PX_JEU) > 1e-4) ecarts.push({f:e.fichier, id:e.id, n:e.n, w:Math.round(e.w), r:r});
  }
  console.log('\n=== PX_JEU = 1/3 : ' + (im.length - ecarts.length) + ' poses sur ' + im.length
    + ' tombent sur la grille, ' + ecarts.length + ' ecart(s) ===');
  if(!ecarts.length) console.log('  aucun');
  for(const e of ecarts)
    console.log('  ECART  ' + e.f.padEnd(26) + ' #' + (e.id||'?').padEnd(9)
      + ' planche ' + e.n + '  boite ' + e.w
      + '  -> ' + e.r.toFixed(4) + ' px CSS par pixel d art (au lieu de 0.3333)');

  const dr = Object.keys(P.draw).sort();
  console.log('\n=== drawImage SUR CONTEXTE 2D (' + dr.length + ' sources) ===');
  for(const k of dr){
    const e = P.draw[k];
    console.log(k.padEnd(34) + String(e.n||'—').padEnd(11)
      + (Math.round(e.w) + 'x' + Math.round(e.h)).padEnd(13)
      + (e.n ? (e.w/e.n).toFixed(4) : '—').padEnd(8) + e.appels + ' appels');
  }
  await b.close(); srv.close();
})().catch(e=>{ console.error('FAIL', e); srv.close(); process.exit(2); });
