'''✅ parser.py: Extracts Data from HTML
	•	Uses BeautifulSoup to extract content
	•	Functions like:
	•	parse_main_page(html) → gets branch links
	•	parse_branch_page(html, url) → extracts info per branch
	•	Keeps all parsing logic in one file, so it’s easy to:
	•	Improve regex or tag selection
	•	Unit test parsing on saved HTML snippets '''

# scraper/parser.py

from bs4 import BeautifulSoup

def parse_main_page(html):
    soup = BeautifulSoup(html, "lxml")
    links = []
    for a in soup.select("a[href^='/location/']"):
        href = a.get("href")
        if href and href.startswith("/location/"):
            full_url = "https://www.vpl.ca" + href
            if full_url not in links:
                links.append(full_url)
    return links

def parse_branch_page(html, url):
    soup = BeautifulSoup(html, "lxml")

    # Name
    name = soup.find("h1").get_text(strip=True) if soup.find("h1") else "N/A"

    # Address
    address_elem = soup.select_one(".location-address")
    address = address_elem.get_text(" ", strip=True) if address_elem else "N/A"

    # Phone
    phone_elem = soup.select_one("a[href^='tel:']")
    phone = phone_elem.get_text(strip=True) if phone_elem else "N/A"

    # Email
    email_elem = soup.select_one("a[href^='mailto:']")
    email = email_elem.get_text(strip=True) if email_elem else "N/A"

    return {
        "Branch Name": name,
        "Address": address,
        "Phone": phone,
        "Email": email,
        "Page URL": url
    }