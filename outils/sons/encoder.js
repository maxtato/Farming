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
      const d = out.getChannelData(0);
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
      return {b64:btoa(s), duree:+out.duration.toFixed(3), sr0:buf.sampleRate, canaux:buf.numberOfChannels, crete0:+crete.toFixed(3), octets:u.length};
    }, [b64, S]);
    fs.writeFileSync(path.join(ICI, cle + '.b64'), r.b64);
    console.log(cle.padEnd(10), S.src.slice(0, 40).padEnd(42), r.sr0 + ' Hz ×' + r.canaux + ' → ' + S.hz + ' Hz mono', r.duree + ' s', Math.round(r.octets/1024) + ' Ko WAV,', Math.round(r.b64.length/1024) + ' Ko en base64', 'crête ' + r.crete0);
  }
  await b.close();
})();
