# -*- coding: utf-8 -*-
"""LA PREUVE VISUELLE DU RECALAGE, parce qu un chiffre qui dit « 0,6 % » ne prouve rien
   tout seul : il peut aussi bien dire que la mesure se ment a elle-meme.
   La reference passe dans le canal rouge, l autre humeur dans les deux autres. Ce qui est
   sombre chez les deux devient gris ; ce qui n est sombre que chez l une ressort en couleur.
   Si le recalage dit vrai, l image de DROITE est grise partout sauf la ou les deux planches
   different VRAIMENT — la bouche, le pouce —, et celle de GAUCHE ne l est pas.

       python3 preuve.py laiterie fromagerie      # deux personnages, avant et apres
"""
import fabriquer as F, calage as K, aligner as A, numpy as np, sys
from PIL import Image, ImageDraw

def cadreDe(rgb, couv):
    im = Image.fromarray(np.clip(rgb,0,255).astype(np.uint8),'RGB')
    im.putalpha(Image.fromarray(np.clip(couv*255,0,255).astype(np.uint8))); return im

def superposer(R, C):
    r = np.asarray(R.convert('RGBA')).astype(np.float64)
    c = np.asarray(C.convert('RGBA')).astype(np.float64)
    gr = (0.299*r[:,:,0]+0.587*r[:,:,1]+0.114*r[:,:,2])*(r[:,:,3]/255.0) + 255*(1-r[:,:,3]/255.0)
    gc = (0.299*c[:,:,0]+0.587*c[:,:,1]+0.114*c[:,:,2])*(c[:,:,3]/255.0) + 255*(1-c[:,:,3]/255.0)
    out = np.stack([gr, gc, gc], -1)
    return Image.fromarray(np.clip(out,0,255).astype(np.uint8),'RGB')

C = F.cadres(); T = F.table()
cas = sys.argv[1:] or ['laiterie','supermarche','restaurant','boucherie']
vig = []
for rad in cas:
    hs = [h for h in F.HUMEURS if (rad+'-'+h) in C]
    R = cadreDe(*C[rad+'-'+hs[0]])
    for h in hs[1:]:
        Au = cadreDe(*C[rad+'-'+h])
        # ON PASSE PAR LA MESURE FINE, ET C EST LE PIEGE DE CETTE PLANCHE. Avec la passe
        # large de `calage.rapport` — 0,80 a 1,26 par pas de deux pour cent — la Laiterie
        # accroche un maximum secondaire a 1,28 : la preuve montrait alors un recalage qui
        # EMPIRE la superposition, sur des fiches pourtant deja alignees. Une planche de
        # preuve qui se trompe est pire que pas de planche du tout.
        s = A.mesureFine(R, Au)
        _, dx, dy, _ = K.rapport(R, Au, yYeux=F.YEUX_Y, echs=np.array([s]),
                                 dmax=6, pas=1, grille=A.FIN)
        W,H = Au.size; P = (W/2.0, F.YEUX_Y*H)
        n = Au.resize((max(1,int(round(W*s))), max(1,int(round(H*s)))), Image.LANCZOS)
        ox = int(round(P[0]-P[0]*s+dx*W)); oy = int(round(P[1]-P[1]*s+dy*H))
        B = Image.new('RGBA',(W,H),(0,0,0,0)); B.paste(n,(ox,oy),n)
        vig.append(('%s %s>%s  s=%.3f' % (rad,hs[0][:3],h[:3],s), superposer(R,Au), superposer(R,B)))
cw,ch = 192,240
im = Image.new('RGB',(len(vig)*(2*cw+16)+16, ch+30),(246,242,234)); d=ImageDraw.Draw(im)
for i,(t,av,ap) in enumerate(vig):
    x = 16+i*(2*cw+16)
    im.paste(av,(x,26)); im.paste(ap,(x+cw+4,26)); d.text((x,8), t, fill=(80,64,48))
S='/tmp/claude-0/-home-user-Farming/3c255efa-fd9f-5aab-a574-54544179bd6d/scratchpad'
im.save(S+'/_preuve.png'); print(im.size)
