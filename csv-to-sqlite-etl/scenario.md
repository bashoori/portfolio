# 🎯 Project Scenario – CSV to SQLite ETL Pipeline

## 🧩 Business Context:
A small logistics company manually collects shipment logs each day and stores them as CSV files. Their analysts want the data centralized in a structured database to run daily reports.

## 🎯 Objective:
Build an ETL pipeline in Python that:
- Extracts shipment data from CSV files
- Cleans and transforms the data (e.g. standardize date format, remove nulls)
- Loads it into a SQLite database for querying

## 🛠️ Tools Used:
- Python
- Pandas
- SQLite (via `sqlite3`)

## 🧪 Sample Dataset:
- Columns: `shipment_id`, `origin`, `destination`, `departure_date`, `arrival_date`, `status`
- File: `data/shipments.csv`

## ✅ Output:
- SQLite database file: `output/shipments.db`
- Cleaned and structured data table: `shipments`

## 📈 Bonus:
Add a summary SQL query that shows the number of shipments per destination city.