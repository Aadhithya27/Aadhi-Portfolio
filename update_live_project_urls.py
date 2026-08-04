import sys
from bs4 import BeautifulSoup

file_path = "d:/aadhi/Portfolio/Portfolio/index.html"

with open(file_path, "r", encoding="utf-8") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "html.parser")

project_links_map = [
    {
        "search_text": "Hari Fitness",
        "url": "https://hari-fitness.vercel.app/",
        "tags": ["GenAI", "React/Next.js", "Vercel"]
    },
    {
        "search_text": "Data Analytics",
        "url": "https://github.com/Aadhithya27",
        "tags": ["Python", "Pandas & NumPy", "Matplotlib"]
    },
    {
        "search_text": "NEET Coaching",
        "url": "https://apoorvaa.in/",
        "tags": ["HTML/CSS/JS", "Figma", "Live Website"]
    },
    {
        "search_text": "Material Master Data",
        "url": "https://github.com/Aadhithya27",
        "tags": ["SAP ABAP", "iERP", "Data Migration"]
    }
]

service_singles = soup.find_all("div", class_="service-three-single")

for i, single in enumerate(service_singles):
    if i < len(project_links_map):
        p_info = project_links_map[i]
        
        # 1. Update Title link
        title_h2 = single.find("h2", class_="service-three-title")
        if title_h2:
            a_tag = title_h2.find("a")
            if a_tag:
                a_tag["href"] = p_info["url"]
                a_tag["target"] = "_blank"
                a_tag["rel"] = "noopener noreferrer"
        
        # 2. Update Thumbnail image link
        thumb_div = single.find("div", class_="service-three-thumb")
        if thumb_div:
            a_thumb = thumb_div.find("a")
            if a_thumb:
                a_thumb["href"] = p_info["url"]
                a_thumb["target"] = "_blank"
                a_thumb["rel"] = "noopener noreferrer"
        
        # 3. Update tags pill list
        ul_tags = single.find("ul", class_="d-flex")
        if ul_tags:
            ul_tags.clear()
            for tag_text in p_info["tags"]:
                li = soup.new_tag("li")
                a_pill = soup.new_tag("a", href=p_info["url"], target="_blank")
                a_pill["class"] = "text-uppercase text-white tw-text-sm fw-medium position-relative z-1 hover-bg-main-two-600 hover-border-main-two-600 hover-text-heading tw-transition-3"
                a_pill.string = tag_text
                li.append(a_pill)
                ul_tags.append(li)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(str(soup))

print("Project URLs, thumbnails, and tech tags updated successfully to open live web pages!")
