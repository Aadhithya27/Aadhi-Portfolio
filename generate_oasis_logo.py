from PIL import Image, ImageDraw, ImageFont
import math
import os

width, height = 1000, 650
image = Image.new("RGB", (width, height), (255, 255, 255))
draw = ImageDraw.Draw(image)

center_x, center_y = 500, 240
radius = 120

# Draw Blue Sphere
for r in range(radius, 0, -1):
    # Blue gradient effect
    color = (0, 75 + int(80 * (1 - r / radius)), 180 + int(75 * (1 - r / radius)))
    draw.ellipse([center_x - r, center_y - r, center_x + r, center_y + r], fill=color)

# Draw rising white swooshes / arrows across the sphere
swoosh_color = (255, 255, 255)
# 4 Curved swoosh lines slicing through the globe
points_list = [
    [(390, 320), (410, 240), (450, 160)],
    [(420, 340), (450, 240), (490, 140)],
    [(455, 350), (490, 240), (530, 125)],
    [(495, 345), (535, 250), (575, 145)]
]

for pts in points_list:
    draw.line(pts, fill=swoosh_color, width=16)

# Arrow heads at the top of the swooshes
arrow_heads = [
    [(435, 160), (455, 145), (460, 175)],
    [(475, 140), (495, 125), (500, 155)],
    [(515, 125), (535, 110), (540, 140)],
    [(560, 145), (580, 130), (585, 160)]
]
for head in arrow_heads:
    draw.polygon(head, fill=swoosh_color)

# Draw Text "OASIS INFOBYTE"
try:
    font = ImageFont.truetype("arialbd.ttf", 60)
except:
    font = ImageFont.load_default()

text = "OASIS INFOBYTE"
bbox = draw.textbbox((0, 0), text, font=font)
text_w = bbox[2] - bbox[1]
draw.text((center_x - text_w // 2, 430), text, fill=(0, 75, 180), font=font)

dest_path = r"d:\aadhi\Portfolio\Portfolio\assets\images\thumbs\portfolio-three-thumb1.jpg"
image.save(dest_path, "JPEG", quality=95)
print(f"Oasis Infobyte logo successfully created and saved to {dest_path}!")
