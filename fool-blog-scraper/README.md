# 📰 Fool Blog Scraper

Scrape up to 1,000 blog articles from [Fool.com](https://www.fool.com) — including titles, full article text, and URLs — and save them into a structured CSV file.

---

## 🚀 Project Summary

This script takes a list of URLs (provided in a `.txt` file) and scrapes each one for:

- 🧠 **Title**
- ✍️ **Full article text**
- 🔗 **URL**

It then saves everything into a CSV file for easy analysis or downstream processing.

---

## 📦 Features

- Scrapes articles quickly and reliably
- Uses `requests` and `BeautifulSoup` for HTML parsing
- Handles minor errors gracefully
- Outputs clean, structured `.csv` file

---

## 🛠️ Requirements

Install dependencies using pip:

```bash
pip install -r requirements.txt