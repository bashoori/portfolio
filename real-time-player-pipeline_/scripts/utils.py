"""
Utility helpers. Works both:
 - Outside Docker (paths from local .env or defaults)
 - Inside Docker (mounted .env at /opt/airflow/.env)

In docker-compose we mount:
  ../data    -> /opt/airflow/data
  ../scripts -> /opt/airflow/scripts
"""

import os, json, csv
from datetime import datetime, timezone
from pathlib import Path
from dotenv import load_dotenv

# Load .env (in Docker it's /opt/airflow/.env; outside it's project .env if present)
load_dotenv(dotenv_path=os.getenv("ENV_PATH"), override=True)
load_dotenv(override=True)  # fallback to current dir

DATA_DIR   = Path(os.getenv("DATA_DIR", "./data"))
STREAM_DIR = Path(os.getenv("STREAM_DIR", str(DATA_DIR / "kinesis_stream")))
S3_BRONZE  = Path(os.getenv("S3_BRONZE", str(DATA_DIR / "s3/bronze")))
S3_SILVER  = Path(os.getenv("S3_SILVER", str(DATA_DIR / "s3/silver")))
S3_GOLD    = Path(os.getenv("S3_GOLD", str(DATA_DIR / "s3/gold")))
WAREHOUSE_DB = Path(os.getenv("WAREHOUSE_DB", str(DATA_DIR / "warehouse.db")))
STREAM_BASENAME = os.getenv("STREAM_BASENAME", "stream")
COPY_WINDOW_MIN = int(os.getenv("COPY_WINDOW_MIN", "5"))

def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")

def ensure_dirs():
    for p in (DATA_DIR, STREAM_DIR, S3_BRONZE, S3_SILVER, S3_GOLD):
        p.mkdir(parents=True, exist_ok=True)

def list_stream_files():
    return sorted(STREAM_DIR.glob("*.jsonl"))

def bronze_path_for_date(date_str: str) -> Path:
    return S3_BRONZE / f"bronze_{date_str}.jsonl"

def silver_path_for_date(date_str: str) -> Path:
    return S3_SILVER / f"silver_{date_str}.csv"

def gold_path_for_date(date_str: str) -> Path:
    return S3_GOLD / f"gold_agg_{date_str}.csv"

def read_jsonl(path: Path):
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                yield json.loads(line)
            except Exception:
                # skip malformed
                continue

def append_lines(path: Path, lines):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        for ln in lines:
            f.write(ln.rstrip("\n") + "\n")

def write_csv(path: Path, fieldnames, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow(r)
