import os
import shutil

src_photo = r"d:\aadhi\Portfolio\Portfolio\assets\images\shapes\banner-three-man.png"
dest_photo = r"d:\aadhi\Portfolio\Portfolio\assets\images\thumbs\about-three-thumb.jpg"

if os.path.exists(src_photo):
    shutil.copyfile(src_photo, dest_photo)
    print(f"Successfully copied animation suit photo to {dest_photo}")
else:
    print("Source animation photo not found!")
