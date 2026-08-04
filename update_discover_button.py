import sys
from bs4 import BeautifulSoup

file_path = "d:/aadhi/Portfolio/Portfolio/index.html"

with open(file_path, "r", encoding="utf-8") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "html.parser")

# Find the Discover Our Projects button
btn_wrapper = soup.find("div", class_="portfolio-three-counter")
if btn_wrapper:
    a_tag = btn_wrapper.find("a")
    if a_tag:
        a_tag["href"] = "https://github.com/Aadhithya27"
        a_tag["target"] = "_blank"
        a_tag["rel"] = "noopener noreferrer"

with open(file_path, "w", encoding="utf-8") as f:
    f.write(str(soup))

print("Discover Our Projects button successfully updated to redirect to GitHub!")
