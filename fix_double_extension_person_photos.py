import os
import shutil

# 1. Fix Hero section photo (banner-three-man.png)
hero_src = r"d:\aadhi\Portfolio\Portfolio\assets\images\shapes\banner-three-man.png.png"
hero_dest = r"d:\aadhi\Portfolio\Portfolio\assets\images\shapes\banner-three-man.png"

if os.path.exists(hero_src):
    shutil.copyfile(hero_src, hero_dest)
    print("Hero animation photo fixed: banner-three-man.png")

# 2. Fix About section photo (about-three-thumb.jpg)
about_src = r"d:\aadhi\Portfolio\Portfolio\assets\images\thumbs\about-three-thumb.jpg.JPG"
about_dest = r"d:\aadhi\Portfolio\Portfolio\assets\images\thumbs\about-three-thumb.jpg"

if os.path.exists(about_src):
    shutil.copyfile(about_src, about_dest)
    print("About section photo fixed: about-three-thumb.jpg")

print("Both profile photos successfully restored with exact filenames!")
