<!-- ====== Header ====== -->
<div style="display: flex; align-items: center; justify-content: space-between; width: 100%; padding: 25px 0; border-bottom: 2px solid #eaeaea;">
  <div style="flex: 1;">
    <h1 style="margin: 0; font-size: 2.4em; font-weight: 700; color: #222;">Bita Ashoori</h1>
    <p style="margin: 6px 0 0; font-size: 1.25em; color: #555;">💼 Data Engineering Portfolio</p>
    <p style="margin: 10px 0 0; font-size: 1em; color: #666; max-width: 560px;">
      Designing scalable, cloud-native data pipelines that power decision-making across healthcare, retail, and public services.
    </p>
  </div>
  <div style="flex-shrink: 0; margin-left: 30px;">
    <img src="https://raw.githubusercontent.com/bashoori/data-engineering-portfolio/main/docs/images/profile-photo2.png"
         width="230" alt="Bita Ashoori"
         style="border-radius: 50%; border: 3px solid #f2f2f2; box-shadow: 0 6px 14px rgba(0,0,0,0.12);" />
  </div>
</div>

<!-- ====== About ====== -->
<h2>About Me</h2>
<p>
I’m a Data Engineer based in Vancouver with 5+ years of experience across data engineering, business intelligence, and analytics. I design
<strong>cloud-native pipelines</strong> and automate workflows that turn raw data into actionable insights. My work spans
<strong>healthcare, retail, and public-sector projects</strong>. With 3+ years building cloud pipelines and 2+ years as a BI/ETL Developer,
I’m skilled in <strong>Python, SQL, Apache Airflow, and AWS (S3, Lambda, Redshift)</strong>.
  
Currently expanding my expertise in <strong>Azure data services</strong> and <strong>Databricks</strong>, alongside modern data stack practices, to build next-generation data platforms that support real-time insights and scalability.
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
  <a href="https://raw.githubusercontent.com/bashoori/data-engineering-portfolio/main/docs/Resume-BitaAshoori-CloudDataSpecialist.pdf">
    <img alt="Resume" src="https://img.shields.io/badge/Resume-Download-green?logo=adobeacrobatreader">
  </a>
</p>

<hr/>

