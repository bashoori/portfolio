# 🚚 CSV to SQLite ETL Pipeline

This beginner-friendly project demonstrates a complete ETL pipeline using Python. The pipeline extracts shipment data from a CSV file, transforms (cleans) it, and loads it into a SQLite database for analysis.

---

## 📊 Use Case
A logistics company tracks its daily shipments via CSV logs. This project helps automate the process of loading those logs into a database for reporting.

---

## 🛠 Tools Used
- Python
- Pandas
- SQLite (via `sqlite3`)
- Modular ETL structure

---

## 📁 Project Structure
```
├── data/              # Raw CSV file
├── etl/               # ETL scripts (extract, transform, load)
├── output/            # Output SQLite DB file
├── scenario.md        # Business context + objectives
├── README.md          # This file
└── requirements.txt   # Python dependencies
```
---

## 🚀 How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```
2. Run the full pipeline
```bash
cd etl
python load.py
```
After running, you’ll find the SQLite database in:
```bash
output/shipments.db
```

🧪 Sample Query
```
SELECT destination, COUNT(*) as total_shipments
FROM shipments
GROUP BY destination
ORDER BY total_shipments DESC;
```