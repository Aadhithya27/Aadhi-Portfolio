from PIL import Image, ImageDraw, ImageFont
import os

width, height = 800, 1000
img = Image.new("RGB", (width, height), (254, 246, 235))  # Warm cream background
draw = ImageDraw.Draw(img)

# Top white section
draw.rectangle([0, 0, width, 450], fill=(255, 255, 255))

# Try loading fonts
try:
    title_font = ImageFont.truetype("georgiai.ttf", 55)
    font_bold = ImageFont.truetype("arialbd.ttf", 26)
    font_regular = ImageFont.truetype("arial.ttf", 20)
    font_small = ImageFont.truetype("arial.ttf", 14)
except:
    title_font = ImageFont.load_default()
    font_bold = ImageFont.load_default()
    font_regular = ImageFont.load_default()
    font_small = ImageFont.load_default()

# 1. Top Cursive Title
title_text = "Check out our\n new Website"
draw.text((100, 60), title_text, fill=(20, 20, 20), font=title_font)

# Search Bar Mockup
draw.rounded_rectangle([180, 220, 620, 270], radius=25, fill=(255, 255, 255), outline=(50, 50, 50), width=2)
draw.text((260, 232), "https://apoorvaa.in", fill=(40, 40, 40), font=font_regular)
# Search magnifying glass icon
draw.ellipse([575, 235, 595, 255], outline=(50, 50, 50), width=2)
draw.line([590, 250, 602, 262], fill=(50, 50, 50), width=3)

# 2. Main Device Screen - Dark Navy Laptop
laptop_left, laptop_top, laptop_right, laptop_bottom = 160, 360, 640, 680
draw.rounded_rectangle([laptop_left, laptop_top, laptop_right, laptop_bottom], radius=15, fill=(12, 18, 32))
# Laptop Base line
draw.rounded_rectangle([130, 675, 670, 690], radius=5, fill=(160, 165, 175))

# Content on Laptop Screen
# Header logo
draw.text((laptop_left + 25, laptop_top + 20), "APOORVAA", fill=(235, 80, 100), font=font_bold)
draw.text((laptop_left + 160, laptop_top + 23), "Furn & Interior", fill=(100, 200, 210), font=font_small)

# Badge
draw.rounded_rectangle([laptop_left + 25, laptop_top + 65, laptop_left + 170, laptop_top + 85], radius=10, fill=(180, 50, 60))
draw.text((laptop_left + 35, laptop_top + 67), "Architectural Innovation", fill=(255, 255, 255), font=font_small)

# Hero Slogan
draw.text((laptop_left + 25, laptop_top + 100), "Crafting Spaces,\nInspiring Minds", fill=(255, 255, 255), font=font_bold)

# 3. Overlapping Tablet Screen (Bottom Left)
tab_left, tab_top, tab_right, tab_bottom = 80, 500, 310, 780
draw.rounded_rectangle([tab_left, tab_top, tab_right, tab_bottom], radius=20, fill=(18, 26, 42), outline=(100, 110, 125), width=4)
# Content inside tablet
draw.text((tab_left + 20, tab_top + 40), "Ready to Discuss\nYour Project?", fill=(255, 255, 255), font=font_bold)
# Green WhatsApp button
draw.rounded_rectangle([tab_left + 20, tab_top + 110, tab_right - 20, tab_top + 145], radius=8, fill=(35, 165, 90))
draw.text((tab_left + 35, tab_top + 118), "Chat Instantly Now", fill=(255, 255, 255), font=font_small)

# 4. Overlapping Smartphone Screen (Bottom Right)
phone_left, phone_top, phone_right, phone_bottom = 520, 520, 680, 790
draw.rounded_rectangle([phone_left, phone_top, phone_right, phone_bottom], radius=22, fill=(18, 26, 42), outline=(100, 110, 125), width=4)
# Content inside phone
draw.text((phone_left + 15, phone_top + 30), "APOORVAA", fill=(235, 80, 100), font=font_bold)
draw.text((phone_left + 15, phone_top + 65), "Crafting Spaces,\nInspiring Minds", fill=(255, 255, 255), font=font_small)
# Red Call button
draw.rounded_rectangle([phone_left + 15, phone_top + 115, phone_right - 15, phone_top + 145], radius=8, fill=(220, 60, 70))
draw.text((phone_left + 25, phone_top + 122), "Enquire via Call", fill=(255, 255, 255), font=font_small)

# Bottom Text
draw.text((320, 810), "Check in Bio", fill=(40, 40, 40), font=title_font)

dest_path = r"d:\aadhi\Portfolio\Portfolio\assets\images\thumbs\feature-three-thumb1.jpg"
img.save(dest_path, "JPEG", quality=95)
print(f"Apoorvaa poster successfully generated and saved to {dest_path}!")
