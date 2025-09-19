'''✅ fetcher.py: Handles Network Requests
	•	Separates the HTTP logic from parsing or output logic.
	•	Functions like fetch_main_page() and fetch_branch_page(url):
	•	Handle requests.get()
	•	Raise errors if a page fails to load
	•	This modularity helps if you later:
	•	Switch to Playwright or Selenium (just update fetcher.py)
	•	Add retry logic or proxies '''

# scraper/fetcher.py

import requests

BASE_URL = "https://www.vpl.ca/hours-locations"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " 
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/122.0.0.0 Safari/537.36"
}

def fetch_main_page():
    response = requests.get(BASE_URL, headers=HEADERS)
    response.raise_for_status()
    return response.text

def fetch_branch_page(url):
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.text