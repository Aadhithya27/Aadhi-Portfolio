import sys
from bs4 import BeautifulSoup

file_path = "d:/aadhi/Portfolio/Portfolio/index.html"

with open(file_path, "r", encoding="utf-8") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "html.parser")

# 1. Update 5 Main Skills List in Hero Banner
banner_list = soup.find("div", class_="banner-three-list")
if banner_list:
    new_skills = [
        "Python & Generative AI",
        "Data Analytics & EDA",
        "SQL & Database Management",
        "Responsive Web Development",
        "UI/UX Design (Figma)"
    ]
    items = banner_list.find_all("li")
    for i, li in enumerate(items):
        if i < len(new_skills):
            # Preserve the span image/icon and update text
            span = li.find("span")
            li.clear()
            if span:
                li.append(span)
            li.append(" " + new_skills[i] + "\n")

# 2. Update Header Social Icons (LinkedIn, GitHub, Instagram, Phone)
header_social = soup.find("div", class_="header-three-social")
if header_social:
    ul = header_social.find("ul")
    if ul:
        ul.clear()
        
        social_items = [
            {"url": "https://www.linkedin.com/in/aadhithya-csg-27913b260/", "icon": "ph-bold ph-linkedin-logo", "title": "LinkedIn", "target": "_blank"},
            {"url": "https://github.com/Aadhithya27", "icon": "ph-bold ph-github-logo", "title": "GitHub", "target": "_blank"},
            {"url": "https://instagram.com", "icon": "ph-bold ph-instagram-logo", "title": "Instagram", "target": "_blank"},
            {"url": "tel:8610082580", "icon": "ph-bold ph-phone-call", "title": "Phone", "target": "_self"}
        ]
        
        for item in social_items:
            li = soup.new_tag("li")
            a = soup.new_tag("a", href=item["url"], target=item["target"], title=item["title"])
            a["class"] = "tw-w-13 tw-h-13 lh-1 d-inline-flex justify-content-center align-items-center text-heading tw-text-xl tw-rounded-md"
            i_tag = soup.new_tag("i")
            i_tag["class"] = item["icon"]
            a.append(i_tag)
            li.append(a)
            ul.append(li)

# Also update footer or side-menu social links if they have Facebook / X
for ul in soup.find_all("ul"):
    # If this ul contains facebook or x icon links, update them to our set
    if ul.find("i", class_=lambda c: c and ("ph-facebook-logo" in c or "ph-x-logo" in c)):
        ul.clear()
        social_items = [
            {"url": "https://www.linkedin.com/in/aadhithya-csg-27913b260/", "icon": "ph ph-linkedin-logo", "title": "LinkedIn", "target": "_blank"},
            {"url": "https://github.com/Aadhithya27", "icon": "ph ph-github-logo", "title": "GitHub", "target": "_blank"},
            {"url": "https://instagram.com", "icon": "ph ph-instagram-logo", "title": "Instagram", "target": "_blank"},
            {"url": "tel:8610082580", "icon": "ph ph-phone-call", "title": "Phone", "target": "_self"}
        ]
        for item in social_items:
            li = soup.new_tag("li")
            a = soup.new_tag("a", href=item["url"], target=item["target"], title=item["title"])
            a["class"] = "tw-w-11 tw-h-101 lh-1 d-inline-flex align-items-center justify-content-center tw-rounded-lg tw-text-xl text-heading hover-bg-main-600 hover-text-heading"
            i_tag = soup.new_tag("i")
            i_tag["class"] = item["icon"]
            a.append(i_tag)
            li.append(a)
            ul.append(li)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(str(soup))

print("Skills list and top social icons successfully updated!")
