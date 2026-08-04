import sys
from bs4 import BeautifulSoup

file_path = "d:/aadhi/Portfolio/Portfolio/index.html"

with open(file_path, "r", encoding="utf-8") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "html.parser")

insta_url = "https://www.instagram.com/aadhi.__.csg/"

updated_count = 0
for a in soup.find_all("a"):
    href = a.get("href", "")
    title = a.get("title", "").lower()
    # Check if link or title refers to Instagram
    if "instagram.com" in href or title == "instagram" or "instagram" in a.text.lower():
        a["href"] = insta_url
        a["target"] = "_blank"
        updated_count += 1

with open(file_path, "w", encoding="utf-8") as f:
    f.write(str(soup))

print(f"Instagram profile URL updated to {insta_url} across {updated_count} link(s)!")
