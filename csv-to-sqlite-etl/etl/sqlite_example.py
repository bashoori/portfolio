import sqlite3
import os

# Create or connect to a local SQLite database file
db_path = os.path.join("output", "example.db")
os.makedirs("output", exist_ok=True)
conn = sqlite3.connect(db_path)

cur = conn.cursor()

# 1. Create a table
cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    );
""")

# 2. Insert some sample users
sample_data = [
    ("Bita", "bita@example.com"),
    ("Elham", "elham@example.com"),
    ("Masoumeh", "masoumeh@example.com")
]

cur.executemany("INSERT OR IGNORE INTO users (name, email) VALUES (?, ?);", sample_data)

# 3. Read from the table
cur.execute("SELECT * FROM users;")
rows = cur.fetchall()

print("📦 Users in database:")
for row in rows:
    print(row)

# 4. Close connection
conn.commit()
cur.close()
conn.close()