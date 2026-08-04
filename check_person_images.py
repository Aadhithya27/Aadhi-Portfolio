import os

files = [
    r"d:\aadhi\Portfolio\Portfolio\assets\images\shapes\banner-three-man.png",
    r"d:\aadhi\Portfolio\Portfolio\assets\images\thumbs\about-three-thumb.jpg",
    r"d:\aadhi\Portfolio\Portfolio\assets\images\thumbs\footer-three-thumb.jpg"
]

for f in files:
    if os.path.exists(f):
        size = os.path.getsize(f)
        mtime = os.path.getmtime(f)
        print(f"File: {f} | Size: {size} bytes | MTime: {mtime}")
    else:
        print(f"File: {f} NOT FOUND!")
