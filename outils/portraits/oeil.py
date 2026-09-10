# -*- coding: utf-8 -*-
"""L ECART INTER-OCULAIRE, MESURE DANS LA BOITE DE VISAGE.
   Le detecteur de visage de Haar mord huit fois sur dix, mais la boite qu il rend est
   tantot le visage seul, tantot toute la tete : elle situe, elle ne mesure pas. On s en
   sert donc comme d une REGION DE RECHERCHE, et l on y cherche les deux yeux — qui, eux,
   se mesurent. L ecart entre leurs centres donne l echelle, leur milieu donne le centre
   et la hauteur. C est la normalisation classique du portrait, et la seule qui donne la
   meme taille de visage a un homme en casquette et a une femme a la coiffure volumineuse."""
import numpy as np, cv2
from PIL import Image

_EYE = None
def _eye():
    global _EYE
    if _EYE is None:
        d = cv2.data.haarcascades
        _EYE = [cv2.CascadeClassifier(d+'haarcascade_eye.xml'),
                cv2.CascadeClassifier(d+'haarcascade_eye_tree_eyeglasses.xml')]
    return _EYE

def yeuxDans(g, boite):
    """Cherche les yeux dans le tiers superieur-median de la boite de visage."""
    x, y, w, h = boite
    y0 = int(y + 0.10*h); y1 = int(y + 0.68*h)
    x0 = int(x - 0.08*w); x1 = int(x + 1.08*w)
    H, W = g.shape
    x0, x1 = max(0, x0), min(W, x1); y0, y1 = max(0, y0), min(H, y1)
    if x1-x0 < 12 or y1-y0 < 8: return []
    z = cv2.equalizeHist(g[y0:y1, x0:x1])
    vus = []
    for c in _eye():
        for ech in (1.03, 1.08, 1.15):
            for (a, b, u, v) in c.detectMultiScale(z, ech, 3,
                                                   minSize=(max(6,int(w*0.07)), max(4,int(w*0.05))),
                                                   maxSize=(int(w*0.55), int(w*0.55))):
                vus.append((x0+a+u/2.0, y0+b+v/2.0, u, v))
    return vus

def fusionner(vus, w):
    """Les cascades rendent plusieurs boites par oeil : on regroupe ce qui se touche."""
    grp = []
    for p in sorted(vus, key=lambda t: -t[2]*t[3]):
        for g in grp:
            if abs(g[0][0]-p[0]) < w*0.10 and abs(g[0][1]-p[1]) < w*0.08: g.append(p); break
        else: grp.append([p])
    return [(float(np.mean([q[0] for q in g])), float(np.mean([q[1] for q in g])),
             float(np.mean([q[2] for q in g])), len(g)) for g in grp]

def reperes(im, boite):
    """Rend (ecart, cx, cy) ou None. `boite` = la boite de visage de Haar."""
    g = cv2.cvtColor(np.asarray(im.convert('RGB')), cv2.COLOR_RGB2GRAY)
    x, y, w, h = boite
    c = fusionner(yeuxDans(g, boite), w)
    if len(c) < 2: return None
    best = None
    for i in range(len(c)):
        for j in range(i+1, len(c)):
            A, B = (c[i], c[j]) if c[i][0] < c[j][0] else (c[j], c[i])
            dx = B[0]-A[0]; dy = abs(B[1]-A[1])
            if dx < w*0.18 or dx > w*0.85: continue
            if dy > 0.28*dx: continue
            r = A[2]/max(B[2], 1e-6)
            if r < 0.55 or r > 1.8: continue
            note = (A[3]+B[3]) + (1-dy/max(dx,1))*3 + (1-abs(1-r))*2
            if best is None or note > best[0]: best = (note, dx, (A[0]+B[0])/2, (A[1]+B[1])/2)
    if best is None: return None
    return dict(ecart=best[1], cx=best[2], cy=best[3])
