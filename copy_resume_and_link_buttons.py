import os
import shutil
from bs4 import BeautifulSoup

# 1. Copy PDF resume from artifacts to portfolio directory
pdf_src = r"C:\Users\welcome\.gemini\antigravity-ide\brain\fdb62e71-ca3c-476f-83cd-778072b4cfb0\media__1785815169916.pdf"
pdf_dest = r"d:\aadhi\Portfolio\Portfolio\Aadhithya_CSG_Resume.pdf"

if os.path.exists(pdf_src):
    shutil.copyfile(pdf_src, pdf_dest)
    print("PDF Resume copied successfully to portfolio folder!")

# 2. Update index.html button links
file_path = r"d:\aadhi\Portfolio\Portfolio\index.html"

with open(file_path, "r", encoding="utf-8") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "html.parser")

# Update "VIEW PROJECTS" button to scroll to #service-three-area
for a_tag in soup.find_all("a"):
    text = a_tag.text.strip().lower()
    if "view projects" in text:
        a_tag["href"] = "#service-three-area"
        print("VIEW PROJECTS button link updated to #service-three-area!")

# Update "DOWNLOAD CV" / "DOWNLOAD RESUME" buttons to download Aadhithya_CSG_Resume.pdf
for a_tag in soup.find_all("a"):
    text = a_tag.text.strip().lower()
    if "download cv" in text or "download resume" in text:
        a_tag["href"] = "Aadhithya_CSG_Resume.pdf"
        a_tag["download"] = "Aadhithya_CSG_Resume.pdf"
        a_tag["target"] = "_blank"
        print("DOWNLOAD CV button configured to download PDF resume!")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(str(soup))

print("Button link updates complete!")
