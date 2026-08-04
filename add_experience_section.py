import sys
from bs4 import BeautifulSoup

file_path = "d:/aadhi/Portfolio/Portfolio/index.html"

with open(file_path, "r", encoding="utf-8") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "html.parser")

# Check if experience section already added
if not soup.find(id="internship-experience-section"):
    experience_html = """
    <!-- ==================== Experience & Education Section Start ==================== -->
    <section id="internship-experience-section" class="py-120 bg-black text-white">
      <div class="container tw-container-1800-px">
        <div class="row tw-mb-15">
          <div class="col-12 text-center">
            <h2 class="tw-text-4xl text-white fw-bold text-uppercase tw-mb-4">Internship Experience & Education</h2>
            <p class="text-white-50 tw-text-lg">My professional journey, key projects, and academic background.</p>
          </div>
        </div>

        <div class="row g-4">
          <!-- Internships Column -->
          <div class="col-lg-6">
            <h3 class="tw-text-2xl text-main-two-600 fw-bold tw-mb-6 border-bottom pb-2">💼 Internship Experience</h3>
            
            <div class="tw-mb-6 p-4 bg-neutral-900 tw-rounded-lg border border-neutral-800">
              <span class="badge bg-main-two-600 text-black fw-bold mb-2">June 2026</span>
              <h4 class="text-white tw-text-xl fw-bold">Data Analytics Intern</h4>
              <p class="text-white-50 fw-medium">Oasis Infobyte Pvt Ltd</p>
              <ul class="text-white-50 tw-text-sm mt-2 ps-3">
                <li>Performed data cleaning, preprocessing, and exploratory data analysis (EDA) using Python.</li>
                <li>Conducted EDA on retail sales data to identify customer and sales trends.</li>
                <li>Built a customer segmentation model and house price prediction model.</li>
              </ul>
            </div>

            <div class="tw-mb-6 p-4 bg-neutral-900 tw-rounded-lg border border-neutral-800">
              <span class="badge bg-main-two-600 text-black fw-bold mb-2">Aug 2025</span>
              <h4 class="text-white tw-text-xl fw-bold">ABAP Developer Intern</h4>
              <p class="text-white-50 fw-medium">Ford Motor Company</p>
              <ul class="text-white-50 tw-text-sm mt-2 ps-3">
                <li>Worked in SAP ABAP within the Data Conversion team as part of the iERP project.</li>
                <li>Contributed to enterprise data migration and SAP integration tasks.</li>
                <li>Handled flat-file operations including reading, validating, and processing files.</li>
              </ul>
            </div>

            <div class="tw-mb-6 p-4 bg-neutral-900 tw-rounded-lg border border-neutral-800">
              <span class="badge bg-main-two-600 text-black fw-bold mb-2">June 2024</span>
              <h4 class="text-white tw-text-xl fw-bold">Web Developer Intern</h4>
              <p class="text-white-50 fw-medium">Jorim Technology Solutions Pvt Ltd</p>
              <ul class="text-white-50 tw-text-sm mt-2 ps-3">
                <li>Designed and implemented responsive web pages using HTML, CSS, and Figma.</li>
                <li>Assisted in deploying frontend changes to testing and production environments.</li>
              </ul>
            </div>

            <div class="tw-mb-6 p-4 bg-neutral-900 tw-rounded-lg border border-neutral-800">
              <span class="badge bg-main-two-600 text-black fw-bold mb-2">May 2024</span>
              <h4 class="text-white tw-text-xl fw-bold">Graphic Designer Intern</h4>
              <p class="text-white-50 fw-medium">Mackinlay Enterprise</p>
              <ul class="text-white-50 tw-text-sm mt-2 ps-3">
                <li>Designed creative, visually engaging digital graphics and marketing/branding materials.</li>
              </ul>
            </div>
          </div>

          <!-- Education & Achievements Column -->
          <div class="col-lg-6">
            <h3 class="tw-text-2xl text-main-two-600 fw-bold tw-mb-6 border-bottom pb-2">🎓 Education & Achievements</h3>
            
            <div class="tw-mb-6 p-4 bg-neutral-900 tw-rounded-lg border border-neutral-800">
              <span class="badge bg-main-two-600 text-black fw-bold mb-2">2022 – 2026</span>
              <h4 class="text-white tw-text-xl fw-bold">B.Tech in Information Technology</h4>
              <p class="text-white-50 fw-medium">Sri Sairam Engineering College, Chennai</p>
              <p class="text-white font-semibold mt-2">CGPA: <span class="text-main-two-600 fw-bold">7.21</span></p>
            </div>

            <div class="tw-mb-6 p-4 bg-neutral-900 tw-rounded-lg border border-neutral-800">
              <span class="badge bg-main-two-600 text-black fw-bold mb-2">2021 – 2022</span>
              <h4 class="text-white tw-text-xl fw-bold">HSC (Higher Secondary)</h4>
              <p class="text-white-50 fw-medium">SRM Nightingale School, Chennai</p>
              <p class="text-white font-semibold mt-2">Percentage: <span class="text-main-two-600 fw-bold">74.33%</span></p>
            </div>

            <div class="tw-mb-6 p-4 bg-neutral-900 tw-rounded-lg border border-neutral-800">
              <h4 class="text-white tw-text-xl fw-bold mb-3">🏆 Achievements & Certifications</h4>
              <ul class="text-white-50 tw-text-sm ps-3">
                <li class="mb-2"><strong>5G & 6G Hackathon 2024:</strong> Selected among Top 30 teams from 4,000+ applicants in Bangalore.</li>
                <li class="mb-2"><strong>Research Publication:</strong> Published paper "Design and Implementation of MR Models in Healthcare" at ICCCT 2025.</li>
                <li class="mb-2"><strong>Certifications:</strong> Spoken Tutorial Python 3.4.3, NPTEL Cloud Computing & IoT, MathWorks Deep Learning Onramp.</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- ==================== Experience & Education Section End ==================== -->
    """
    
    # Insert before main footer
    footer = soup.find("footer") or soup.find("section", class_="footer-three-area")
    if footer:
        new_section_soup = BeautifulSoup(experience_html, "html.parser")
        footer.insert_before(new_section_soup)
    else:
        # Append to body
        new_section_soup = BeautifulSoup(experience_html, "html.parser")
        soup.body.append(new_section_soup)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(str(soup))
    print("Experience and Education section added successfully!")
else:
    print("Experience section already exists!")
