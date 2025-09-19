"""
Bronze JSONL -> Silver CSV (cleaned/normalized).

Input :
  data/s3/bronze/bronze_YYYYMMDD.jsonl
Output:
  data/s3/silver/silver_YYYYMMDD.csv

NOW SUPPORTS: --date YYYYMMDD (defaults to today UTC)
"""

import argparse
from datetime import datetime, timezone
from utils import read_jsonl, bronze_path_for_date, silver_path_for_date, write_csv, ensure_dirs

REQUIRED = ["ts","player_id","event","platform","region","session_id"]

def main(yyyymmdd:str|None):
    ensure_dirs()
    target = yyyymmdd or datetime.now(timezone.utc).strftime("%Y%m%d")
    bronze = bronze_path_for_date(target)
    silver = silver_path_for_date(target)

    if not bronze.exists():
        print("[silver] no bronze file for target date.")
        return

    rows = []
    for obj in read_jsonl(bronze):
        if not all(k in obj for k in REQUIRED):
            continue
        rows.append({
            "ts": obj.get("ts"),
            "player_id": obj.get("player_id"),
            "event": obj.get("event"),
            "platform": obj.get("platform"),
            "region": obj.get("region"),
            "session_id": obj.get("session_id"),
            "sku": obj.get("sku",""),
            "price": float(obj.get("price", 0) or 0),
            "currency": obj.get("currency",""),
            # dt is derived from file's target date to simulate day-based partitioning
            "dt": f"{target[:4]}-{target[4:6]}-{target[6:8]}",
        })

    if rows:
        write_csv(
            silver,
            fieldnames=["ts","player_id","event","platform","region","session_id","sku","price","currency","dt"],
            rows=rows
        )
        print(f"[silver] wrote {len(rows)} rows → {silver}")
    else:
        print("[silver] nothing transformed.")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", type=str, default=None, help="YYYYMMDD (optional)")
    args = ap.parse_args()
    main(args.date)
