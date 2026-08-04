import sys
from bs4 import BeautifulSoup

file_path = "d:/aadhi/Portfolio/Portfolio/index.html"

with open(file_path, "r", encoding="utf-8") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "html.parser")

# Find and decompose about-three-wrap-shape
wrap_shape = soup.find("div", class_="about-three-wrap-shape")
if wrap_shape:
    wrap_shape.decompose()

with open(file_path, "w", encoding="utf-8") as f:
    f.write(str(soup))

print("Unwanted stat cards (478/5 and 115k+) successfully removed!")
