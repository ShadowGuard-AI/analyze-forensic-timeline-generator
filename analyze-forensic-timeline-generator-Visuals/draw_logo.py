#!/usr/bin/env python3
"""analyze-forensic-timeline-generator logo: open sample case from the front at a slight angle, lid
thrown back, fitted interior facing the viewer. Panel grey leather over wood, darker corner hide,
two brass latches hanging open. Inside in strict order: three lightning rods of graduated length in
bright metal with desert dusk orange ball finials, a copper weather vane arrow laid flat across the
lower compartment, a round barometer dial set into the lid lining, needle into the fair sector.
Warning red once only, a thin stripe along the case bottom edge. Name in Averia Gruesa Libre below."""
import math, sys
from PIL import Image, ImageDraw, ImageFont
V1 = "--v1" in sys.argv
W, H = 980, 680
GREY = (90, 90, 88); CREAM = (243, 234, 214); ORANGE = (217, 123, 46); RED = (179, 49, 42); DARK = (30, 30, 30)
img = Image.new("RGB", (W, H), CREAM); d = ImageDraw.Draw(img, "RGBA")
HERE = __file__.rsplit("/", 1)[0]
font = ImageFont.truetype(HERE + "/fonts/AveriaGruesaLibre.ttf", 31)
# lid thrown back: lining panel above, tilted
d.polygon([(190, 66), (790, 66), (756, 252), (224, 252)], fill=(112, 112, 108))
d.polygon([(214, 88), (766, 88), (740, 234), (240, 234)], fill=(128, 126, 120))
# barometer dial set into the lid lining, face cream, needle into the fair sector, tick marks only
d.ellipse([556, 104, 692, 226], fill=CREAM, outline=(64, 60, 54), width=4)
for k in range(9):
    a = 3.6 + k * 0.32; d.line([(624 + math.cos(a) * 48, 165 + math.sin(a) * 48), (624 + math.cos(a) * 56, 165 + math.sin(a) * 56)], fill=DARK, width=3)
d.line([(624, 165), (660, 138)], fill=DARK, width=4); d.ellipse([618, 159, 630, 171], fill=DARK)
# case body: fitted interior facing the viewer
d.polygon([(170, 252), (810, 252), (842, 512), (138, 512)], fill=GREY)
d.polygon([(196, 276), (784, 276), (806, 488), (174, 488)], fill=(104, 104, 100))
for x, y in [(196, 276), (762, 276), (180, 466), (784, 466)]:  # corner reinforcements in darker hide
    d.polygon([(x, y), (x + 34, y), (x, y + 30)], fill=(58, 58, 56))
# three rods of graduated length, bright metal, orange ball finials; draft 1 keeps them short and dim
lengths = [86, 74, 62] if V1 else [176, 148, 120]
metal = (150, 152, 150) if V1 else (216, 220, 224)
for i, ln in enumerate(lengths):
    x = 320 + i * 110; base = 452
    d.line([(x, base), (x, base - ln)], fill=metal, width=8)
    d.polygon([(x - 6, base - ln), (x + 6, base - ln), (x, base - ln - 20)], fill=metal)  # tip above the ball on the longest reading: finial ball below tip
    d.ellipse([x - 13, base - ln + 8, x + 13, base - ln + 34], fill=ORANGE, outline=(168, 92, 30))
    d.line([(x - 20, base - 56), (x + 20, base - 56)], fill=(66, 58, 44), width=6)  # holding loop
    d.line([(x - 20, base - 118 if ln > 118 else base - 60), (x + 20, base - 118 if ln > 118 else base - 60)], fill=(66, 58, 44), width=6)
# copper weather vane arrow laid flat across the lower compartment
d.line([(250, 470), (720, 470)], fill=(176, 108, 54), width=7)
d.polygon([(720, 470), (682, 456), (682, 484)], fill=(176, 108, 54))
d.polygon([(250, 470), (296, 450), (296, 470)], fill=(176, 108, 54)); d.polygon([(250, 470), (296, 490), (296, 470)], fill=(176, 108, 54))  # forked tail, one head only
# two brass latches hanging open below the front edge
for x in (330, 610):
    d.rectangle([x, 512, x + 40, 534], fill=(196, 158, 62)); d.rectangle([x + 6, 534, x + 34, 562], outline=(160, 126, 48), width=5)
# warning red once only: thin stripe along the case bottom edge
d.rectangle([138, 500, 842, 512], fill=RED)
name = "analyze-forensic-timeline-generator"
tw = d.textlength(name, font=font); d.text(((W - tw) / 2, 592), name, font=font, fill=(26, 26, 26))
out = "scratch/logo-v1.png" if V1 else "logo.png"
img.save(HERE + "/" + out)
if not V1:
    img.resize((64, 44)).save(HERE + "/scratch/logo64-ship.png")
print("saved", out)
