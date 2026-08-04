import sys
import time
from bs4 import BeautifulSoup

file_path = "d:/aadhi/Portfolio/Portfolio/index.html"

with open(file_path, "r", encoding="utf-8") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "html.parser")

timestamp = int(time.time())

# 1. Add cache-busting timestamp to all <img> tags
for img in soup.find_all("img"):
    src = img.get("src")
    if src and not src.startswith("http") and not src.startswith("data:"):
        base_src = src.split("?")[0]
        img["src"] = f"{base_src}?v={timestamp}"

# 2. Add cache-busting timestamp to all hover reveal data-background-image attributes
for item in soup.find_all(attrs={"data-background-image": True}):
    bg_img = item["data-background-image"]
    if bg_img and not bg_img.startswith("http"):
        base_bg = bg_img.split("?")[0]
        item["data-background-image"] = f"{base_bg}?v={timestamp}"

with open(file_path, "w", encoding="utf-8") as f:
    f.write(str(soup))

print(f"Cache-busting query timestamp (?v={timestamp}) added to all images in index.html!")
