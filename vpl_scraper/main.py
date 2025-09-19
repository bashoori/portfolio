'''📌 main.py: The Entry Point
	•	This is your controller or driver script.
	•	It coordinates the workflow: fetch the main page, extract links, scrape each branch, save to CSV.
	•	Keeps logic clean and easy to run: python main.py '''

# vpl_scraper/main.py
"""
Main script for scraping Vancouver Public Library branch data.
It coordinates fetching, parsing, and saving results to a CSV and Excel file.
Includes enrichment: operating hours, accessibility, manager contact, transit info.
"""
import os
import time
import logging
import pandas as pd
from bs4 import BeautifulSoup
import requests
from scraper.fetcher import fetch_main_page, fetch_branch_page
from scraper.parser import parse_main_page

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Headers to mimic a real browser
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/122.0.0.0 Safari/537.36"
}

def enrich_branch_data(url):
    """
    Extract extended branch data: operating hours, accessibility, contact, transit.
    Implements retry logic for resilient scraping.
    """
    retries = 3
    for attempt in range(retries):
        try:
            response = requests.get(url, headers=HEADERS, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "lxml")

            # Extract name
            name = soup.find("h1").get_text(strip=True) if soup.find("h1") else "N/A"

            # Address
            address_elem = soup.select_one(".location-address")
            address = address_elem.get_text(" ", strip=True) if address_elem else "N/A"

            # Phone & Email
            phone = soup.select_one("a[href^='tel:']")
            email = soup.select_one("a[href^='mailto:']")
            phone_text = phone.get_text(strip=True) if phone else "N/A"
            email_text = email.get_text(strip=True) if email else "N/A"

            # Operating hours
            hours_elem = soup.select_one(".hours-block")
            hours = hours_elem.get_text(" ", strip=True) if hours_elem else "N/A"

            # Accessibility
            accessibility_elem = soup.find("div", class_="accessibility")
            accessibility = accessibility_elem.get_text(" ", strip=True) if accessibility_elem else "N/A"

            # Contact / Manager info
            contact = "N/A"
            for p in soup.find_all("p"):
                if "manager" in p.get_text(strip=True).lower():
                    contact = p.get_text(" ", strip=True)
                    break

            # Transit / Parking
            transit_elem = soup.find("div", class_="transit")
            transit = transit_elem.get_text(" ", strip=True) if transit_elem else "N/A"

            return {
                "Branch Name": name,
                "Address": address,
                "Phone": phone_text,
                "Email": email_text,
                "Operating Hours": hours,
                "Accessibility": accessibility,
                "Branch Contact": contact,
                "Transit / Parking": transit,
                "Page URL": url
            }

        except Exception as e:
            logging.warning(f"Attempt {attempt+1} failed for {url}: {e}")
            time.sleep(2 * (attempt + 1))
    return {
        "Branch Name": "Error",
        "Address": "Error",
        "Phone": "Error",
        "Email": "Error",
        "Operating Hours": "Error",
        "Accessibility": "Error",
        "Branch Contact": "Error",
        "Transit / Parking": "Error",
        "Page URL": url
    }

def main():
    print("\U0001F50D Fetching main page...")
    html = fetch_main_page()
    branch_links = parse_main_page(html)
    print(f"\U0001F517 Found {len(branch_links)} branch pages.")

    all_data = []
    for idx, url in enumerate(branch_links):
        print(f"\U0001F4C4 Scraping [{idx + 1}/{len(branch_links)}]: {url}")
        branch_data = enrich_branch_data(url)
        all_data.append(branch_data)

    df = pd.DataFrame(all_data)

    # Ensure output directory exists
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/output.csv", index=False)
    df.to_excel("data/output.xlsx", index=False)
    print("\u2705 Done! Data saved to data/output.csv and output.xlsx")

if __name__ == "__main__":
    main()
