import sys
from bs4 import BeautifulSoup
import re

file_path = "d:/aadhi/Portfolio/Portfolio/index.html"

with open(file_path, "r", encoding="utf-8") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "html.parser")

# 1. Update logo color to black
for span in soup.find_all("span", string="PORTFOLIO"):
    span["style"] = "font-size: 26px; letter-spacing: 2px; font-family: sans-serif; color: #000;"
    span["class"] = "fw-bold text-uppercase text-black"

# 2. Update Stats Boxes (Side cards next to hero greeting)
counter_items = soup.select(".banner-three-counter-item")
if len(counter_items) >= 3:
    # Card 1: CGPA
    card1_title = counter_items[0].find(class_="banner-three-counter-title")
    if card1_title:
        card1_title.clear()
        card1_title.append("7.21")
    card1_p = counter_items[0].find(class_="banner-three-counter-paragraph")
    if card1_p:
        card1_p.string = "B.Tech IT CGPA (Sri Sairam Eng. College)"

    # Card 2: Projects
    card2_title = counter_items[1].find(class_="banner-three-counter-title")
    if card2_title:
        card2_title.clear()
        card2_title.append("4+")
    card2_p = counter_items[1].find(class_="banner-three-counter-paragraph")
    if card2_p:
        card2_p.string = "Major Projects & Platforms Built"

    # Card 3: Internships
    card3_title = counter_items[2].find(class_="banner-three-counter-title")
    if card3_title:
        card3_title.clear()
        card3_title.append("4")
    card3_p = counter_items[2].find(class_="banner-three-counter-paragraph")
    if card3_p:
        card3_p.string = "Internships (Oasis, Ford, Jorim, Mackinlay)"

# 3. Update Experience / Work section if present or create/insert structured content
# Let's inspect service / portfolio items and update them with Projects and Internships

# Projects list
projects_data = [
    {
        "title": "Hari Fitness — Personal Training Platform",
        "category": "GenAI-assisted Platform (July 2026)",
        "desc": "Fitness coaching web platform with GenAI tools, nutrition tracking, client progress management, deployed on Vercel."
    },
    {
        "title": "Data Analytics — Time-Series Market Data",
        "category": "Python & EDA (June 2026)",
        "desc": "Object-oriented Python app performing time-series analysis & Matplotlib visualizations on OHLCV financial market data."
    },
    {
        "title": "NEET Coaching Academy — Website & Design",
        "category": "Web Development (June 2024)",
        "desc": "Responsive website for NEET coaching academy with intuitive user interfaces focused on accessibility and UX (apoorvaa.in)."
    },
    {
        "title": "Material Master Data Conversion — Ford Motor Co.",
        "category": "SAP ABAP / iERP Project (Aug 2025)",
        "desc": "Worked in SAP ABAP data conversion team for Ford's SAP iERP implementation, handling validation & enterprise data migration."
    }
]

# Internships list
internships_data = [
    {
        "role": "Data Analytics Intern",
        "company": "Oasis Infobyte Pvt Ltd",
        "date": "June 2026",
        "details": "Exploratory Data Analysis (EDA) on retail sales data, customer segmentation, and house price prediction ML models."
    },
    {
        "role": "ABAP Developer Intern",
        "company": "Ford Motor Company",
        "date": "August 2025",
        "details": "SAP ABAP Data Conversion team for iERP project. Data migration, flat-file processing & integration."
    },
    {
        "role": "Web Developer Intern",
        "company": "Jorim Technology Solutions Pvt Ltd",
        "date": "June 2024",
        "details": "Responsive HTML/CSS/Figma web pages, frontend deployment to testing & production environments."
    },
    {
        "role": "Graphic Designer Intern",
        "company": "Mackinlay Enterprise",
        "date": "May 2024",
        "details": "Designed digital graphics, branding materials, visual content while maintaining brand consistency."
    }
]

# Replace service items with Projects
service_titles = soup.select(".service-three-title")
for i, item in enumerate(service_titles):
    if i < len(projects_data):
        p = projects_data[i]
        if item.find("a"):
            item.find("a").string = p["title"]
        else:
            item.string = p["title"]

# Replace service descriptions if available
service_paras = soup.select(".service-three-item p, .service-item p")
for i, p_tag in enumerate(service_paras):
    if i < len(projects_data):
        p_tag.string = projects_data[i]["desc"]

with open(file_path, "w", encoding="utf-8") as f:
    f.write(str(soup))

print("Successfully updated logo to black, CGPA, stats cards, and project details!")
