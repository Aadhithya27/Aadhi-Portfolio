import sys
from bs4 import BeautifulSoup
import re

file_path = "d:/aadhi/Portfolio/Portfolio/index.html"

with open(file_path, "r", encoding="utf-8") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "html.parser")

# 1. Replace logo images with "PORTFOLIO" text logo
for logo_img in soup.find_all("img", alt=re.compile(r"logo", re.IGNORECASE)):
    parent_a = logo_img.parent
    if parent_a and parent_a.name == "a":
        new_tag = soup.new_tag("span")
        new_tag["class"] = "fw-bold text-uppercase text-white"
        new_tag["style"] = "font-size: 26px; letter-spacing: 2px; font-family: sans-serif;"
        new_tag.string = "PORTFOLIO"
        logo_img.replace_with(new_tag)

# 2. Replace the banner heading text (Hello! I'm Noah Niko...)
banner_left = soup.find("h2", class_="banner-three-left-title")
if banner_left:
    banner_left.clear()
    banner_left.append("HELLO! I'M AADHITHYA C S G. A DEVELOPER, DATA ANALYTICS & GENAI ENTHUSIAST FROM CHENNAI.")

# Also replace Noah Niko in footer or anywhere else
for text_node in soup.find_all(string=True):
    if text_node.parent and text_node.parent.name not in ['script', 'style']:
        if "Noah Niko" in text_node:
            text_node.replace_with(text_node.replace("Noah Niko", "Aadhithya C S G"))
        elif "noah" in text_node.lower():
            text_node.replace_with(re.sub(r'(?i)noah', 'Aadhithya', text_node))

with open(file_path, "w", encoding="utf-8") as f:
    f.write(str(soup))

print("Logo and Hello banner text successfully updated!")
