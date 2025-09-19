<div style="display: flex; align-items: center; justify-content: space-between; width: 100%; padding: 20px 0; border-bottom: 2px solid #f0f0f0;">
  <!-- Left section: Name & Title -->
  <div style="flex: 1;">
    <h1 style="margin: 0; font-size: 2.2em; font-weight: 700; color: #333;">Bita Ashoori</h1>
    <span style="font-size: 1.4em; font-weight: 400; color: #555;">💼 Data Engineering Portfolio</span>
  </div>

  <!-- Right section: Profile Image -->
  <div style="flex-shrink: 0; margin-left: 20px;">
    <img src="https://raw.githubusercontent.com/bashoori/data-engineering-portfolio/main/docs/images/IMG_9043.JPG"
         width="220"
         alt="Bita Ashoori"
         style="border-radius: 50%; border: 2px solid #e0e0e0; box-shadow: 0 6px 12px rgba(0,0,0,0.15);" />
  </div>
</div>


## About Me

I’m a Data Engineer based in Vancouver with over 5 years of experience in data engineering, business intelligence, and analytics. I focus on designing cloud-native data pipelines and automating workflows that turn raw data into actionable insights. My background spans healthcare, retail, consumer services, and public-sector projects, giving me a broad perspective on real-world data challenges. I bring 3+ years of experience building and maintaining cloud pipelines and 2+ years as a BI/ETL Developer. Skilled in Python, SQL, Apache Airflow, and AWS (S3, Lambda, Redshift), I specialize in modern data orchestration and automation.

## Contact Me 

