# -*- coding: utf-8 -*-
"""LA PLANCHE DE VERIFICATION, EN UN SEUL FICHIER HTML.

    python3 planche.py            # ecrit verifier.html a la racine du depot

Le joueur : « genere-moi un fichier HTML, on voit une fenetre avec la tete de chacun des
perso que je puisse verifier. » Une planche PNG ne suffit pas pour juger du pixel art : il
faut pouvoir la voir A LA TAILLE OU LE JEU L AFFICHE — 192 sur l ecran de gain, 96 dans la
fenetre de contrat, 64 au guichet — et aussi au point pres, pour compter les pixels.

TROIS PARTIS PRIS.

  1. LES IMAGES SONT DANS LE FICHIER, en base 64. Une page qui pointe vers `portraits/` ne
     marche que depuis le depot ; celle-ci s ouvre depuis n importe ou, se transfere par
     message et se regarde sur un telephone. Elle pese ce que pesent les fiches plus un
     tiers, et c est le prix de cette independance.
  2. LE FOND EST CELUI DU JEU. Un portrait detoure juge sur du blanc ment : les liserés
     clairs disparaissent et les sombres crient. On offre les deux fonds ou le jeu les
     pose vraiment — le voile sombre de l ecran de gain, le papier creme de la fenetre de
     contrat — plus un damier pour voir la transparence elle-meme.
  3. LES TAILLES SONT CELLES DU JEU, ET AUCUNE AUTRE. Pas de curseur libre : les fiches
     sont dessinees pour tomber juste a 384, 192, 96 et 64, et un affichage a 137 pixels
     ne dirait rien de ce qu on verra.
"""
import base64, json, os, sys
from collections import Counter
from PIL import Image

ICI = os.path.dirname(os.path.abspath(__file__))
JEU = os.path.abspath(os.path.join(ICI, '..', '..'))
HUMEURS = [('neutre', 'neutre', 'propose la mission'),
           ('bravo', 'pouce levé', 'mission remplie'),
           ('refus', 'refus', 'étal plein')]

def table():
    return json.load(open(os.path.join(ICI, 'commerces.json')))

def fiche(rad, h, jeu=True):
    d = os.path.join(JEU, 'portraits') if jeu else os.path.join(ICI, 'attente')
    f = os.path.join(d, rad + '-' + h + '.png')
    return f if os.path.exists(f) else None

def mesurer(f):
    im = Image.open(f).convert('RGBA')
    a = im.split()[3].point(lambda v: 255 if v > 127 else 0)
    px = list(im.convert('RGB').getdata())
    op = [p for p, m in zip(px, a.getdata()) if m]
    return dict(l=im.width, h=im.height, ko=os.path.getsize(f)/1024.0,
                teintes=len(set(op)), opaque=len(op),
                b64=base64.b64encode(open(f, 'rb').read()).decode('ascii'))

def ecrire(sortie=None):
    sortie = sortie or os.path.join(JEU, 'verifier.html')
    T = table()
    pal = json.load(open(os.path.join(ICI, 'palette.json')))
    lignes, tot, nb = [], 0, 0
    for rad in sorted(T, key=lambda r: (T[r].get('site') or 'zz').lower()):
        jeu = bool(T[rad].get('site'))
        nom = T[rad].get('site') or (rad + ' — en attente')
        cases = []
        for h, lab, quand in HUMEURS:
            f = fiche(rad, h, jeu)
            if not f:
                cases.append('<div class="vig"><div class="case vide">'
                             '<span>sans objet</span></div></div>')
                continue
            m = mesurer(f); tot += m['ko']; nb += 1
            # LA LEGENDE EST HORS DE LA BOITE, ET IL A FALLU LA PLANCHE POUR LE VOIR.
            # Dedans, elle heritait du fond sombre du jeu et s ecrivait en brun sur
            # anthracite : illisible, et collee au buste par-dessus le marche.
            cases.append(
              '<div class="vig"><div class="case">'
              '<img src="data:image/png;base64,' + m['b64'] + '" alt=""></div>'
              '<div class="sous"><b>' + lab + '</b><span>' + quand + '</span>'
              '<span class="chiffres">' + str(m['l']) + '×' + str(m['h']) + ' · '
              + str(m['teintes']) + ' teintes · ' + ('%.1f' % m['ko']) + ' Ko</span></div></div>')
        lignes.append('<section class="perso' + ('' if jeu else ' attente') + '">'
                      '<h2>' + nom + '</h2><div class="trio">' + ''.join(cases) + '</div></section>')

    nuancier = ''.join(
        '<div class="gam">' + ''.join(
            '<i style="background:rgb(%d,%d,%d)" title="%d,%d,%d"></i>' % tuple(pal['couleurs'][c]*2)
            for c in g) + '</div>'
        for g in pal['gammes'] if g)

    html = MODELE.replace('@@LIGNES@@', ''.join(lignes)) \
                 .replace('@@NUANCIER@@', nuancier) \
                 .replace('@@N@@', str(nb)) \
                 .replace('@@KO@@', '%.0f' % tot) \
                 .replace('@@COUL@@', str(len(pal['couleurs']))) \
                 .replace('@@GAM@@', str(sum(1 for g in pal['gammes'] if g)))
    open(sortie, 'w', encoding='utf-8').write(html)
    print('->', sortie, '%.0f Ko' % (os.path.getsize(sortie)/1024.0), '·', nb, 'fiches')

