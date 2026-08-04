import sys
from bs4 import BeautifulSoup

file_path = "d:/aadhi/Portfolio/Portfolio/index.html"

with open(file_path, "r", encoding="utf-8") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "html.parser")

# Clear mobile/offcanvas main menu completely
mobile_menu = soup.find("div", class_="tw-main-menu-mobile")
if mobile_menu:
    mobile_menu.clear()

# Clear main menu completely
header_menu = soup.find("div", class_="header-menu")
if header_menu:
    header_menu.clear()

with open(file_path, "w", encoding="utf-8") as f:
    f.write(str(soup))

print("Text menu list successfully removed completely from index.html!")
