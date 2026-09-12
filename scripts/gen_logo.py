#!/usr/bin/env python3
from PIL import Image, ImageDraw

img = Image.new("RGBA", (512, 512), (5, 9,  18,  255))
d = ImageDraw.Draw(img)
d.rounded_rectangle((40, 40,  472,  472), radius=100, fill=(10,  14,  24))
d.ellipse((140,  140,372,372), fill=(99,102,241))
d.ellipse((156,  156,356,356), fill=(79,70,229))
d.polygon([(262,150), (348,160), (310,216), (330,256), (348,302), (306,296), (280,252), (250,222), (254,180)], fill=(245,247,252))
d.line([(252,140), (330,150)], fill=(255,255,255,120), width=8)
d.arc((96,128,384,416), start=220, end=410, fill=(255,255,255,60), width=6)
d.line([(170,110), (230,122)], fill=(255,255,255,90), width=6)
d.line([(150,128), (205,138)], fill=(255,255,255,70), width=5)
img.save("/workspace/project/Autopilot/autopilot.png")
print("done")