# 📚 Vancouver Public Library Scraper

This Python project scrapes detailed information about all public library branches listed on the [Vancouver Public Library website](https://www.vpl.ca/hours-locations). It collects data such as branch name, address, contact info, and more. The results are exported to both a structured CSV and Excel file.

---

## 🚀 Features

- Extracts all branch links from the main library directory page
- Enriches each branch with the following details:
  - Branch Name
  - Address
  - Phone Number
  - Email
  - Operating Hours ✅
  - Accessibility Features ✅
  - Branch Manager or Contact Name ✅
  - Public Transit or Parking Options ✅
- Retry logic with logging for robust scraping ✅
- Exports to both CSV and Excel formats ✅

---

## 🛠️ Tech Stack

- Python 3.x
- [Requests](https://docs.python-requests.org/en/latest/)
- [BeautifulSoup (bs4)](https://www.crummy.com/software/BeautifulSoup/)
- [Pandas](https://pandas.pydata.org/)
- [Openpyxl](https://openpyxl.readthedocs.io/en/stable/) (for Excel output)

---

## 📁 Project Structure

```
vpl_scraper/
├── main.py                # Main script: orchestrates scraping and saving
├── scraper/
│   ├── fetcher.py         # Handles HTTP requests
│   └── parser.py          # Parses main directory for branch links
├── data/
│   ├── output.csv         # CSV output
│   └── output.xlsx        # Excel output
├── requirements.txt       # Python dependencies
└── README.md              # Documentation
```

---

## ⚙️ Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/vpl_scraper.git
   cd vpl_scraper
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the scraper:**
   ```bash
   python main.py
   ```

4. **Check the output:**
   - `data/output.csv`
   - `data/output.xlsx`

---

## 📝 Sample Output (CSV & Excel)

| Branch Name      | Address                               | Phone        | Email        | Operating Hours | Accessibility | Branch Contact | Transit / Parking |
|------------------|----------------------------------------|--------------|--------------|------------------|----------------|------------------|--------------------|
| Central Library  | 350 W Georgia St, Vancouver, BC V6B... | 604-331-3603 | info@vpl.ca  | Mon-Fri: 10-6    | Wheelchair access | Jane Doe       | Near SkyTrain     |

---

## 🔄 Future Enhancements

- [ ] Save raw HTML per branch for offline parsing
- [ ] Upload to Google Sheets via `gspread`
- [ ] Command-line argument to scrape a specific branch only
- [ ] Logging to file instead of stdout

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙋‍♀️ Author

Built with ❤️ by [Bita Ashoori](https://github.com/bashoori)
