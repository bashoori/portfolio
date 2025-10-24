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
  <img src="https://raw.githubusercontent.com/bashoori/herbal-products-api-etl/main/docs/images/herbal_products_etl.png"
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
