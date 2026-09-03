// Encode les sons de sons.json pour le jeu : Chromium les décode (MP3, WAV, OGG…), les
// rééchantillonne à la fréquence retenue, les met en mono, les ramène à la crête voulue,
// et les écrit en WAV 16 bits base64 dans <cle>.b64. `poser.py` les pose ensuite dans la
// table SONS de index.html. Usage : node encoder.js [cle…]
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const fs = require('fs'), path = require('path');
const U = '/root/.claude/uploads/3c255efa-fd9f-5aab-a574-54544179bd6d/';
const ICI = __dirname;
const T = JSON.parse(fs.readFileSync(path.join(ICI, 'sons.json'), 'utf8'));
const cles = process.argv.slice(2).length ? process.argv.slice(2) : Object.keys(T).filter((k)=> k !== '_');
(async () => {
  const b = await chromium.launch({ executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args:['--no-sandbox'] });
  const page = await b.newPage();
  await page.setContent('<html><body></body></html>');
  for(const cle of cles){
    const S = T[cle];
    const b64 = fs.readFileSync(path.join(U, S.src)).toString('base64');
    const r = await page.evaluate(async ([b64, S]) => {
      const brut = atob(b64), u8 = new Uint8Array(brut.length);
      for(let i = 0; i < brut.length; i++) u8[i] = brut.charCodeAt(i);
      const c0 = new OfflineAudioContext(1, 44100, 44100);
      const buf = await c0.decodeAudioData(u8.buffer.slice(0));
      const d0 = S.debut || 0, d1 = S.fin || buf.duration;
      const n = Math.round((d1 - d0)*S.hz);
      const ctx = new OfflineAudioContext(1, n, S.hz);
      const src = ctx.createBufferSource(); src.buffer = buf; src.connect(ctx.destination);
      src.start(0, d0, d1 - d0);
      const out = await ctx.startRendering();
      let d = out.getChannelData(0);
      /* UNE HAUTEUR PLATE (`hauteur`, la hauteur nominale en Hz). On suit la hauteur par
         autocorrélation — fenêtre de 100 ms, pas de 50 ms, ±30 % autour de la nominale —,
         et pour une BOUCLE on rééchantillonne à vitesse variable : lu plus vite là où le
         moteur est plus bas, moins vite là où il est plus haut, pour que la hauteur soit
         égale d'un bout à l'autre, à sa moyenne. Sans cela, une croisière qui monte de 7 %
         sur deux secondes (le SUV du pick-up) se réentend à chaque tour comme un moteur qui
         redescend puis remonte. Une montée n'est pas touchée : on ne fait que dire sa
         hauteur au départ et à l'arrivée, pour caler la boucle dessus (`plage`). */
      let hauteur = null;
      if(S.hauteur){
        const suivre = (x)=>{
          const W = Math.round(S.hz*0.1), H = Math.round(S.hz*0.05);
          const l0 = Math.round(S.hz/(S.hauteur*1.3)), l1 = Math.round(S.hz/(S.hauteur*0.77));
          const P = [];
          for(let a = 0; a + W + l1 <= x.length; a += H){
            let best = -Infinity, bl = l0; const ac = [];
            for(let l = l0; l <= l1; l++){ let q = 0; for(let i = a; i < a + W; i++) q += x[i]*x[i+l]; ac[l] = q; if(q > best){ best = q; bl = l; } }
            let lag = bl;
            if(bl > l0 && bl < l1){ const y0 = ac[bl-1], y1 = ac[bl], y2 = ac[bl+1], den = y0 - 2*y1 + y2; if(den !== 0) lag = bl + 0.5*(y0 - y2)/den; }
            P.push({t:(a + W/2)/S.hz, hz:S.hz/lag});
          }
          return P;
        };
        const moy = (v)=> v.reduce((q, z)=> q + z, 0)/Math.max(1, v.length);
        // le départ et l'arrivée se lisent à la MÉDIANE de six fenêtres : une seule fenêtre
        // folle (93,9 Hz au milieu d'un plateau à 78, sur la montée du tracteur) faussait la
        // moyenne de quatre pour cent, et la boucle se calait dessus
        const med = (v)=>{ const w = v.slice().sort((a, b)=> a - b); return w.length ? (w.length % 2 ? w[(w.length-1)/2] : (w[w.length/2-1] + w[w.length/2])/2) : 0; };
        const stat = (P)=>{ const v = P.map((p)=> p.hz), m = moy(v);
          return {moy:+m.toFixed(1), sd:+(100*Math.sqrt(moy(v.map((z)=> (z - m)*(z - m))))/m).toFixed(2), debut:+med(v.slice(0, 6)).toFixed(1), fin:+med(v.slice(-6)).toFixed(1)}; };
        let P0 = suivre(d);
        hauteur = {avant:stat(P0), passes:0};
        // Plusieurs passes : la première ôte la dérive lente, les suivantes ce qui reste de
        // plus rapide que le lissage ; on s'arrête quand l'écart ne baisse plus.
        if(S.boucle && P0.length > 4){
          const cible = hauteur.avant.moy;
          let sd = hauteur.avant.sd;
          for(let passe = 0; passe < 4; passe++){
            const v = P0.map((p)=> p.hz);
            const med = v.map((z, i)=>{ const w = [v[Math.max(0, i-1)], z, v[Math.min(v.length-1, i+1)]].sort((a, b)=> a - b); return w[1]; });
            const lis = med.map((z, i)=>{ let q = 0, c = 0; for(let j = -1; j <= 1; j++){ const k = i + j; if(k >= 0 && k < med.length){ q += med[k]; c++; } } return q/c; });
            const pas = P0[1].t - P0[0].t;
            const hzA = (t)=>{ const u = (t - P0[0].t)/pas, i = Math.floor(u);
              if(i < 0) return lis[0]; if(i >= lis.length - 1) return lis[lis.length - 1];
              return lis[i]*(1 - (u - i)) + lis[i+1]*(u - i); };
            const sortie = []; let x = 0;
            while(x < d.length - 1){ const i = Math.floor(x), f = x - i; sortie.push(d[i]*(1 - f) + d[i+1]*f); x += cible/hzA(x/S.hz); }
            const d2 = Float32Array.from(sortie), P2 = suivre(d2), st2 = stat(P2);
            if(st2.sd >= sd - 0.05) break;
            d = d2; P0 = P2; sd = st2.sd; hauteur.passes = passe + 1;
          }
          hauteur.apres = stat(P0); hauteur.cible = cible;
        }
      }
      // Une boucle : la fin se fond dans le début, et l'on coupe ce qui a servi au fondu.
      if(S.boucle){
        const N = Math.round(S.boucle/1000*S.hz), L = d.length, y = new Float32Array(L - N);
        for(let i = 0; i < L - N; i++) y[i] = i < N ? d[i]*(i/N) + d[L - N + i]*(1 - i/N) : d[i];
        d = y;
      }
      /* UN NIVEAU PLAT (`plat`) : une boucle de croisière doit être égale d'un bout à l'autre,
         et l'enregistrement ne l'est jamais tout à fait — le micro bouge, le vent passe. On
         mesure le niveau (RMS) par tranche de 50 ms, on le lisse sur un quart de seconde, et
         l'on ramène chaque tranche au niveau moyen, gain interpolé d'une tranche à l'autre,
         borné à ±6 dB. La hauteur, elle, n'est pas touchée. */
      let plat = null;
      if(S.plat){
        const T = Math.round(S.hz*0.05), nb = Math.floor(d.length/T), r = new Float32Array(nb);
        for(let k = 0; k < nb; k++){ let s = 0; for(let i = k*T; i < (k+1)*T; i++) s += d[i]*d[i]; r[k] = Math.sqrt(s/T); }
        const lisse = new Float32Array(nb);
        for(let k = 0; k < nb; k++){ let s = 0, c = 0; for(let j = -2; j <= 2; j++){ const kk = (k + j + nb) % nb; s += r[kk]; c++; } lisse[k] = s/c; }
        let moy = 0; for(let k = 0; k < nb; k++) moy += lisse[k]; moy /= nb;
        const gains = Array.from(lisse, (x)=> Math.max(0.5, Math.min(2, x > 0 ? moy/x : 1)));
        const y = new Float32Array(d.length);
        for(let i = 0; i < d.length; i++){
          const k = Math.min(nb - 1, Math.floor(i/T)), f = (i - k*T)/T, k2 = (k + 1) % nb;
          y[i] = d[i]*(gains[k]*(1 - f) + gains[k2]*f);
        }
        d = y;
        plat = {avant:+(100*Math.sqrt(Array.from(r).reduce((s, x)=> s + (x - moy)*(x - moy), 0)/nb)/moy).toFixed(1),
                apres:(()=>{ let s = 0, mm = 0; const rr = []; for(let k = 0; k < nb; k++){ let q = 0; for(let i = k*T; i < (k+1)*T; i++) q += d[i]*d[i]; rr.push(Math.sqrt(q/T)); mm += rr[k]; } mm /= nb; for(const x of rr) s += (x - mm)*(x - mm); return +(100*Math.sqrt(s/nb)/mm).toFixed(1); })()};
      }
      let crete = 0; for(let i = 0; i < d.length; i++) crete = Math.max(crete, Math.abs(d[i]));
      const g = crete > 0 ? (S.crete || 0.9)/crete : 1;
      // WAV 16 bits mono
      const w = new DataView(new ArrayBuffer(44 + d.length*2));
      const str = (o, s)=>{ for(let i = 0; i < s.length; i++) w.setUint8(o + i, s.charCodeAt(i)); };
      str(0, 'RIFF'); w.setUint32(4, 36 + d.length*2, true); str(8, 'WAVE'); str(12, 'fmt ');
      w.setUint32(16, 16, true); w.setUint16(20, 1, true); w.setUint16(22, 1, true);
      w.setUint32(24, S.hz, true); w.setUint32(28, S.hz*2, true); w.setUint16(32, 2, true); w.setUint16(34, 16, true);
      str(36, 'data'); w.setUint32(40, d.length*2, true);
      for(let i = 0; i < d.length; i++){ const v = Math.max(-1, Math.min(1, d[i]*g)); w.setInt16(44 + i*2, v < 0 ? v*32768 : v*32767, true); }
      let s = ''; const u = new Uint8Array(w.buffer); for(let i = 0; i < u.length; i++) s += String.fromCharCode(u[i]);
      return {b64:btoa(s), duree:+(d.length/S.hz).toFixed(3), sr0:buf.sampleRate, canaux:buf.numberOfChannels, crete0:+crete.toFixed(3), octets:u.length, plat:plat, hauteur:hauteur};
    }, [b64, S]);
    fs.writeFileSync(path.join(ICI, cle + '.b64'), r.b64);
    console.log(cle.padEnd(10), S.src.slice(0, 40).padEnd(42), r.sr0 + ' Hz ×' + r.canaux + ' → ' + S.hz + ' Hz mono', r.duree + ' s', Math.round(r.octets/1024) + ' Ko WAV,', Math.round(r.b64.length/1024) + ' Ko en base64', 'crête ' + r.crete0, r.plat ? 'niveau aplani : écart ' + r.plat.avant + ' % → ' + r.plat.apres + ' %' : '',
                r.hauteur ? '| hauteur ' + r.hauteur.avant.moy + ' Hz ±' + r.hauteur.avant.sd + ' % (' + r.hauteur.avant.debut + ' → ' + r.hauteur.avant.fin + ')'
                            + (r.hauteur.apres ? ' aplanie : ' + r.hauteur.apres.moy + ' Hz ±' + r.hauteur.apres.sd + ' % (' + r.hauteur.apres.debut + ' → ' + r.hauteur.apres.fin + ')' : '') : '');
  }
  await b.close();
})();
