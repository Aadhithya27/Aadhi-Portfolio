import urllib.request
import os

thumb_dir = r"d:\aadhi\Portfolio\Portfolio\assets\images\thumbs"

# Clean high-res visual assets for the 6 hover items
images = {
    "feature-three-thumb1.jpg": "https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?q=80&w=1000&auto=format&fit=crop", # Interior & Furniture Design (Apoorvaa)
    "portfolio-two-thumb1.jpg": "https://images.unsplash.com/photo-1542751371-adc38448a05e?q=80&w=1000&auto=format&fit=crop", # Gaming & Battle Circuit Esports Poster (Infovista)
    "portfolio-two-thumb2.jpg": "https://images.unsplash.com/photo-1581092160607-ee22621dd758?q=80&w=1000&auto=format&fit=crop", # Industrial Calibrator & Electronics (ATOM)
    "portfolio-two-thumb3.jpg": "https://images.unsplash.com/photo-1552728089-57bdde30beb3?q=80&w=1000&auto=format&fit=crop", # Bird & Animal Rescue Sanctuary (Praani News)
    "portfolio-two-thumb4.jpg": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=1000&auto=format&fit=crop", # Web Development Service & Analytics (Web Dev Promo)
    "portfolio-thumb1.jpg": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?q=80&w=1000&auto=format&fit=crop"      # Wooden Architectural Interior Render (3D Architecture)
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

for filename, url in images.items():
    dest_path = os.path.join(thumb_dir, filename)
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response, open(dest_path, "wb") as out_file:
            out_file.write(response.read())
        print(f"Successfully updated hover reveal image: {filename}")
    except Exception as e:
        print(f"Error downloading {filename}: {e}")