💻 Explore my work on [GitHub](https://github.com/bashoori)  
🔗 Connect with me on [LinkedIn](https://www.linkedin.com/in/bitaashoori)  
📧 Contact me at [bitaashoori20@gmail.com](mailto:bitaashoori20@gmail.com)  
📄 [Download My Resume](https://raw.githubusercontent.com/bashoori/data-engineering-portfolio/main/docs/images/BitaAshoori-DataEngineer-resume%20(1).pdf)

---

## Project Highlights  

### 🎮 Real-Time Player Pipeline  

**Scenario**: Gaming companies require real-time analytics on player activity to optimize engagement, matchmaking, and monetization.  
📎[GitHub Repo](https://github.com/bashoori/data-engineering-portfolio/tree/main/real-time-player-pipeline)  
**Solution**: Built a simulated real-time data pipeline that streams player events into a data lake, applies aggregations, and provides analytics-ready data.  
✅ **Potential Impact**: Enables near real-time dashboards for player activity, reducing reporting lag from hours to seconds and enhancing player retention strategies.  

🧰 **Stack**: Apache Kafka (or Kinesis), AWS S3, DynamoDB, Airflow, Spark  
🧪 **Tested On**: Local Kafka + AWS localstack + GitHub Codespaces  

<p align="center">
  <img src="https://raw.githubusercontent.com/bashoori/data-engineering-portfolio/main/docs/images/Real-Time-Player.png" alt="Real-Time Player Pipeline Diagram" width="700" style="border: 1px solid #ccc; border-radius: 6px;" />
</p>

---

### 🛠️ Airflow AWS Modernization  

**Scenario**: Businesses needed faster feedback loops from ad campaigns to optimize performance and engagement.  
📎[GitHub Repo](https://github.com/bashoori/data-engineering-portfolio/tree/main/airflow-aws-modernization)  
**Solution**: Migrated legacy Windows Task Scheduler jobs into modular Airflow DAGs with Docker and AWS S3.  
✅ **Potential Impact**: Could reduce manual errors by up to 50% and improve job monitoring and reliability in real-world environments.  

🧰 **Stack**: Python, Apache Airflow, Docker, AWS S3  
🧪 **Tested On**: Local Docker, GitHub Codespaces  

<p align="center">
  <img src="https://raw.githubusercontent.com/bashoori/data-engineering-portfolio/main/docs/images/etl2.png" alt="Airflow AWS Diagram" width="700" style="border: 1px solid #ccc; border-radius: 6px;" />
</p>

---

### ☁️ Cloud ETL Modernization  

**Scenario**: Legacy workflows lacked observability, scalability, and centralized monitoring—critical for modern data teams.  
📎[GitHub Repo](https://github.com/bashoori/data-engineering-portfolio/tree/main/cloud-etl-modernization-airflow-aws)  
**Solution**: Built a scalable and maintainable ETL pipeline for structured data movement from APIs to Redshift with alerting via CloudWatch.  
✅ **Potential Impact**: Should improve troubleshooting efficiency by ~30% with enhanced logging and monitoring practices.  

🧰 **Stack**: Apache Airflow, AWS Redshift, CloudWatch  
🧪 **Tested On**: AWS Free Tier, Docker  

<p align="center">
  <img src="https://raw.githubusercontent.com/bashoori/data-engineering-portfolio/main/docs/images/CloudETLModernization.png" alt="Cloud ETL Diagram" width="700" style="border: 1px solid #ccc; border-radius: 6px;" />
</p>

---

### ⚡ Real-Time Marketing Pipeline  

**Scenario**: Businesses needed faster feedback loops from ad campaigns to optimize performance and engagement.  
📎[GitHub Repo](https://github.com/bashoori/data-engineering-portfolio/tree/main/real-time-marketing-pipeline)  
**Solution**: Simulates real-time ingestion of campaign data, transforming and storing insights using PySpark and Delta Lake.  
✅ **Potential Impact**: May reduce reporting lag from 24 hours to 1 hour, enabling faster marketing insights and campaign optimization.  

🧰 **Stack**: PySpark, Databricks, GitHub Actions, AWS S3  
🧪 **Tested On**: Databricks Community Edition, GitHub CI/CD  

<p align="center">
  <img src="https://raw.githubusercontent.com/bashoori/data-engineering-portfolio/main/docs/images/image1.png" alt="Real-Time Pipeline Diagram" width="700" style="border: 1px solid #ccc; border-radius: 6px;" />
</p>

---

### 🏥 FHIR Healthcare Pipeline  

**Scenario**: Healthcare projects using FHIR data require a clean, structured pipeline to support downstream analytics and ML.  
📎[GitHub Repo](https://github.com/bashoori/data-engineering-portfolio/tree/main/healthcare-FHIR-data-pipeline)  
**Solution**: Processes synthetic healthcare records in FHIR JSON format and converts them into clean, queryable relational tables.  
✅ **Potential Impact**: Designed to reduce preprocessing time by 60% and prepare healthcare data for analytics and ML workloads.  

🧰 **Stack**: Python, Pandas, Synthea, SQLite, Streamlit  
🧪 **Tested On**: Local + Streamlit + BigQuery-compatible  

<p align="center">
  <img src="https://raw.githubusercontent.com/bashoori/data-engineering-portfolio/main/docs/images/etl4.png" alt="FHIR Pipeline Diagram" width="700" style="border: 1px solid #ccc; border-radius: 6px;" />
</p>

---

### 📈 PySpark Sales Pipeline  

**Scenario**: Businesses need scalable ETL systems to process large sales datasets for timely business intelligence reporting.  
📎[GitHub Repo](https://github.com/bashoori/data-engineering-portfolio/tree/main/pyspark-sales-pipeline)  
**Solution**: A production-ready PySpark ETL that ingests and transforms high-volume sales data into Delta Lake for BI.  
✅ **Potential Impact**: Built to cut transformation runtimes by 40% and improve sales reporting accuracy through Delta Lake optimization.  

🧰 **Stack**: PySpark, Delta Lake, AWS S3  
🧪 **Tested On**: Local Databricks + S3  

<p align="center">
  <img src="https://raw.githubusercontent.com/bashoori/data-engineering-portfolio/main/docs/images/etl6.png" alt="PySpark Pipeline Diagram" width="700" style="border: 1px solid #ccc; border-radius: 6px;" />
</p>

---

### 🔍 LinkedIn Scraper (Lambda)  

**Scenario**: Manual job tracking and lead sourcing is time-consuming and unscalable.  
📎[GitHub Repo](https://github.com/bashoori/data-engineering-portfolio/tree/main/linkedIn-job-scraper)  
**Solution**: Automates job scraping from LinkedIn using serverless AWS Lambda and stores structured output in S3.  
✅ **Potential Impact**: Can automate job scraping workflows and enable structured job search analysis without manual effort.  

🧰 **Stack**: AWS Lambda, EventBridge, BeautifulSoup, S3, CloudWatch  
🧪 **Tested On**: AWS Free Tier  

<p align="center">
  <img src="https://raw.githubusercontent.com/bashoori/data-engineering-portfolio/main/docs/images/etl5.png" alt="LinkedIn Scraper Diagram" width="700" style="border: 1px solid #ccc; border-radius: 6px;" />
</p>

---