## 🔗 Quick Navigation
- [🏗️ End-to-End Data Pipeline with Databricks](#databricks-end-to-end)
- [⚡ Real-Time Marketing Pipeline](#real-time-marketing-pipeline)
- [📈 PySpark Sales Pipeline](#pyspark-sales-pipeline)
- [☁️ Cloud ETL Modernization](#cloud-etl-modernization)
- [🛠️ Airflow AWS Modernization](#airflow-aws-modernization)
- [🚀 Real-Time Event Processing with AWS Kinesis, Glue & Athena](#kinesis-glue-athena)
- [🎮 Real-Time Player Pipeline](#real-time-player-pipeline)
- [🏥 FHIR Healthcare Pipeline](#fhir-healthcare-pipeline)
- [🔍 LinkedIn Scraper (Lambda)](#linkedin-scraper-lambda)

<hr/>

<h2>Project Highlights</h2>

<!-- 1. End-to-End Databricks Pipeline -->
<h3 id="databricks-end-to-end">🏗️ End-to-End Data Pipeline with Databricks</h3>
<p><strong>Scenario:</strong> Designed and implemented a complete end-to-end ETL pipeline in Azure Databricks, applying the <strong>Medallion Architecture (Bronze → Silver → Gold)</strong> to build a modern data lakehouse for analytics.<br/>
📎 <a href="https://github.com/bashoori/databricks-lakehouse-pipeline">View GitHub Repo</a><br/>
<strong>Solution:</strong> Developed a multi-layer Delta Lake pipeline to ingest, cleanse, and aggregate retail data using PySpark and SQL within Databricks notebooks. Implemented data quality rules, incremental MERGE operations, and created analytical views for dashboards.<br/>
✅ <strong>Impact:</strong> Improved data reliability and reduced transformation latency by enabling efficient, governed, and automated data processing in the Databricks ecosystem.<br/>
🧰 <strong>Stack:</strong> Azure Databricks, Delta Lake, PySpark, Spark SQL, Unity Catalog, Power BI Cloud<br/>
🧪 <strong>Tested On:</strong> Azure Databricks Community Edition + GitHub Codespaces</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/bashoori/data-engineering-portfolio/main/docs/images/databricks_end_to_end.png"
       alt="Databricks Lakehouse Pipeline Diagram" width="720"
       style="border: 1px solid #ddd; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.08);" />
</p>

<hr/>

<!-- 2. Real-Time Marketing Pipeline -->
<h3 id="real-time-marketing-pipeline">⚡ Real-Time Marketing Pipeline</h3>
<p><strong>Scenario:</strong> Marketing teams need faster feedback loops from ad campaigns to optimize spend and performance.<br/>
📎 <a href="https://github.com/bashoori/data-engineering-portfolio/tree/main/real-time-marketing-pipeline">View GitHub Repo</a><br/>
<strong>Solution:</strong> Simulated real-time ingestion of campaign data with PySpark + Delta patterns for incremental insights.<br/>
✅ <strong>Impact:</strong> Reduced reporting lag from <strong>24h → ~1h</strong>, enabling quicker optimization cycles.<br/>
🧰 <strong>Stack:</strong> PySpark, Databricks, GitHub Actions, AWS S3<br/>
🧪 <strong>Tested On:</strong> Databricks Community Edition, GitHub CI/CD</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/bashoori/data-engineering-portfolio/main/docs/images/image1.png"
       alt="Real-Time Marketing Pipeline Diagram" width="720"
       style="border: 1px solid #ddd; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.08);" />
</p>

<hr/>

<!-- 3. PySpark Sales Pipeline -->
<h3 id="pyspark-sales-pipeline">📈 PySpark Sales Pipeline</h3>
<p><strong>Scenario:</strong> Enterprises need scalable ETL for large sales datasets to drive timely BI and planning.<br/>
📎 <a href="https://github.com/bashoori/data-engineering-portfolio/tree/main/pyspark-sales-pipeline">View GitHub Repo</a><br/>
<strong>Solution:</strong> Production-style PySpark ETL to ingest/transform into Delta Lake with partitioning and optimization.<br/>
✅ <strong>Impact:</strong> ~<strong>40% faster</strong> transformations and improved reporting accuracy with Delta optimizations.<br/>
🧰 <strong>Stack:</strong> PySpark, Delta Lake, AWS S3<br/>
🧪 <strong>Tested On:</strong> Local Databricks + S3</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/bashoori/data-engineering-portfolio/main/docs/images/etl6.png"
       alt="PySpark Sales Pipeline Diagram" width="720"
       style="border: 1px solid #ddd; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.08);" />
</p>

<hr/>

<!-- 4. Cloud ETL Modernization -->
<h3 id="cloud-etl-modernization">☁️ Cloud ETL Modernization</h3>
<p><strong>Scenario:</strong> Legacy workflows lacked observability, scalability, and centralized monitoring.<br/>
📎 <a href="https://github.com/bashoori/data-engineering-portfolio/tree/main/cloud-etl-modernization-airflow-aws">View GitHub Repo</a><br/>
<strong>Solution:</strong> Built scalable ETL from APIs to Redshift with Airflow orchestration and CloudWatch alerting; standardized schemas and error handling.<br/>
✅ <strong>Impact:</strong> ~<strong>30% faster</strong> troubleshooting via unified logging/metrics; more consistent SLAs.<br/>
🧰 <strong>Stack:</strong> Apache Airflow, AWS Redshift, CloudWatch<br/>
🧪 <strong>Tested On:</strong> AWS Free Tier, Docker</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/bashoori/data-engineering-portfolio/main/docs/images/CloudETLModernization.png"
       alt="Cloud ETL Diagram" width="720"
       style="border: 1px solid #ddd; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.08);" />
</p>

<hr/>

<!-- 5. Airflow AWS Modernization -->
<h3 id="airflow-aws-modernization">🛠️ Airflow AWS Modernization</h3>
<p><strong>Scenario:</strong> Legacy Windows Task Scheduler jobs needed modernization for reliability and observability.<br/>
📎 <a href="https://github.com/bashoori/data-engineering-portfolio/tree/main/airflow-aws-modernization">View GitHub Repo</a><br/>
<strong>Solution:</strong> Migrated jobs into modular Airflow DAGs containerized with Docker, storing artifacts in S3 and standardizing logging/retries.<br/>
✅ <strong>Impact:</strong> Up to <strong>50% reduction</strong> in manual errors and improved job monitoring/alerting.<br/>
🧰 <strong>Stack:</strong> Python, Apache Airflow, Docker, AWS S3<br/>
🧪 <strong>Tested On:</strong> Local Docker, GitHub Codespaces</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/bashoori/data-engineering-portfolio/main/docs/images/etl2.png"
       alt="Airflow AWS Diagram" width="720"
       style="border: 1px solid #ddd; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.08);" />
</p>

<hr/>

<!-- 6. Real-Time Event Processing -->
<h3 id="kinesis-glue-athena">🚀 Real-Time Event Processing with AWS Kinesis, Glue & Athena</h3>
<p><strong>Scenario:</strong> Simulated a real-time clickstream pipeline where user interaction events are sent to AWS Kinesis, processed with Glue, and queried in Athena.</p>
🧰 <strong>Stack:</strong> Python • AWS Kinesis • AWS Glue • AWS Athena • S3<br/>
✅ <strong>Impact:</strong> Built a reusable pattern for clickstream and analytics pipelines.<br/>
<p align="center">
  <img src="https://raw.githubusercontent.com/bashoori/Real-Time-Event-Processing-with-AWS-Kinesis-Glue-Athena/main/Image.png"
       alt="Kinesis Glue Athena Diagram" width="720"
       style="border: 1px solid #ddd; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.08);" />
</p>

<hr/>

<!-- 7. Real-Time Player Pipeline -->
<h3 id="real-time-player-pipeline">🎮 Real-Time Player Pipeline</h3>
<p><strong>Scenario:</strong> Gaming companies need real-time analytics on player activity to optimize engagement and retention.<br/>
📎 <a href="https://github.com/bashoori/data-engineering-portfolio/tree/main/real-time-player-pipeline">View GitHub Repo</a></p>
✅ <strong>Impact:</strong> Reduced reporting lag from <strong>hours → seconds</strong> for live ops insights.<br/>
🧰 <strong>Stack:</strong> Kafka / AWS Kinesis, Airflow, S3, Spark<br/>
<p align="center">
  <img src="https://raw.githubusercontent.com/bashoori/data-engineering-portfolio/main/docs/images/etl3.png"
       alt="Real-Time Player Pipeline Diagram" width="720"
       style="border: 1px solid #ddd; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.08);" />
</p>

<hr/>

<!-- 8. FHIR Healthcare Pipeline -->
<h3 id="fhir-healthcare-pipeline">🏥 FHIR Healthcare Pipeline</h3>
<p><strong>Scenario:</strong> Healthcare projects using FHIR require clean, analytics-ready datasets while preserving clinical context.<br/>
📎 <a href="https://github.com/bashoori/data-engineering-portfolio/tree/main/healthcare-FHIR-data-pipeline">View GitHub Repo</a></p>
✅ <strong>Impact:</strong> Cut preprocessing time by ~<strong>60%</strong>; improved data quality.<br/>
🧰 <strong>Stack:</strong> Python, Pandas, SQLite, Streamlit<br/>
<p align="center">
  <img src="https://raw.githubusercontent.com/bashoori/data-engineering-portfolio/main/docs/images/etl4.png"
       alt="FHIR Pipeline Diagram" width="720"
       style="border: 1px solid #ddd; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.08);" />
</p>

<hr/>

<!-- 9. LinkedIn Scraper -->
<h3 id="linkedin-scraper-lambda">🔍 LinkedIn Scraper (Lambda)</h3>
<p><strong>Scenario:</strong> Manual job tracking is slow and error-prone for candidates and recruiters.<br/>
📎 <a href="https://github.com/bashoori/data-engineering-portfolio/tree/main/linkedIn-job-scraper">View GitHub Repo</a></p>
✅ <strong>Impact:</strong> Automated lead sourcing and job search analytics.<br/>
🧰 <strong>Stack:</strong> AWS Lambda, EventBridge, BeautifulSoup, S3<br/>
<p align="center">
  <img src="https://raw.githubusercontent.com/bashoori/data-engineering-portfolio/main/docs/images/etl5.png"
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
  <img src="https://visitor-badge.laobi.icu/badge?page_id=bashoori.data-engineering-portfolio&left_color=lightgrey&right_color=teal&style=flat-square"
       alt="Unique Visitors" height="18">
  <img src="https://komarev.com/ghpvc/?username=bashoori&label=Views&color=blueviolet&style=flat-square"
       alt="Portfolio Views" height="18">
</div>


