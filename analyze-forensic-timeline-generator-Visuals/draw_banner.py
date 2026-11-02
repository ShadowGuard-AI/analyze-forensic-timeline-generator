#!/usr/bin/env python3
"""analyze-forensic-timeline-generator banner: farmyard in the last hour before a summer storm, light
gone copper at the edges. Salesman's cart beside a barn with one blackened gable. Sample case open on
the cart tailboard at centre, rods catching strange light, a second rod fully assembled on trestles,
longer than two men, orange ball finial, tip pointed at a sky filling the upper half, stratosphere
blue down to bruised grey. Weather vane arrow and running horse on the barn roof mid turn. Farmhouse
roof behind with an older rod, cable, and earth plate in one traceable line. Route papers and a framed
barometer, needle falling, on the cart seat: ruled columns forming no words. Title stencilled inside
the open case lid in Averia Gruesa Libre, cream on grey lining, one inscription only."""
import math, random, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
random.seed(881)
V1 = "--v1" in sys.argv
W, H = 1200, 520
GREY = (90, 90, 88); CREAM = (243, 234, 214); ORANGE = (217, 123, 46); BLUE = (46, 95, 138); RED = (179, 49, 42)
img = Image.new("RGB", (W, H), BLUE); d = ImageDraw.Draw(img, "RGBA")
HERE = __file__.rsplit("/", 1)[0]
# sky fills the upper half
for y in range(0, 262):
    t = y / 262; col = tuple(int(BLUE[i] + ((124, 114, 110)[i] - BLUE[i]) * t * t) for i in range(3))
    d.line([(0, y), (W, y)], fill=col)
for i in range(30):  # copper at the edges
    x = random.choice([random.uniform(0, 180), random.uniform(1020, 1200)]); y = random.uniform(120, 256)
    d.ellipse([x - 46, y - 13, x + 46, y + 13], fill=(220, 142, 70, 55))
# distant rain sheet under one cloud, no lightning
d.ellipse([60, 168, 300, 214], fill=(96, 100, 108))
for i in range(24):
    x = 84 + i * 8; d.line([(x, 212), (x - 10, 272)], fill=(170, 182, 196, 110), width=2)
# field, fence, water pump, wash lines in the middle ground
d.rectangle([0, 262, W, H], fill=(112, 116, 72))
for x in (40, 260, 500, 760, 1020):
    d.rectangle([x, 292, x + 8, 330], fill=(96, 74, 50))
d.line([(0, 304), (W, 298)], fill=(110, 86, 58), width=4)
d.line([(952, 330), (952, 386)], fill=(70, 74, 78), width=7); d.line([(952, 344), (986, 330)], fill=(70, 74, 78), width=6); d.ellipse([944, 384, 960, 394], fill=(70, 74, 78))  # pump
d.line([(420, 316), (560, 310)], fill=(60, 56, 50), width=3)
d.rectangle([446, 312, 482, 356], fill=CREAM); d.rectangle([508, 310, 542, 348], fill=(200, 208, 216))
# barn left, blackened gable, vane arrow and running horse mid turn
d.rectangle([70, 282, 360, 408], fill=(128, 84, 58))
d.polygon([(54, 284), (215, 204), (376, 284)], fill=(104, 66, 44))
d.polygon([(272, 240), (376, 284), (360, 284), (284, 250)], fill=(26, 22, 20))
d.line([(215, 204), (215, 168)], fill=(40, 38, 36), width=4)
d.line([(188, 176), (246, 170)], fill=(52, 50, 48), width=4); d.polygon([(246, 170), (228, 164), (230, 178)], fill=(52, 50, 48))  # arrow
d.ellipse([196, 152, 228, 164], fill=(52, 50, 48)); d.polygon([(222, 154), (236, 146), (234, 158)], fill=(52, 50, 48))  # running horse, crude silhouette
# farmhouse behind right with the finished promise: rod, cable, earth plate in one line
d.rectangle([880, 268, 1130, 392], fill=(214, 204, 178))
d.polygon([(866, 270), (1005, 214), (1144, 270)], fill=(92, 80, 70))
d.line([(1005, 214), (1005, 178)], fill=(60, 60, 62), width=4); d.ellipse([999, 170, 1011, 182], fill=ORANGE)
d.line([(1018, 232), (1018, 378)], fill=(70, 70, 72), width=3); d.rectangle([1008, 378, 1028, 388], fill=(70, 70, 72))
# cart at centre: wheels, tailboard, seat with route papers and framed barometer
d.rectangle([430, 356, 800, 382], fill=(110, 82, 52))
d.ellipse([452, 382, 522, 452], outline=(70, 52, 34), width=9); d.ellipse([700, 382, 770, 452], outline=(70, 52, 34), width=9)
d.rectangle([452, 322, 560, 356], fill=(122, 92, 56))  # cart seat
d.polygon([(462, 330), (540, 324), (546, 348), (468, 352)], fill=CREAM)  # route papers: ruled columns, no words
for i in range(4):
    d.line([(474 + i * 17, 328), (478 + i * 17, 350)], fill=(150, 150, 158), width=2)
for r in range(3):
    d.line([(468, 334 + r * 6), (542, 330 + r * 6)], fill=(170, 172, 178), width=1)
d.rectangle([566, 318, 622, 356], outline=(96, 70, 42), width=5)  # barometer in wooden frame, needle falling
d.ellipse([574, 324, 614, 352], fill=CREAM); d.line([(594, 338), (582, 330)], fill=(50, 46, 42), width=2)
# assembled rod on trestles, longer than two men, tip pointed at the sky
d.line([(806, 300), (1136, 196)], fill=(216, 220, 224), width=6)
d.ellipse([880, 268, 898, 286], fill=ORANGE)  # ball finial along the shaft
d.polygon([(1136, 196), (1116, 200), (1130, 210)], fill=(216, 220, 224))
for tx in (850, 1060):
    d.line([(tx, 330), (tx + 18, 286)], fill=(96, 70, 44), width=6); d.line([(tx + 36, 330), (tx + 18, 286)], fill=(96, 70, 44), width=6)
# sample case open on the tailboard at centre, lid facing viewer, stencil inside the lid
d.polygon([(540, 236), (778, 236), (766, 330), (552, 330)], fill=(116, 116, 112))
d.polygon([(552, 248), (766, 248), (758, 320), (560, 320)], fill=(130, 128, 122))
d.rectangle([536, 330, 782, 392], fill=GREY); d.rectangle([536, 384, 782, 392], fill=RED)
for i, ln in enumerate([52, 42, 32]):
    x = 596 + i * 52; d.line([(x, 380), (x, 380 - ln)], fill=(216, 220, 224), width=4); d.ellipse([x - 6, 380 - ln - 12, x + 6, 380 - ln], fill=ORANGE)
if V1:  # flaw: title painted on the barn wall as a sign instead of stencilled inside the lid
    f = ImageFont.truetype(HERE + "/fonts/AveriaGruesaLibre.ttf", 17)
    d.text((76, 292), "analyze-forensic-timeline-generator", font=f, fill=CREAM)
else:
    f = ImageFont.truetype(HERE + "/fonts/AveriaGruesaLibre.ttf", 11)
    t = "analyze-forensic-timeline-generator"
    tw = d.textlength(t, font=f); d.text((659 - tw / 2, 276), t, font=f, fill=CREAM)
img = img.filter(ImageFilter.GaussianBlur(0.4))
out = "scratch/banner-v1.png" if V1 else "banner.png"
img.save(HERE + "/" + out); print("saved", out)
