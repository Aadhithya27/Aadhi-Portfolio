import sys
from bs4 import BeautifulSoup

file_path = "d:/aadhi/Portfolio/Portfolio/index.html"

with open(file_path, "r", encoding="utf-8") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "html.parser")

brand_section = soup.find("section", class_="brand-three-area")
if brand_section:
    brand_section.decompose()
    print("Client brand logo grid section successfully removed from index.html!")
else:
    print("Brand section not found.")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(str(soup))
