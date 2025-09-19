"""
read_from_db.py

This script connects to the SQLite database and reads data
from the `shipments` table using optional SQL filters.

Author: Bita
Date: 2025-07
"""

import sqlite3
import pandas as pd
import os

def read_from_sqlite(db_path: str, table_name: str = "shipments", where_clause: str = "") -> pd.DataFrame:
    """
    Reads data from the specified table in SQLite with optional filters.

    Args:
        db_path (str): Path to the SQLite database
        table_name (str): Table name to read from
        where_clause (str): Optional SQL WHERE clause (without the "WHERE" keyword)

    Returns:
        pd.DataFrame: Resulting rows as DataFrame
    """
    try:
        conn = sqlite3.connect(db_path)

        query = f"SELECT * FROM {table_name}"
        if where_clause:
            query += f" WHERE {where_clause}"

        df = pd.read_sql(query, conn)
        conn.close()

        print(f"[INFO] Read {len(df)} rows using filter: {where_clause or 'None'}")
        return df
    except Exception as e:
        print(f"[ERROR] Failed to read from DB: {e}")
        return pd.DataFrame()


# Example filters for testing
if __name__ == "__main__":
    db_path = os.path.join("output", "shipments.db")

    print("\n🔹 Delivered shipments:")
    delivered_df = read_from_sqlite(db_path, where_clause="status = 'Delivered'")
    print(delivered_df)

    print("\n🔹 Shipments to 'Vancouver':")
    to_vancouver_df = read_from_sqlite(db_path, where_clause="destination = 'Vancouver'")
    print(to_vancouver_df)

    print("\n🔹 Shipments in June 2024:")
    june_df = read_from_sqlite(db_path, where_clause="""
        departure_date >= '2024-06-01' AND departure_date < '2024-07-01'
    """)
    print(june_df)