import sys
from bs4 import BeautifulSoup

file_path = "d:/aadhi/Portfolio/Portfolio/index.html"

with open(file_path, "r", encoding="utf-8") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "html.parser")

header_social = soup.find("div", class_="header-three-social")
if header_social:
    header_social.clear()
    
    ul = soup.new_tag("ul")
    ul["class"] = "d-flex tw-gap-205"
    
    socials = [
        {"url": "https://www.linkedin.com/in/aadhithya-csg-27913b260/", "icon": "ph-bold ph-linkedin-logo", "title": "LinkedIn", "target": "_blank"},
        {"url": "https://github.com/Aadhithya27", "icon": "ph-bold ph-github-logo", "title": "GitHub", "target": "_blank"},
        {"url": "https://instagram.com", "icon": "ph-bold ph-instagram-logo", "title": "Instagram", "target": "_blank"},
        {"url": "tel:8610082580", "icon": "ph-bold ph-phone-call", "title": "Phone", "target": "_self"}
    ]
    
    for item in socials:
        li = soup.new_tag("li")
        a = soup.new_tag("a", href=item["url"], target=item["target"], title=item["title"])
        a["class"] = "tw-w-13 tw-h-13 lh-1 d-inline-flex justify-content-center align-items-center text-heading tw-text-xl tw-rounded-md"
        i_tag = soup.new_tag("i")
        i_tag["class"] = item["icon"]
        a.append(i_tag)
        li.append(a)
        ul.append(li)
        
    header_social.append(ul)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(str(soup))

print("Header text menu removed and social media icon buttons successfully restored!")
