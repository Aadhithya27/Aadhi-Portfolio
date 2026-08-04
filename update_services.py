import sys
from bs4 import BeautifulSoup

file_path = "d:/aadhi/Portfolio/Portfolio/index.html"

with open(file_path, "r", encoding="utf-8") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "html.parser")

# Update services
services = ['Data Analysis & Insights', 'Python Automation Scripts', 'Web Development', 'AI Workflow Integration']
service_elements = soup.select('.service-three-title')

for i, el in enumerate(service_elements):
    if i < len(services):
        if el.find('a'):
            el.find('a').string = services[i]
        else:
            el.string = services[i]

# Update social links
# Assuming we want to update the social links in footer or header
for a in soup.find_all('a'):
    href = a.get('href')
    if href and 'linkedin.com' in href:
        a['href'] = 'https://www.linkedin.com/in/aadhithya-csg-27913b260/'
    if href and 'github.com' in href:
        a['href'] = 'https://github.com/Aadhithya27'
    # if it's generic # social link, we can just replace the first few
    
# We will just write it back
with open(file_path, "w", encoding="utf-8") as f:
    f.write(str(soup))

print("Services and Social Links updated successfully!")