MODELE = r"""<!doctype html>
<html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Portraits — planche de vérification</title>
<style>
  :root{
    --pap1:#F6F0DF; --pap2:#F1E9D4; --ligne:#E4DAC0; --ligneOmb:#C9BE9E;
    --titreC:#2F5233; --texte:#4A4636; --sous:#7C7458;
    --or:#E8B33A; --orOmb:#B4861A; --vert:#5C8C3F; --jeu:#202326;
    --titre:"Haettenschweiler","Arial Narrow","Impact",sans-serif;
    --corps:"Trebuchet MS",Verdana,system-ui,sans-serif;
    --taille:192px; --hauteur:240px;
  }
  *{box-sizing:border-box}
  body{margin:0;background:var(--jeu);color:var(--pap1);font-family:var(--corps);
       -webkit-text-size-adjust:100%}
  header{position:sticky;top:0;z-index:5;background:rgba(24,27,30,.96);
         border-bottom:1px solid rgba(255,255,255,.10);padding:14px 18px 12px;
         backdrop-filter:blur(6px)}
  h1{font-family:var(--titre);font-weight:400;letter-spacing:.06em;margin:0 0 2px;
     font-size:26px;color:var(--or)}
  .info{color:#9AA3A9;font-size:12.5px;margin-bottom:10px}
  .barre{display:flex;flex-wrap:wrap;gap:16px}
  .grp{display:flex;align-items:center;gap:6px}
  .grp>span{font-size:11px;letter-spacing:.10em;text-transform:uppercase;color:#7C858B;
            margin-right:2px}
  button{font:inherit;font-size:12.5px;padding:5px 11px;border:0;border-radius:8px;
         background:#31363B;color:#D6DBDF;cursor:pointer}
  button.on{background:var(--or);color:#2A2411;font-weight:bold}
  main{padding:18px;display:grid;gap:18px;
       grid-template-columns:repeat(auto-fill,minmax(min(100%,var(--carte)),1fr))}
  .perso{background:var(--pap1);border-radius:14px;padding:12px 14px 14px;
         box-shadow:0 6px 0 rgba(0,0,0,.28)}
  .perso.attente{background:#EDE6D2;outline:2px dashed #C6B893;outline-offset:-6px}
  h2{font-family:var(--titre);font-weight:400;font-size:19px;letter-spacing:.05em;
     color:var(--titreC);margin:0 0 10px;text-transform:uppercase}
  .trio{display:flex;gap:10px;align-items:flex-end;flex-wrap:wrap}
  .vig{display:flex;flex-direction:column}
  .case{position:relative}
  .case img{display:block;width:var(--taille);height:var(--hauteur);object-fit:contain;
            object-position:bottom center;image-rendering:pixelated}
  body.lisse .case img{image-rendering:auto}
  /* LE FOND EST CELUI DU JEU, parce qu un portrait detoure juge sur du blanc ment. */
  body.fjeu .case{background:#2A2E31}
  body.fpapier .case{background:var(--ligne)}
  body.fdamier .case{background-image:
      linear-gradient(45deg,#C9BE9E 25%,transparent 25%,transparent 75%,#C9BE9E 75%),
      linear-gradient(45deg,#C9BE9E 25%,transparent 25%,transparent 75%,#C9BE9E 75%);
    background-size:16px 16px;background-position:0 0,8px 8px;background-color:var(--pap2)}
  .case{border-radius:8px;overflow:hidden}
  /* LA LIGNE DES YEUX, a 0,318 de la hauteur : c est la cote sur laquelle tout le casting
     est cadre, et la seule facon de verifier d un coup d oeil que les trois humeurs d un
     personnage sont bien au meme endroit. */
  body.yeux .case::after{content:"";position:absolute;left:0;right:0;top:31.8%;
    height:1px;background:rgba(214,90,60,.85);pointer-events:none}
  .sous{margin-top:5px;display:flex;flex-direction:column;line-height:1.35;
        width:var(--taille)}
  .sous b{font-size:12px;color:var(--texte);text-transform:uppercase;letter-spacing:.05em}
  .sous span{font-size:11px;color:var(--sous)}
  .chiffres{font-variant-numeric:tabular-nums}
  .vide{width:var(--taille);height:var(--hauteur);display:grid;place-items:center;
        border:1px dashed #CFC3A4;color:#B2A98F;font-size:11px;background:none!important;
        box-sizing:border-box}
  .pal{padding:0 18px 26px}
  .pal h3{font-family:var(--titre);font-weight:400;letter-spacing:.06em;color:var(--or);
          font-size:16px;margin:0 0 8px;text-transform:uppercase}
  .gam{display:flex;gap:2px;margin-bottom:3px}
  .gam i{width:34px;height:22px;border-radius:3px;display:block}
  @media (max-width:520px){ .trio{gap:6px} main{padding:10px} }
</style></head>
<body class="fjeu">
<header>
  <h1>Portraits — planche de vérification</h1>
  <div class="info">@@N@@ fiches · @@KO@@ Ko · palette de @@COUL@@ couleurs en @@GAM@@ gammes,
    partagée par tout le casting</div>
  <div class="barre">
    <div class="grp"><span>Taille</span>
      <button data-t="64">64</button><button data-t="96">96</button>
      <button data-t="192" class="on">192</button><button data-t="384">384 · 1:1</button>
      <button data-t="768">768 · 2:1</button></div>
    <div class="grp"><span>Fond</span>
      <button data-f="fjeu" class="on">jeu</button>
      <button data-f="fpapier">papier</button>
      <button data-f="fdamier">damier</button></div>
    <div class="grp"><span>Rendu</span>
      <button data-r="pix" class="on">pixels francs</button>
      <button data-r="lisse">lissé</button></div>
    <div class="grp"><span>Repères</span>
      <button data-y="1">ligne des yeux</button></div>
  </div>
</header>
<main>@@LIGNES@@</main>
<div class="pal"><h3>La palette</h3>@@NUANCIER@@</div>
<script>
  var R = document.documentElement, B = document.body;
  function poser(t){
    R.style.setProperty('--taille', t + 'px');
    R.style.setProperty('--hauteur', Math.round(t*1.25) + 'px');
    R.style.setProperty('--carte', (t*3 + 60) + 'px');
  }
  poser(192);
  function seul(g, b){ g.forEach(function(x){ x.classList.toggle('on', x === b); }); }
  document.querySelectorAll('[data-t]').forEach(function(b){
    b.onclick = function(){ poser(+b.dataset.t);
      seul([].slice.call(document.querySelectorAll('[data-t]')), b); }; });
  document.querySelectorAll('[data-f]').forEach(function(b){
    b.onclick = function(){ B.classList.remove('fjeu','fpapier','fdamier');
      B.classList.add(b.dataset.f);
      seul([].slice.call(document.querySelectorAll('[data-f]')), b); }; });
  document.querySelectorAll('[data-r]').forEach(function(b){
    b.onclick = function(){ B.classList.toggle('lisse', b.dataset.r === 'lisse');
      seul([].slice.call(document.querySelectorAll('[data-r]')), b); }; });
  document.querySelector('[data-y]').onclick = function(){
    B.classList.toggle('yeux'); this.classList.toggle('on', B.classList.contains('yeux')); };
</script>
</body></html>
"""

if __name__ == '__main__':
    ecrire(sys.argv[1] if len(sys.argv) > 1 else None)
