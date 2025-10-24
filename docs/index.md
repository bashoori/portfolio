<!-- ====== Header ====== -->
<div style="display: flex; align-items: center; justify-content: space-between; width: 100%; padding: 25px 0; border-bottom: 2px solid #eaeaea;">
  <div style="flex: 1;">
    <h1 style="margin: 0; font-size: 2.4em; font-weight: 700; color: #222;">Bita Ashoori</h1>
    <p style="margin: 6px 0 0; font-size: 1.25em; color: #555;">
      <strong>💼 Data Engineering Portfolio</strong>
    </p>
    <p style="margin: 10px 0 0; font-size: 1em; color: #666; max-width: 560px;">
      Designing scalable, cloud-native data pipelines that power decision-making across healthcare, retail, and public services.
    </p>
  </div>
  <div style="flex-shrink: 0; margin-left: 30px;">
    <img src="https://raw.githubusercontent.com/bashoori/portfolio/main/docs/images/profile-photo4.png"
         width="230" alt="Bita Ashoori"
         style="border-radius: 50%; border: 3px solid #f2f2f2; box-shadow: 0 6px 14px rgba(0,0,0,0.12);" />
  </div>
</div>

<!-- ====== About ====== -->
<h2>About Me</h2>
<p>
I’m a <strong>Data Engineer based in Vancouver</strong> with over 5 years of experience spanning <strong>data engineering, business intelligence, and analytics</strong>. I specialize in designing <strong>cloud-native ETL/ELT pipelines</strong> and <strong>automating data workflows</strong> that transform raw data into actionable insights.
</p>

<p>
My background includes work across <strong>healthcare, retail, and public-sector</strong> environments, where I’ve delivered scalable and reliable data solutions. With 3+ years building <strong>cloud data pipelines</strong> and 2+ years as a <strong>BI/ETL Developer</strong>, I bring strong expertise in <strong>Python, SQL, Apache Airflow, and AWS (S3, Lambda, Redshift)</strong>.
</p>

<p>
I’m currently <strong>expanding my skills in Azure and Databricks</strong>, focusing on <strong>modern data stack architectures</strong>—including <strong>Delta Lake, Medallion design, and real-time streaming</strong>—to build next-generation data platforms that drive <strong>performance, reliability, and business value</strong>.
</p>

<!-- ====== Contact ====== -->
<h2>Contact Me</h2>
<p>
  <a href="https://github.com/bashoori">
    <img alt="GitHub" src="https://img.shields.io/badge/GitHub-bashoori-black?logo=github">
  </a>
  &nbsp;
  <a href="https://www.linkedin.com/in/bitaashoori">
    <img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-Bita%20Ashoori-blue?logo=linkedin">
  </a>
  &nbsp;
  <a href="https://raw.githubusercontent.com/bashoori/portfolio/main/docs/Resume-BitaAshoori-CloudDataSpecialist.pdf">
    <img alt="Resume" src="https://img.shields.io/badge/Resume-Download-green?logo=adobeacrobatreader">
  </a>
</p>

<hr/>

