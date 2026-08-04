import sys
from bs4 import BeautifulSoup

file_path = "d:/aadhi/Portfolio/Portfolio/index.html"

with open(file_path, "r", encoding="utf-8") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "html.parser")

testimonial_section = soup.find("section", class_="testimonial-three-area")
if testimonial_section:
    testimonial_section.decompose()
    print("Testimonial section successfully removed from index.html!")
else:
    print("Testimonial section not found.")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(str(soup))
