import sys
from bs4 import BeautifulSoup

file_path = "d:/aadhi/Portfolio/Portfolio/index.html"

with open(file_path, "r", encoding="utf-8") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "html.parser")

# 1. Ensure section IDs exist
banner = soup.find("section", class_="banner-three-area")
if banner:
    banner["id"] = "hero-section"

about = soup.find("section", class_="about-three-area")
if about:
    about["id"] = "about-three-area"

service = soup.find("section", class_="service-three-area")
if service:
    service["id"] = "service-three-area"

feature = soup.find("div", class_="feature-three-area")
if feature:
    feature["id"] = "feature-three-area"

footer = soup.find("footer")
if footer:
    footer["id"] = "footer-three-area"

# 2. Build offcanvas menu items explicitly inside <div class="tw-main-menu-mobile"><nav></nav></div>
mobile_menu_nav = soup.find("div", class_="tw-main-menu-mobile")
if mobile_menu_nav:
    nav = mobile_menu_nav.find("nav") or soup.new_tag("nav")
    nav.clear()
    
    ul = soup.new_tag("ul")
    ul["class"] = "tw-offcanvas-menu-list"
    
    menu_items = [
        {"title": "HOME", "href": "#hero-section"},
        {"title": "ABOUT", "href": "#about-three-area"},
        {"title": "PROJECTS", "href": "#service-three-area"},
        {"title": "SHOWCASE", "href": "#feature-three-area"},
        {"title": "INTERNSHIPS", "href": "#internship-experience-section"},
        {"title": "CONTACT", "href": "#footer-three-area"}
    ]
    
    for item in menu_items:
        li = soup.new_tag("li")
        a = soup.new_tag("a", href=item["href"])
        a["class"] = "tw-offcanvas-nav-link text-white fw-bold tw-text-4xl hover-text-main-two-600 tw-transition-3"
        a.string = item["title"]
        li.append(a)
        ul.append(li)
        
    nav.append(ul)
    mobile_menu_nav.clear()
    mobile_menu_nav.append(nav)

# 3. Add smooth scroll and drawer auto-close script before </body>
script_tag_id = "offcanvas-nav-script"
if not soup.find(id=script_tag_id):
    js_code = """
    document.addEventListener("DOMContentLoaded", function() {
        var links = document.querySelectorAll(".tw-main-menu-mobile a, .tw-offcanvas-2-area a[href^='#']");
        links.forEach(function(link) {
            link.addEventListener("click", function(e) {
                var targetId = this.getAttribute("href");
                if (targetId && targetId.startsWith("#")) {
                    var targetElement = document.querySelector(targetId);
                    if (targetElement) {
                        e.preventDefault();
                        // Close offcanvas drawer
                        var closeBtn = document.querySelector(".tw-offcanvas-2-close-btn, .tw-offcanvas-close-btn");
                        if (closeBtn) {
                            closeBtn.click();
                        }
                        var offcanvasArea = document.querySelector(".tw-offcanvas-2-area");
                        if (offcanvasArea) {
                            offcanvasArea.classList.remove("offcanvas-open");
                        }
                        var overlay = document.querySelector(".side-overlay, .overlay");
                        if (overlay) {
                            overlay.classList.remove("overlay-open");
                        }
                        // Smooth scroll to target section
                        targetElement.scrollIntoView({ behavior: "smooth" });
                    }
                }
            });
        });
    });
    """
    new_script = soup.new_tag("script", id=script_tag_id)
    new_script.string = js_code
    soup.body.append(new_script)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(str(soup))

print("Offcanvas navigation links and smooth scroll auto-close handlers successfully configured!")
