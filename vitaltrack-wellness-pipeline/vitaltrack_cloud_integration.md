# ☁️ Connect Your VitalTrack Data Pipeline to BigQuery & Google Sheets

This guide shows how to extend your `VitalTrack Wellness Pipeline` to cloud destinations — so it powers dashboards, analytics, and ML workflows.

---

## ✅ Option A: Load Clean Data to Google Sheets (via Python + gspread)

1. 📦 Install required packages

```bash
pip install gspread oauth2client
```

2. 🔐 Create a Google Service Account and enable Sheets API
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project (e.g., `vitaltrack`)
   - Enable **Google Sheets API**
   - Create **Service Account Credentials**
   - Download `credentials.json`
   - Share your Google Sheet with the service email (`...@...gserviceaccount.com`)

3. 🧠 Python Snippet:

```python
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Authenticate
scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# Open Google Sheet
sheet = client.open("VitalTrack Dashboard").sheet1

# Upload DataFrame
df = pd.read_csv("flattened_activity.csv")  # your clean output
sheet.update([df.columns.values.tolist()] + df.values.tolist())
```

---

## ✅ Option B: Load to BigQuery

1. 📦 Install Google Cloud dependencies:

```bash
pip install google-cloud-bigquery pandas
```

2. 🔐 Set up GCP BigQuery:
   - Enable BigQuery API
   - Create a **BigQuery dataset** (e.g., `vitaltrack_raw`)
   - Download service credentials (`.json`)

3. 🧠 Python Snippet to Upload CSV → BigQuery:

```python
from google.cloud import bigquery
import pandas as pd

client = bigquery.Client.from_service_account_json("credentials.json")
df = pd.read_csv("flattened_activity.csv")

table_id = "your-project-id.vitaltrack_raw.activity_logs"

job = client.load_table_from_dataframe(df, table_id)
job.result()

print("✅ Data uploaded to BigQuery!")
```

---

## 🎯 Bonus Tip:

Once your data is in Google Sheets or BigQuery, you can:
- Connect it to **Looker Studio** for visualization
- Schedule updates via **Airflow** or **GitHub Actions**

Let me know if you want a visual dashboard walkthrough too!

