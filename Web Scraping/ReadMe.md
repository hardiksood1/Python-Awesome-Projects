# Web Scraper: Extract Important Details & Website Type
---
## Overview
This Python project allows users to scrape important details from any website and store the extracted information in both CSV and SQLite database. It also automatically detects the type of website (e.g., Blog, E-commerce, News, Portfolio, Educational) based on the URL and content.

---

## Features
- Dynamic scraping of most important content from any website.
- Detection of website type using URL patterns and content heuristics.
- Saves data to CSV (important_scraped_data.csv) and SQLite (important_scraped_data.db).
- Easy to extend for additional metadata or dynamic content scraping.

---

## Requirements
- Python 3.8+
- Required Python libraries:
```
requests
beautifulsoup4
```
Install dependencies using:
```
pip install -r requirements.txt
```

---

## Usage
1. Clone or download the repository.
2. Run the Python script:
```
python web_scraper.py
```
3. Enter the URL you want to scrape when prompted.
4. The script will fetch, parse, and save the data to both CSV and SQLite.

CSV columns include:
site_name, title, meta_description, meta_keywords, meta_author, headings, paragraphs, links, images, og_tags, website_type

---

## Sample Output
CSV row example:
```
site_name: example.com
title: Example Domain
meta_description: This domain is for use in illustrative examples in documents.
meta_keywords: example, domain
meta_author: John Doe
headings: h1: Example Domain
paragraphs: This domain is for use in illustrative examples in documents.
links: https://www.iana.org/domains/example
images: https://example.com/image.png (Example Image)
og_tags: {'og:title': 'Example Domain', 'og:description': 'Illustrative Example'}
website_type: Blog/News
```
---

## Project Structure
```
web-scraper/
├── web_scraper.py          # Main Python scraping script
├── requirements.txt        # Required Python libraries
├── important_scraped_data.csv  # CSV output
└── important_scraped_data.db   # SQLite database
```
---