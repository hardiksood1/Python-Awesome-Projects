import requests
from bs4 import BeautifulSoup
import csv
import sqlite3
from urllib.parse import urlparse

# ---------------------------
# 1. User input URL
# ---------------------------
url = input("Enter the URL to scrape: ")

# ---------------------------
# 2. Fetch page content
# ---------------------------
response = requests.get(url)
if response.status_code != 200:
    print(f"Failed to fetch the website. Status code: {response.status_code}")
    exit()

# ---------------------------
# 3. Parse HTML
# ---------------------------
soup = BeautifulSoup(response.text, "html.parser")

# ---------------------------
# 4. Extract important details
# ---------------------------

# Title
title = soup.title.string.strip() if soup.title else "No title found"

# Meta description
meta_desc = soup.find("meta", attrs={"name": "description"})
meta_desc = meta_desc.get("content", "").strip() if meta_desc else ""

# Meta keywords
meta_keywords = soup.find("meta", attrs={"name": "keywords"})
meta_keywords = meta_keywords.get("content", "").strip() if meta_keywords else ""

# Meta author
meta_author = soup.find("meta", attrs={"name": "author"})
meta_author = meta_author.get("content", "").strip() if meta_author else ""

# OpenGraph tags
og_tags = {}
for tag in soup.find_all("meta"):
    if tag.get("property", "").startswith("og:"):
        og_tags[tag.get("property")] = tag.get("content", "")

# Headings
headings = []
for tag in ["h1", "h2", "h3", "h4", "h5", "h6"]:
    for heading in soup.find_all(tag):
        headings.append(f"{tag}: {heading.text.strip()}")

# Paragraphs
paragraphs = [p.text.strip() for p in soup.find_all("p") if p.text.strip()]

# Links
links = [a.get("href") for a in soup.find_all("a", href=True)]

# Images
images = []
for img in soup.find_all("img"):
    src = img.get("src")
    alt = img.get("alt", "")
    if src:
        images.append(f"{src} ({alt})")

# Guess website type based on content
site_type = "Unknown"
domain = urlparse(url).netloc.lower()

if any(keyword in domain for keyword in ["blog", "medium", "wordpress"]):
    site_type = "Blog"
elif any(keyword in domain for keyword in ["shop", "store", "ecommerce", "cart"]):
    site_type = "E-commerce"
elif any(keyword in domain for keyword in ["news", "daily", "times"]):
    site_type = "News"
elif any(keyword in domain for keyword in ["portfolio", "resume"]):
    site_type = "Portfolio"
elif "edu" in domain or "school" in domain or "university" in domain:
    site_type = "Educational"

# Additional heuristic based on page content
if soup.find("article"):
    site_type = "Blog/News"

# ---------------------------
# 5. Structure data
# ---------------------------
data = {
    "site_name": domain,
    "title": title,
    "meta_description": meta_desc,
    "meta_keywords": meta_keywords,
    "meta_author": meta_author,
    "headings": headings,
    "paragraphs": paragraphs,
    "links": links,
    "images": images,
    "og_tags": og_tags,
    "website_type": site_type
}

# ---------------------------
# 6. Save to CSV
# ---------------------------
csv_file = "important_scraped_data.csv"
with open(csv_file, mode="a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    # Write header if file is empty
    file.seek(0)
    if file.tell() == 0:
        writer.writerow([
            "site_name", "title", "meta_description", "meta_keywords", "meta_author",
            "headings", "paragraphs", "links", "images", "og_tags", "website_type"
        ])
    writer.writerow([
        data["site_name"],
        data["title"],
        data["meta_description"],
        data["meta_keywords"],
        data["meta_author"],
        "; ".join(data["headings"]),
        "; ".join(data["paragraphs"]),
        "; ".join(data["links"]),
        "; ".join(data["images"]),
        str(data["og_tags"]),
        data["website_type"]
    ])

print(f"Data saved to CSV: {csv_file}")

# ---------------------------
# 7. Save to SQLite DB
# ---------------------------
conn = sqlite3.connect("important_scraped_data.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS website_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    site_name TEXT,
    title TEXT,
    meta_description TEXT,
    meta_keywords TEXT,
    meta_author TEXT,
    headings TEXT,
    paragraphs TEXT,
    links TEXT,
    images TEXT,
    og_tags TEXT,
    website_type TEXT
)
""")

cursor.execute("""
INSERT INTO website_data (
    site_name, title, meta_description, meta_keywords, meta_author,
    headings, paragraphs, links, images, og_tags, website_type
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", (
    data["site_name"],
    data["title"],
    data["meta_description"],
    data["meta_keywords"],
    data["meta_author"],
    "; ".join(data["headings"]),
    "; ".join(data["paragraphs"]),
    "; ".join(data["links"]),
    "; ".join(data["images"]),
    str(data["og_tags"]),
    data["website_type"]
))

conn.commit()
conn.close()
print("Data saved to SQLite DB: important_scraped_data.db")