import sys
from bs4 import BeautifulSoup
import re

file_path = "d:/aadhi/Portfolio/Portfolio/index.html"

with open(file_path, "r", encoding="utf-8") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "html.parser")

# Replace Title
if soup.title:
    soup.title.string = "Aadhithya C S G - Portfolio"

# Replace Meta Description and Keywords
meta_desc = soup.find("meta", {"name": "description"})
if meta_desc:
    meta_desc["content"] = "Aadhithya C S G Portfolio. B.Tech IT Graduate, Developer, Data Analytics, and GenAI Enthusiast."

meta_keywords = soup.find("meta", {"name": "keywords"})
if meta_keywords:
    meta_keywords["content"] = "Aadhithya C S G, Portfolio, Developer, Data Analytics, Python, GenAI, SQL, Pandas"

# General text replacements
# Note: we need to be careful with string replacements to not break tags. We'll find all text nodes and replace.
def replace_text(node, old_text, new_text, exact=False):
    if exact:
        if node.string and node.string.strip() == old_text:
            node.string.replace_with(new_text)
    else:
        if node.string and old_text in node.string:
            node.string.replace_with(node.string.replace(old_text, new_text))

for text_node in soup.find_all(string=True):
    # Replace email
    if "omioinfo@mail.com" in text_node:
        text_node.replace_with(text_node.replace("omioinfo@mail.com", "csgaadhithya11@gmail.com"))
    # Replace name placeholders
    if "Unifex" in text_node and text_node.parent.name not in ['script', 'style']:
        text_node.replace_with(text_node.replace("Unifex", "Aadhithya"))
    # Example placeholder: "developer" -> "Aadhithya C S G" in banner
    if "developer" in text_node.lower() and text_node.parent.get('class') and 'banner-three-title' in text_node.parent.get('class'):
        text_node.replace_with("Aadhithya C S G")

# Update banner specific text
banner_center = soup.find("h3", class_="banner-three-center-title")
if banner_center:
    banner_center.string = "Developer | Data Analytics | Generative AI"

# Replace about section
about_title = soup.find("h3", class_="about-three-title")
if about_title:
    about_title.string = "I'm a B.Tech Information Technology Graduate with a strong interest in Generative AI, Data Analytics, and Python development."

# Update contact
for a in soup.find_all('a'):
    if a.get('href') == 'mailto:omioinfo@mail.com':
        a['href'] = 'mailto:csgaadhithya11@gmail.com'
    if 'tel:' in str(a.get('href')):
        a['href'] = 'tel:8610082580'
        if a.string:
            a.string = '8610082580'

with open(file_path, "w", encoding="utf-8") as f:
    f.write(str(soup))

print("Portfolio updated successfully!")
