from bs4 import BeautifulSoup

file_path = "d:/aadhi/Portfolio/Portfolio/index.html"

with open(file_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

imgs = soup.find_all("img")
for i, img in enumerate(imgs):
    print(f"{i+1}. src='{img.get('src')}' alt='{img.get('alt')}' class='{img.get('class')}'")
