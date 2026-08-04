import sys
from bs4 import BeautifulSoup
import re

file_path = "d:/aadhi/Portfolio/Portfolio/index.html"

with open(file_path, "r", encoding="utf-8") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "html.parser")

# 1. Remove "4+" from the circular badge
for span in soup.find_all("span", class_="tw-btn-circle-icon"):
    if "4+" in span.text or "4" in span.text:
        span.clear()

# 2. Change scrolling Marquee "Services" to "PROJECTS"
for h2 in soup.find_all("h2", class_=lambda c: c and "marquee" in c):
    # If text contains Services or SERVICES, replace it with PROJECTS
    for text_node in h2.find_all(string=True):
        if "Services" in text_node:
            text_node.replace_with(text_node.replace("Services", "PROJECTS"))
        elif "SERVICES" in text_node:
            text_node.replace_with(text_node.replace("SERVICES", "PROJECTS"))
        elif "services" in text_node:
            text_node.replace_with(text_node.replace("services", "PROJECTS"))

with open(file_path, "w", encoding="utf-8") as f:
    f.write(str(soup))

print("Badge number removed and Marquee updated to PROJECTS successfully!")
