import urllib.request
import os

thumb_path = r"d:\aadhi\Portfolio\Portfolio\assets\images\thumbs\portfolio-three-thumb1.jpg"

# Direct URL for Oasis Infobyte logo image
logo_url = "https://oasisinfobyte.com/images/logo.png"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

try:
    req = urllib.request.Request(logo_url, headers=headers)
    with urllib.request.urlopen(req) as response, open(thumb_path, "wb") as out_file:
        out_file.write(response.read())
    print("Oasis Infobyte logo downloaded successfully!")
except Exception as e:
    print(f"Error: {e}")
