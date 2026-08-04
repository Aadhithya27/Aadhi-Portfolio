import sys
from bs4 import BeautifulSoup

file_path = "d:/aadhi/Portfolio/Portfolio/index.html"

with open(file_path, "r", encoding="utf-8") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "html.parser")

wrapper = soup.find("div", class_="feature-three-wrapper")
if wrapper:
    singles = wrapper.find_all("div", class_="feature-three-single")
    for single in singles:
        # Find year span (last span with 2026)
        spans = single.find_all("span", class_="feature-three-text")
        for span in spans:
            if "2026" in span.text:
                span["style"] = "white-space: nowrap; display: inline-block;"
                parent_div = span.parent
                if parent_div and parent_div.name == "div":
                    parent_div["style"] = "white-space: nowrap; flex-shrink: 0; margin-left: 15px;"
                    parent_div["class"] = parent_div.get("class", []) + ["flex-shrink-0", "ms-3"]

with open(file_path, "w", encoding="utf-8") as f:
    f.write(str(soup))

print("Year 2026 alignment fixed across all design showcase items!")
