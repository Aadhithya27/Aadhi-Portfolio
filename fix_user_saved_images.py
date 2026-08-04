import os
import shutil

thumb_dir = r"d:\aadhi\Portfolio\Portfolio\assets\images\thumbs"

# Map of double extension files saved by Windows to their required html image filenames
mappings = [
    ("feature-three-thumb1.jpg.png", "feature-three-thumb1.jpg"), # Apoorvaa Poster
    ("portfolio-two-thumb1.jpg.png", "portfolio-two-thumb1.jpg"), # Infovista Poster
    ("portfolio-two-thumb1.jpg (2).png", "portfolio-two-thumb2.jpg"), # Atom Catalogue Poster (if 2nd file)
    ("portfolio-two-thumb3.jpg.png", "portfolio-two-thumb3.jpg"), # Praani News Poster
    ("portfolio-two-thumb4.jpg.png", "portfolio-two-thumb4.jpg"), # Web Dev Poster
    ("portfolio-thumb1.jpg.png", "portfolio-thumb1.jpg")          # Mandir 3D Architecture Poster
]

for src_name, target_name in mappings:
    src_path = os.path.join(thumb_dir, src_name)
    target_path = os.path.join(thumb_dir, target_name)
    
    if os.path.exists(src_path):
        shutil.copyfile(src_path, target_path)
        print(f"Successfully copied {src_name} -> {target_name}")

print("All user uploaded images have been assigned successfully!")
