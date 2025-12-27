# Data Engineering Portfolio — Bita Ashoori

Production-style data engineering projects focused on ingestion, transformation, orchestration, and analytics.

Each project models real-world data problems and operational tradeoffs rather than toy examples or isolated scripts.

---

## Selected Projects

### Airflow AWS Modernization

![Airflow AWS Modernization Architecture](images/airflow-aws-modernization.png)

**Stack:** Airflow, Docker, AWS S3  
Modernized legacy batch jobs into orchestrated Airflow DAGs with cloud storage integration. Emphasis on scheduling, dependency management, retries, and operational reliability.

---

### Cloud ETL Modernization (Airflow + AWS)

![Cloud ETL Modernization Architecture](images/cloud-etl-modernization.png)

**Stack:** Python, Airflow, AWS  
End-to-end ETL pipeline ingesting API data, transforming it, and loading curated datasets into cloud storage and databases. Built with modular components to support reuse and change.

---

### Healthcare FHIR Data Pipeline

![Healthcare FHIR Data Pipeline Architecture](images/healthcare-fhir-pipeline.png)

**Stack:** Python, Pandas, SQLite, Streamlit  
Processes FHIR-formatted healthcare JSON into structured analytical tables and dashboards. Focuses on schema normalization, data quality, and healthcare data complexity.

---

### Real-Time Marketing Data Pipeline

![Real-Time Marketing Data Pipeline Architecture](images/real-time-marketing-pipeline.png)

**Stack:** Airflow, Docker, SQL  
Simulates near real-time marketing events and processes them through scheduled pipelines. Demonstrates time-window aggregation, transformation logic, and analytics readiness.

---

### Customer Insights Pipeline

![Customer Insights Pipeline Architecture](images/customer-insights-pipeline.png)

**Stack:** Python, PostgreSQL, Airflow  
Integrates multiple customer data sources into unified reporting tables. Emphasis on joins, data modeling, and analytics-friendly schema design.

---

### PySpark Sales Pipeline

![PySpark Sales Pipeline Architecture](images/pyspark-sales-pipeline.png)

**Stack:** PySpark, Delta Lake  
Distributed pipeline transforming raw sales data into cleaned, analytics-ready layers. Demonstrates scalable processing patterns and layered data architecture.

---

### AWS Lambda LinkedIn Job Scraper

![AWS Lambda Job Scraper Architecture](images/aws-lambda-job-scraper.png)

**Stack:** AWS Lambda, Python, S3  
Serverless scraper extracting job postings and storing structured outputs in cloud storage. Designed to demonstrate automation and event-driven architecture.

---

### Patient Engagement Analytics

![Patient Engagement Analytics Pipeline](images/patient-engagement-analytics.png)

**Stack:** SQL, Pandas  
ETL workflow analyzing patient engagement behavior across healthcare datasets for trend analysis and reporting.

---

### eBay Product Tracker

![eBay Product Tracker Pipeline](images/ebay-product-tracker.png)

**Stack:** Python, BeautifulSoup  
Web scraper tracking product listings and pricing changes with structured, queryable output.

---

### Vancouver Public Library Scraper

![Vancouver Public Library Scraper Pipeline](images/vpl-scraper.png)

**Stack:** Python, BeautifulSoup  
Scrapes and enriches public library book metadata for local data exploration and enrichment.

---

## How to Read This Repository

Each project includes:
- A clear problem definition  
- Data sources and assumptions  
- Transformation and modeling logic  
- Notes on tradeoffs and design decisions  

Projects are updated continuously as new tools and patterns are learned.

---

## Links

- GitHub: https://github.com/bashoori  
- Live Portfolio: https://bashoori.github.io/portfolio  
- LinkedIn: https://www.linkedin.com/in/bitaashoori