## 🔗 Quick Navigation
- [🛒 Azure ADF Retail Pipeline](#azure-adf-retail-pipeline)
- [🏗️ End-to-End Data Pipeline with Databricks](#databricks-end-to-end)
- [☁️ Cloud ETL Modernization](#cloud-etl-modernization)
- [⚗️ Herbal Products API ETL](#herbal-products-api-etl)
- [🛠️ Airflow AWS Modernization](#airflow-aws-modernization)
- [⚡ Real-Time Marketing Pipeline](#real-time-marketing-pipeline)
- [🎮 Real-Time Player Pipeline](#real-time-player-pipeline)
- [📈 PySpark Sales Pipeline](#pyspark-sales-pipeline)
- [🏥 FHIR Healthcare Pipeline](#fhir-healthcare-pipeline)
- [🚀 Real-Time Event Processing with AWS Kinesis, Glue & Athena](#kinesis-glue-athena)
- [🔍 LinkedIn Scraper (Lambda)](#linkedin-scraper-lambda)

<hr/>

<h2>Project Highlights</h2>

<!-- 1. Azure ADF Retail Pipeline -->
<h3 id="azure-adf-retail-pipeline">🛒 Azure ADF Retail Pipeline</h3>
<p><strong>Scenario:</strong> Retail organizations needed an automated cloud data pipeline to consolidate and analyze sales data from multiple regions.<br/>
📎 <a href="https://github.com/bashoori/azure-adf-retail-pipeline">View GitHub Repo</a><br/>
<strong>Solution:</strong> Developed a cloud-native ETL pipeline using <strong>Azure Data Factory</strong> that ingests, transforms, and loads retail sales data from on-prem SQL Server to <strong>Azure Data Lake</strong> and <strong>Azure SQL Database</strong>. Implemented <strong>parameterized pipelines</strong>, <strong>incremental data loads</strong>, and <strong>monitoring through ADF logs</strong>.<br/>
✅ <strong>Impact:</strong> Improved reporting efficiency by 45%, automated data refresh cycles, and reduced manual dependencies.<br/>
🧰 <strong>Stack:</strong> Azure Data Factory · Azure SQL Database · Blob Storage · Power BI<br/>
🧪 <strong>Tested On:</strong> Azure Free Tier + GitHub Codespaces</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/bashoori/portfolio/main/docs/images/ADF2.png"
       alt="Azure ADF Retail Pipeline Diagram" width="720"
       style="border: 1px solid #ddd; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.08);" />
</p>

<hr/>

<!-- 2. End-to-End Databricks Pipeline -->
<h3 id="databricks-end-to-end">🏗️ End-to-End Data Pipeline with Databricks</h3>
<p><strong>Scenario:</strong> Designed and implemented a complete end-to-end ETL pipeline in Azure Databricks, applying the <strong>Medallion Architecture (Bronze → Silver → Gold)</strong> to build a modern data lakehouse for analytics.<br/>
📎 <a href="https://github.com/bashoori/databricks-lakehouse-pipeline">View GitHub Repo</a><br/>
<strong>Solution:</strong> Developed a multi-layer Delta Lake pipeline to ingest, cleanse, and aggregate retail data using PySpark and SQL within Databricks notebooks. Implemented data quality rules, incremental MERGE operations, and created analytical views for dashboards.<br/>
✅ <strong>Impact:</strong> Improved data reliability and reduced transformation latency by enabling efficient, governed, and automated data processing in the Databricks ecosystem.<br/>
🧰 <strong>Stack:</strong> Azure Databricks · Delta Lake · PySpark · Unity Catalog · Power BI<br/>
🧪 <strong>Tested On:</strong> Azure Databricks Community Edition + GitHub Codespaces</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/bashoori/portfolio/main/docs/images/databricks_end_to_end.png"
       alt="Databricks Lakehouse Pipeline Diagram" width="720"
       style="border: 1px solid #ddd; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.08);" />
</p>

<hr/>

<!-- 3. Cloud ETL Modernization -->
<h3 id="cloud-etl-modernization">☁️ Cloud ETL Modernization</h3>
<p><strong>Scenario:</strong> Legacy workflows lacked observability, scalability, and centralized monitoring.<br/>
📎 <a href="https://github.com/bashoori/portfolio/tree/main/cloud-etl-modernization-airflow-aws">View GitHub Repo</a><br/>
<strong>Solution:</strong> Built scalable ETL from APIs to Redshift with Airflow orchestration and CloudWatch alerting; standardized schemas and error handling.<br/>
✅ <strong>Impact:</strong> ~<strong>30% faster</strong> troubleshooting via unified logging/metrics; more consistent SLAs.<br/>
🧰 <strong>Stack:</strong> Apache Airflow · AWS Redshift · CloudWatch<br/>
🧪 <strong>Tested On:</strong> AWS Free Tier + Docker</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/bashoori/portfolio/main/docs/images/CloudETLModernization.png"
       alt="Cloud ETL Diagram" width="720"
       style="border: 1px solid #ddd; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.08);" />
</p>

<hr/>

<!-- 4. Herbal Products API ETL -->
<h3 id="herbal-products-api-etl">⚗️ Herbal Products API ETL (SQLite + Logging)</h3>
<p><strong>Scenario:</strong> Built a complete API-based ETL pipeline for a natural products company (simulated from <em>Natural Factors</em>) to extract, transform, and load product data into a local SQLite database for analysis and visualization.<br/>
📎 <a href="https://github.com/bashoori/herbal-products-api-etl">View GitHub Repo</a><br/>
<strong>Solution:</strong> Designed a modular ETL process in Python that connects to an external API, performs data cleaning, loads data into SQLite, and includes full <strong>logging, error handling, and ETL monitoring</strong> with Loguru. A Streamlit dashboard visualizes data for easy validation.<br/>
✅ <strong>Impact:</strong> Demonstrates production-style ETL workflow design, monitoring, and API integration within a lightweight, reproducible environment (GitHub Codespaces).<br/>
🧰 <strong>Stack:</strong> Python · SQLite · Pandas · Loguru · Streamlit · SQLAlchemy<br/>
🧪 <strong>Tested On:</strong> GitHub Codespaces + Local SQLite</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/bashoori/portfolio/main/docs/images/herbal.png"
       alt="Herbal Products ETL Diagram" width="720"
       style="border: 1px solid #ddd; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.08);" />
</p>

<hr/>

<!-- 5. Airflow AWS Modernization -->
<h3 id="airflow-aws-modernization">🛠️ Airflow AWS Modernization</h3>
<p><strong>Scenario:</strong> Legacy Windows Task Scheduler jobs needed modernization for reliability and observability.<br/>
📎 <a href="https://github.com/bashoori/portfolio/tree/main/airflow-aws-modernization">View GitHub Repo</a><br/>
<strong>Solution:</strong> Migrated jobs into modular Airflow DAGs containerized with Docker, storing artifacts in S3 and standardizing logging/retries.<br/>
✅ <strong>Impact:</strong> Up to <strong>50% reduction</strong> in manual errors and improved job monitoring/alerting.<br/>
🧰 <strong>Stack:</strong> Python · Apache Airflow · Docker · AWS S3<br/>
🧪 <strong>Tested On:</strong> Local Docker + GitHub Codespaces</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/bashoori/portfolio/main/docs/images/etl2.png"
       alt="Airflow AWS Diagram" width="720"
       style="border: 1px solid #ddd; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.08);" />
</p>

<hr/>

<!-- 6. Real-Time Marketing Pipeline -->
<h3 id="real-time-marketing-pipeline">⚡ Real-Time Marketing Pipeline</h3>
<p><strong>Scenario:</strong> Marketing teams often struggle to get timely insights from campaign data spread across multiple ad platforms. This project simulates a real-time ingestion and transformation system to provide near-instant analytics for marketing performance.<br/>
📎 <a href="https://github.com/bashoori/portfolio/tree/main/real-time-marketing-pipeline">View GitHub Repo</a><br/>
<strong>Solution:</strong> Implemented a PySpark-based data ingestion and transformation pipeline that streams ad campaign data into a Delta Lake architecture. Leveraged incremental data loading and scheduled automation with GitHub Actions for CI/CD.<br/>
✅ <strong>Impact:</strong> Reduced data latency from <strong>24 hours to under 1 hour</strong>, enabling rapid decision-making for campaign optimization.<br/>
🧰 <strong>Stack:</strong> PySpark · Databricks · Delta Lake · GitHub Actions · AWS S3<br/>
🧪 <strong>Tested On:</strong> Databricks Community Edition + GitHub CI/CD</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/bashoori/portfolio/main/docs/images/image1.png"
       alt="Real-Time Marketing Pipeline Diagram" width="720"
       style="border: 1px solid #ddd; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.08);" />
</p>

<hr/>

<!-- 7. Real-Time Player Pipeline -->
<h3 id="real-time-player-pipeline">🎮 Real-Time Player Pipeline</h3>
<p><strong>Scenario:</strong> Gaming companies need live insights into player behavior to improve engagement and retention. This project demonstrates how to process high-volume event streams from gameplay in real time.<br/>
📎 <a href="https://github.com/bashoori/portfolio/tree/main/real-time-player-pipeline">View GitHub Repo</a><br/>
<strong>Solution:</strong> Built a streaming data pipeline using Kafka (or AWS Kinesis) for real-time ingestion, orchestrated with Airflow. Transformed and stored event data in AWS S3 for analytics, allowing near-instant monitoring of user engagement metrics.<br/>
✅ <strong>Impact:</strong> Enabled dashboards with <strong>real-time player stats</strong> and reduced data availability lag from hours to seconds.<br/>
🧰 <strong>Stack:</strong> Kafka · AWS Kinesis · Airflow · S3 · Spark<br/>
🧪 <strong>Tested On:</strong> Local Docker + AWS Free Tier</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/bashoori/portfolio/main/docs/images/etl3.png"
       alt="Real-Time Player Pipeline Diagram" width="720"
       style="border: 1px solid #ddd; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.08);" />
</p>

<hr/>

<!-- 8. PySpark Sales Pipeline -->
<h3 id="pyspark-sales-pipeline">📈 PySpark Sales Pipeline</h3>
<p><strong>Scenario:</strong> Enterprises require efficient ETL systems to handle growing volumes of sales data and provide timely insights for forecasting and reporting.<br/>
📎 <a href="https://github.com/bashoori/portfolio/tree/main/pyspark-sales-pipeline">View GitHub Repo</a><br/>
<strong>Solution:</strong> Created a production-style PySpark ETL pipeline to extract large sales datasets, transform and aggregate them into a Delta Lake, and optimize with partitioning and caching for query performance.<br/>
✅ <strong>Impact:</strong> Achieved up to <strong>40% faster transformations</strong> and improved report accuracy through standardized schema validation and Delta Lake optimization.<br/>
🧰 <strong>Stack:</strong> PySpark · Delta Lake · AWS S3 · Databricks<br/>
🧪 <strong>Tested On:</strong> Local Databricks + AWS Free Tier</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/bashoori/portfolio/main/docs/images/etl6.png"
       alt="PySpark Sales Pipeline Diagram" width="720"
       style="border: 1px solid #ddd; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.08);" />
</p>

<hr/>

<!-- 9. FHIR Healthcare Pipeline -->
<h3 id="fhir-healthcare-pipeline">🏥 FHIR Healthcare Pipeline</h3>
<p><strong>Scenario:</strong> Healthcare organizations using FHIR (Fast Healthcare Interoperability Resources) often face data integration challenges between clinical systems and analytics tools.<br/>
📎 <a href="https://github.com/bashoori/portfolio/tree/main/healthcare-FHIR-data-pipeline">View GitHub Repo</a><br/>
<strong>Solution:</strong> Developed a Python-based ETL pipeline to ingest and normalize FHIR patient and encounter data, clean and store it in SQLite, and visualize it using Streamlit. Added validation and audit layers to ensure clinical data integrity.<br/>
✅ <strong>Impact:</strong> Improved preprocessing efficiency by <strong>60%</strong> and ensured high-quality, analytics-ready clinical data.<br/>
🧰 <strong>Stack:</strong> Python · Pandas · FHIR API · SQLite · Streamlit<br/>
🧪 <strong>Tested On:</strong> Local + GitHub Codespaces</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/bashoori/portfolio/main/docs/images/etl4.png"
       alt="FHIR Healthcare Pipeline Diagram" width="720"
       style="border: 1px solid #ddd; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.08);" />
</p>

<hr/>

<!-- 10. Real-Time Event Processing -->
<h3 id="kinesis-glue-athena">🚀 Real-Time Event Processing with AWS Kinesis, Glue & Athena</h3>
<p><strong>Scenario:</strong> Modern applications generate massive clickstream and interaction data that must be processed in near-real time for user analytics and system monitoring.<br/>
📎 <a href="https://github.com/bashoori/Real-Time-Event-Processing-with-AWS-Kinesis-Glue-Athena">View GitHub Repo</a><br/>
<strong>Solution:</strong> Designed an end-to-end data pipeline where user events are streamed to AWS Kinesis, transformed using Glue jobs, and queried via Athena. Implemented data cataloging and schema evolution for dynamic JSON data.<br/>
✅ <strong>Impact:</strong> Built a reusable real-time processing pattern for streaming analytics and data lake integration.<br/>
🧰 <strong>Stack:</strong> Python · AWS Kinesis · AWS Glue · AWS Athena · S3<br/>
🧪 <strong>Tested On:</strong> AWS Free Tier</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/bashoori/Real-Time-Event-Processing-with-AWS-Kinesis-Glue-Athena/main/Image.png"
       alt="Kinesis Glue Athena Diagram" width="720"
       style="border: 1px solid #ddd; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.08);" />
</p>

<hr/>

<!-- 11. LinkedIn Scraper -->
<h3 id="linkedin-scraper-lambda">🔍 LinkedIn Scraper (Lambda)</h3>
<p><strong>Scenario:</strong> Manual job tracking is slow and error-prone for candidates, recruiters, and analysts seeking real-time market insights.<br/>
📎 <a href="https://github.com/bashoori/portfolio/tree/main/linkedIn-job-scraper">View GitHub Repo</a><br/>
<strong>Solution:</strong> Created an automated data scraper using AWS Lambda and EventBridge that extracts LinkedIn job posts at scheduled intervals, parses them with BeautifulSoup, and stores them in S3 for analysis.<br/>
✅ <strong>Impact:</strong> Automated collection of job market data for trend analysis and dashboarding.<br/>
🧰 <strong>Stack:</strong> AWS Lambda · EventBridge · BeautifulSoup · S3<br/>
🧪 <strong>Tested On:</strong> AWS Free Tier + Local Validation</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/bashoori/portfolio/main/docs/images/etl5.png"
       alt="LinkedIn Scraper Diagram" width="720"
       style="border: 1px solid #ddd; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.08);" />
</p>

<hr/>

<!-- ====== Visitor & View Badges (bottom of page) ====== -->
<div style="
  margin-top: 40px;
  padding: 6px 10px;
  display: flex;
  align-items: center;
  gap: 8px;
  background-color: #ffffff;
  border-radius: 8px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.08);
  width: fit-content;
  font-size: 0.85em;
">
  <img src="https://visitor-badge.laobi.icu/badge?page_id=bashoori.portfolio&left_color=lightgrey&right_color=teal&style=flat-square"
       alt="Unique Visitors" height="18">
  <img src="https://komarev.com/ghpvc/?username=bashoori&label=Views&color=blueviolet&style=flat-square"
       alt="Portfolio Views" height="18">
</div>

