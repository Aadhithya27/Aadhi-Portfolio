import sys
from bs4 import BeautifulSoup

file_path = "d:/aadhi/Portfolio/Portfolio/index.html"

with open(file_path, "r", encoding="utf-8") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "html.parser")

for span in soup.find_all("span", class_="tw-btn-circle-icon"):
    if "15+" in span.text or "15" in span.text:
        span.string = "4+"

for span in soup.find_all("span"):
    if span.string and "Years of Experience" in span.string:
        span.string = "MNC level Internship exp"

with open(file_path, "w", encoding="utf-8") as f:
    f.write(str(soup))

print("Badge successfully updated to 4+ MNC level Internship exp!")
