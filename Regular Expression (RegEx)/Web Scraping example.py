import re
import requests

# -------------------------------
# Fetch a sample web page (example.com)
# -------------------------------

url = "https://www.example.com"
response = requests.get(url)
html = response.text

print("===== Raw HTML Fetched =====")
print(html[:200], "...")  # Print first 200 chars

# -------------------------------
# 1️⃣ Extract all <h1> headings
# -------------------------------

h1_pattern = r"<h1[^>]*>(.*?)</h1>"
h1s = re.findall(h1_pattern, html, flags=re.IGNORECASE | re.DOTALL)
print("\nH1 Headings:", h1s)

# -------------------------------
# 2️⃣ Extract all <a href="...">
# -------------------------------

a_href_pattern = r'<a[^>]+href=["\'](.*?)["\']'
links = re.findall(a_href_pattern, html, flags=re.IGNORECASE)
print("\nLinks:", links)

# -------------------------------
# 3️⃣ Extract all <img src="...">
# -------------------------------

img_src_pattern = r'<img[^>]+src=["\'](.*?)["\']'
images = re.findall(img_src_pattern, html, flags=re.IGNORECASE)
print("\nImage Sources:", images)
