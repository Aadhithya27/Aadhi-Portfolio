import sys
from bs4 import BeautifulSoup

file_path = "d:/aadhi/Portfolio/Portfolio/index.html"

with open(file_path, "r", encoding="utf-8") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "html.parser")

internships = [
    {
        "title": "Data Analytics Intern — Oasis Infobyte",
        "company": "Oasis Infobyte Pvt Ltd (June 2026)",
        "tags": ["DATA ANALYTICS", "PYTHON", "MACHINE LEARNING"]
    },
    {
        "title": "ABAP Developer Intern — Ford Motor Co.",
        "company": "Ford Motor Company (August 2025)",
        "tags": ["SAP ABAP", "FORD iERP", "DATA MIGRATION"]
    },
    {
        "title": "Web Developer Intern — Jorim Tech",
        "company": "Jorim Technology Solutions (June 2024)",
        "tags": ["WEB DEVELOPMENT", "HTML/CSS", "FIGMA"]
    },
    {
        "title": "Graphic Designer Intern — Mackinlay",
        "company": "Mackinlay Enterprise (May 2024)",
        "tags": ["GRAPHIC DESIGN", "BRANDING", "VISUAL DESIGN"]
    }
]

items = soup.find_all("div", class_="portfolio-three-item")

for i, item in enumerate(items):
    if i < len(internships):
        data = internships[i]
        
        # 1. Update Title link
        title_a = item.find("h2", class_="tw-text-605").find("a") if item.find("h2", class_="tw-text-605") else None
        if title_a:
            title_a.string = data["title"]
            title_a["href"] = "#internship-experience-section"
        
        # 2. Update button link
        btn_a = item.find("a", class_="portfolio-three-btn")
        if btn_a:
            btn_a["href"] = "#internship-experience-section"

        # 3. Update thumb link
        thumb_a = item.find("div", class_="portfolio-thumb").find("a") if item.find("div", class_="portfolio-thumb") else None
        if thumb_a:
            thumb_a["href"] = "#internship-experience-section"

        # 4. Update tags
        ul_tags = item.find("ul", class_="d-flex")
        if ul_tags:
            ul_tags.clear()
            for tag_text in data["tags"]:
                li = soup.new_tag("li")
                a_tag = soup.new_tag("a", href="#internship-experience-section")
                a_tag["class"] = "text-uppercase text-heading fw-medium position-relative z-1 hover-bg-main-two-600 hover-border-main-two-600 hover-text-white tw-transition-3"
                a_tag.string = tag_text
                li.append(a_tag)
                ul_tags.append(li)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(str(soup))

print("WORKS section updated with all 4 internship experiences successfully!")
