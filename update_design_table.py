import sys
from bs4 import BeautifulSoup

file_path = "d:/aadhi/Portfolio/Portfolio/index.html"

with open(file_path, "r", encoding="utf-8") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "html.parser")

designs_data = [
    {
        "category": "Apoorvaa.in",
        "title": "Interior & Furniture Company Web Design",
        "year": "2026"
    },
    {
        "category": "INFOVISTA '25",
        "title": "Battle Circuit Event Poster & Graphic Design",
        "year": "2026"
    },
    {
        "category": "ATOM Instruments",
        "title": "Product Catalogue & Industrial Visual Design",
        "year": "2026"
    },
    {
        "category": "Praani News",
        "title": "Haven of Hues Animal Rescue Campaign & Newsletter",
        "year": "2026"
    },
    {
        "category": "Web Dev Promo",
        "title": "Get Your Website In A Week Marketing Assets",
        "year": "2026"
    },
    {
        "category": "3D Architecture",
        "title": "Wooden Mandir Temple Spatial & Dimension Design",
        "year": "2026"
    }
]

wrapper = soup.find("div", class_="feature-three-wrapper")
if wrapper:
    rows = wrapper.find_all("div", class_="feature-three-single")
    for i, row in enumerate(rows):
        if i < len(designs_data):
            d = designs_data[i]
            
            # Find spans inside feature-three-left
            left_div = row.find("div", class_="feature-three-left")
            if left_div:
                spans = left_div.find_all("span", class_="feature-three-text")
                if len(spans) >= 3:
                    spans[1].string = d["category"]
                    spans[2].string = d["title"]
            
            # Update Year to 2026
            right_div = row.find_all("div")[-1] if row.find_all("div") else None
            year_span = row.find_all("span", class_="feature-three-text")[-1] if row.find_all("span", class_="feature-three-text") else None
            if year_span:
                year_span.string = "2026"

with open(file_path, "w", encoding="utf-8") as f:
    f.write(str(soup))

print("Design Showcase Table successfully updated with 2026 for all items!")
