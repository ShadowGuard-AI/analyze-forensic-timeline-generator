#!/usr/bin/env python3
"""analyze-forensic-timeline-generator intro: farmyard and sky alone, no inscription of any kind.
Cart tailboard close in front with the sample case open, rods in loops, finial balls catching copper
light, leather gloves beside it, assembled rod edge entering from the right with tip out of view.
Barn with blackened gable midground, vane turned three quarters away, farmhouse beyond with its older
rod and cable in one clean vertical line, wash hanging heavy and still. Sky fills the top half,
stratosphere blue down to bruised grey, one distant sheet of rain, no lightning anywhere."""
import math, random, sys
from PIL import Image, ImageDraw, ImageFilter
random.seed(724)
V1 = "--v1" in sys.argv
W, H = 1200, 520
GREY = (90, 90, 88); CREAM = (243, 234, 214); ORANGE = (217, 123, 46); BLUE = (46, 95, 138); RED = (179, 49, 42)
img = Image.new("RGB", (W, H), BLUE); d = ImageDraw.Draw(img, "RGBA")
# sky occupying the top half: stratosphere blue high, grey and orange quarrelling at the edges
for y in range(0, 262):
    t = y / 262
    col = tuple(int(BLUE[i] + ((128, 118, 112)[i] - BLUE[i]) * t * t) for i in range(3))
    d.line([(0, y), (W, y)], fill=col)
for side in (0, W):
    for i in range(26):
        x = side + random.uniform(-160, 160); y = random.uniform(150, 258)
        d.ellipse([x - 40, y - 12, x + 40, y + 12], fill=(217, 140, 70, 60))
# one distant sheet of rain under one cloud, far right
d.ellipse([880, 178, 1120, 226], fill=(96, 100, 108))
for i in range(30):
    x = 900 + i * 7; d.line([(x, 224), (x - 12, 292)], fill=(170, 182, 196, 120), width=2)
# field and fence to a low horizon, one stand of trees darker than the sky
d.rectangle([0, 262, W, 330], fill=(116, 122, 74))
if not V1:
    d.rectangle([0, 330, W, H], fill=(124, 106, 70))  # yard ground below the field band; draft 1 left sky showing through here
for x in (60, 300, 560, 820, 1080):
    d.rectangle([x, 286, x + 8, 322], fill=(96, 74, 50))
d.line([(0, 296), (W, 290)], fill=(110, 86, 58), width=4)
for i in range(7):
    d.ellipse([140 + i * 26, 218 - (i % 3) * 14, 196 + i * 26, 268], fill=(40, 56, 38))
# barn midground left with its blackened gable, vane turned three quarters away on the roof
d.rectangle([90, 268, 400, 392], fill=(128, 84, 58))
d.polygon([(74, 270), (245, 188), (416, 270)], fill=(104, 66, 44))
d.polygon([(300, 226), (416, 270), (400, 270), (316, 238)], fill=(26, 22, 20))  # blackened gable end, older strike
d.line([(245, 188), (245, 158)], fill=(40, 38, 36), width=4)
d.polygon([(245, 158), (276, 166), (245, 172)], fill=(52, 50, 48))  # vane arrow, three quarters away
# farmhouse beyond, older rod installation in a clean vertical line a child could trace
d.rectangle([700, 276, 930, 384], fill=(214, 204, 178))
d.polygon([(686, 278), (815, 224), (944, 278)], fill=(92, 80, 70))
d.line([(815, 224), (815, 190)], fill=(60, 60, 62), width=4); d.ellipse([809, 182, 821, 194], fill=ORANGE)
d.line([(828, 240), (828, 372)], fill=(70, 70, 72), width=3)  # cable down the wall
d.rectangle([818, 372, 838, 382], fill=(70, 70, 72))  # earth plate at the foundation
# wash line hanging heavy and barely moving
d.line([(452, 300), (664, 292)], fill=(60, 56, 50), width=3)
for x, ln, col in [(472, 52, CREAM), (530, 60, (196, 204, 214)), (596, 48, (226, 218, 200))]:
    d.rectangle([x, 296, x + 42, 296 + ln], fill=col)
# cart tailboard close in front, lower right
d.polygon([(560, 420), (W, 398), (W, H), (520, H)], fill=(110, 82, 52))
for i in range(6):
    d.line([(580 + i * 110, 416 - i * 3), (560 + i * 110, H)], fill=(84, 60, 38), width=4)
# sample case open on the tailboard: lid thrown back, rods in loops, finial balls catching copper light
d.polygon([(700, 330), (960, 322), (946, 404), (714, 412)], fill=GREY)  # lid lining facing up
d.rectangle([690, 404, 972, 478], fill=(104, 104, 100)); d.rectangle([690, 404, 972, 478], outline=(64, 64, 62), width=4)
d.rectangle([690, 470, 972, 478], fill=RED)  # the one warning red stripe, case bottom edge
for i, ln in enumerate([64, 52, 40]):  # graduated rods held in loops
    x = 736 + i * 62
    d.line([(x, 462), (x, 462 - ln)], fill=(206, 210, 214), width=5)
    d.ellipse([x - 8, 462 - ln - 16, x + 8, 462 - ln], fill=ORANGE)
    d.line([(x - 14, 430), (x + 14, 430)], fill=(70, 60, 44), width=4)  # loop
# barometer in the lid lining, face cream, needle falling, no numerals anywhere
d.ellipse([852, 336, 922, 392], fill=CREAM, outline=(70, 62, 50), width=3)
d.line([(887, 364), (866, 348)], fill=(50, 46, 42), width=3)
# leather gloves laid beside the case
for gx in (596, 640):
    d.ellipse([gx, 448, gx + 34, 490], fill=(140, 102, 62)); d.rectangle([gx + 4, 428, gx + 30, 456], fill=(140, 102, 62))
    for f in range(4):
        d.rectangle([gx + 3 + f * 8, 416, gx + 8 + f * 8, 434], fill=(140, 102, 62))
# assembled rod on trestles entering from the right, tip out of view
d.line([(W, 452), (986, 470)], fill=(206, 210, 214), width=6)
d.ellipse([972, 460, 990, 478], fill=ORANGE)
img = img.filter(ImageFilter.GaussianBlur(0.4))
out = "scratch/intro-v1.png" if V1 else "intro-banner.png"
img.save(__file__.rsplit("/", 1)[0] + "/" + out); print("saved", out)
