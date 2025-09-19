"""
Load Gold CSV into SQLite (simulated Redshift), MERGE by dt.

Input : data/s3/gold/gold_agg_YYYYMMDD.csv
DB    : data/warehouse.db  (table fact_daily_kpis)

NOW SUPPORTS: --date YYYYMMDD (defaults to today UTC)
"""

import argparse, sqlite3, csv
from datetime import datetime, timezone
from utils import gold_path_for_date, WAREHOUSE_DB, ensure_dirs

DDL = """
CREATE TABLE IF NOT EXISTS fact_daily_kpis (
  dt TEXT PRIMARY KEY,
  dau INTEGER,
  events INTEGER,
  purchases INTEGER,
  revenue REAL
);
"""

UPSERT = """
INSERT INTO fact_daily_kpis (dt, dau, events, purchases, revenue)
VALUES (?, ?, ?, ?, ?)
ON CONFLICT(dt) DO UPDATE SET
  dau=excluded.dau,
  events=excluded.events,
  purchases=excluded.purchases,
  revenue=excluded.revenue;
"""

def main(yyyymmdd:str|None):
    ensure_dirs()
    target = yyyymmdd or datetime.now(timezone.utc).strftime("%Y%m%d")
    gold = gold_path_for_date(target)
    if not gold.exists():
        print("[warehouse] no gold file.")
        return

    conn = sqlite3.connect(WAREHOUSE_DB)
    cur = conn.cursor()
    cur.execute(DDL)

    with gold.open("r", encoding="utf-8") as f:
        r = csv.DictReader(f)
        rows = [(row["dt"], int(row["dau"]), int(row["events"]),
                 int(row["purchases"]), float(row["revenue"])) for row in r]

    cur.executemany(UPSERT, rows)
    conn.commit()
    conn.close()
    print(f"[warehouse] upserted {len(rows)} row(s) into {WAREHOUSE_DB}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", type=str, default=None, help="YYYYMMDD (optional)")
    args = ap.parse_args()
    main(args.date)
