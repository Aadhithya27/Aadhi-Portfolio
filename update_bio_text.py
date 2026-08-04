import sys
from bs4 import BeautifulSoup

file_path = "d:/aadhi/Portfolio/Portfolio/index.html"

with open(file_path, "r", encoding="utf-8") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "html.parser")

# 1. Update About Heading Title
about_title = soup.find("h2", class_="about-three-title")
if about_title:
    about_title.clear()
    about_title.append("I'm a B.Tech Information Technology Graduate with a strong interest in Generative AI, Data Analytics, and Python development.")

# 2. Update About Right Paragraphs
about_right = soup.find("div", class_="about-three-right")
if about_right:
    paras = about_right.find_all("p", class_="tw-text-xl")
    new_paras_text = [
        "I have hands-on experience with Python, SQL, data analysis, and building responsive web interfaces.",
        "I'm passionate about exploring AI technologies, analyzing data to uncover meaningful insights, and continuously expanding my knowledge of machine learning and modern AI tools.",
        "My goal is to grow into a skilled GenAI Engineer by combining problem-solving, continuous learning, and practical project development."
    ]
    for i, p in enumerate(paras):
        if i < len(new_paras_text):
            p.string = new_paras_text[i]

with open(file_path, "w", encoding="utf-8") as f:
    f.write(str(soup))

print("Bio text successfully updated in the About section!")
