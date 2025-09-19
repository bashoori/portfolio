"""
📄 query_sqlite.py

This script connects to the fhir_data.db SQLite database and runs sample SQL queries,
printing the results to the terminal.

Author: Bita Ashoori
"""

import sqlite3
import pandas as pd

DB_FILE = "../data/output/fhir_data.db"

# Connect to the database
conn = sqlite3.connect(DB_FILE)

# Sample queries to explore your data
sample_queries = {
    "All female patients": "SELECT * FROM patients WHERE Gender = 'female';",
    "All conditions with clinical status 'active'": "SELECT * FROM conditions WHERE [Clinical Status] = 'active';",
    "Top 5 observations": "SELECT * FROM observations LIMIT 5;",
    "Recent encounters": "SELECT * FROM encounters ORDER BY [Start Time] DESC LIMIT 5;"
}

print(f"🔍 Querying database: {DB_FILE}\n")

for label, query in sample_queries.items():
    print(f"📌 {label}")
    try:
        df = pd.read_sql(query, conn)
        print(df.to_markdown(index=False))
    except Exception as e:
        print(f"⚠️ Error running query: {e}")
    print("\n" + "-"*60 + "\n")

conn.close()
print("✅ Done querying.")
