"""
Simulates Kinesis -> S3 Bronze copy.

Inputs:
  data/kinesis_stream/stream_YYYYMMDD.jsonl
Outputs:
  data/s3/bronze/bronze_YYYYMMDD.jsonl

NOW SUPPORTS: --date YYYYMMDD (defaults to today UTC)
"""

import argparse
from datetime import datetime, timezone
from utils import list_stream_files, bronze_path_for_date, append_lines, ensure_dirs

def main(yyyymmdd:str|None):
    ensure_dirs()
    target = yyyymmdd or datetime.now(timezone.utc).strftime("%Y%m%d")
    bronze_path = bronze_path_for_date(target)

    lines = []
    for p in list_stream_files():
        if target in p.name:
            with p.open("r", encoding="utf-8") as f:
                lines.extend(f.readlines())

    if lines:
        append_lines(bronze_path, lines)
        print(f"[bronze] appended {len(lines)} lines → {bronze_path}")
    else:
        print("[bronze] no new lines.")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", type=str, default=None, help="YYYYMMDD (optional)")
    args = ap.parse_args()
    main(args.date)
