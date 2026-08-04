import urllib.request
import os

thumb_dir = r"d:\aadhi\Portfolio\Portfolio\assets\images\thumbs"

images = {
    "portfolio-three-thumb1.jpg": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=1000&auto=format&fit=crop", # Data Analytics Dashboard (Oasis Infobyte)
    "portfolio-three-thumb2.jpg": "https://images.unsplash.com/photo-1552519507-da3b142c6e3d?q=80&w=1000&auto=format&fit=crop"  # Automotive & Enterprise System (Ford)
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

for filename, url in images.items():
    dest_path = os.path.join(thumb_dir, filename)
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response, open(dest_path, "wb") as out_file:
            out_file.write(response.read())
        print(f"Successfully saved {filename}")
    except Exception as e:
        print(f"Error downloading {filename}: {e}")
