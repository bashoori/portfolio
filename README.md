<!-- ====== Header ====== -->
<div style="display: flex; align-items: center; justify-content: space-between; width: 100%; padding: 25px 0; border-bottom: 2px solid #eaeaea;">
  <div style="flex: 1;">
    <h1 style="margin: 0; font-size: 2.4em; font-weight: 700; color: #222;">Bita Ashoori</h1>
    <p style="margin: 6px 0 0; font-size: 1.25em; color: #555;">
      <strong>💼 Data Engineering Portfolio</strong>
    </p>
    <p style="margin: 10px 0 0; font-size: 1em; color: #666; max-width: 560px;">
      Designing scalable, cloud-native data pipelines that turn raw data into reliable, analytics-ready systems.
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
I’m a <strong>Data Engineer based in Vancouver</strong> with experience across <strong>data engineering, BI, and analytics</strong>. I specialize in building <strong>cloud-native ETL/ELT pipelines</strong> that are observable, scalable, and designed for real operational use.
</p>

<p>
My work spans <strong>healthcare, retail, and public-sector data</strong>, where reliability, data quality, and auditability matter. I’ve spent multiple years building and maintaining <strong>production pipelines</strong> using <strong>Python, SQL, Apache Airflow, and AWS</strong>, supporting both analytics and downstream reporting systems.
</p>

<p>
I’m currently deepening my focus on <strong>Azure, Databricks, and modern lakehouse architectures</strong>, including <strong>Delta Lake, Medallion design, and streaming pipelines</strong>, with the goal of building data platforms that scale cleanly as organizations grow.
</p>

<!-- ====== Contact ====== -->
<h2>Contact</h2>
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
- [Azure ADF Retail Pipeline](#azure-adf-retail-pipeline)
- [Databricks End-to-End Pipeline](#databricks-end-to-end)
- [Cloud ETL Modernization](#cloud-etl-modernization)
- [Herbal Products API ETL](#herbal-products-api-etl)
- [Airflow AWS Modernization](#airflow-aws-modernization)
- [Real-Time Marketing Pipeline](#real-time-marketing-pipeline)
- [Real-Time Player Pipeline](#real-time-player-pipeline)
- [PySpark Sales Pipeline](#pyspark-sales-pipeline)
- [FHIR Healthcare Pipeline](#fhir-healthcare-pipeline)
- [AWS Kinesis · Glue · Athena](#kinesis-glue-athena)
- [LinkedIn Scraper (Lambda)](#linkedin-scraper-lambda)

<hr/>

<h2>Project Highlights</h2>

<!-- ====== PROJECT TEMPLATE ====== -->

<h3 id="azure-adf-retail-pipeline">🛒 Azure ADF Retail Pipeline</h3>
<p>
<strong>Scenario:</strong> Consolidate retail sales data across regions into a centralized cloud analytics platform.<br/>
📎 <a href="https://github.com/bashoori/azure-adf-retail-pipeline">View Repository</a><br/>
<strong>Solution:</strong> Built a parameterized Azure Data Factory pipeline to ingest, transform, and load data from on-prem SQL Server into Azure Data Lake and Azure SQL Database, with incremental loads and monitoring.<br/>
<strong>Impact:</strong> Automated refresh cycles and improved reporting reliability while reducing manual intervention.<br/>
<strong>Stack:</strong> Azure Data Factory · Azure SQL · Data Lake · Power BI
</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/bashoori/portfolio/main/docs/images/ADF2.png"
       alt="Azure ADF Retail Pipeline" width="720"
       style="border: 1px solid #ddd; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.08);" />
</p>

<hr/>

<h3 id="databricks-end-to-end">🏗️ End-to-End Data Pipeline with Databricks</h3>
<p>
<strong>Scenario:</strong> Build a modern lakehouse architecture for analytics using Medallion design.<br/>
📎 <a href="https://github.com/bashoori/databricks-lakehouse-pipeline">View Repository</a><br/>
<strong>Solution:</strong> Implemented Bronze → Silver → Gold layers using Delta Lake with PySpark, including data quality checks and incremental MERGE operations.<br/>
<strong>Impact:</strong> Improved data reliability and reduced transformation latency through governed lakehouse patterns.<br/>
<strong>Stack:</strong> Databricks · Delta Lake · PySpark · Power BI
</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/bashoori/portfolio/main/docs/images/databricks_end_to_end.png"
       alt="Databricks End-to-End Pipeline" width="720"
       style="border: 1px solid #ddd; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.08);" />
</p>

<hr/>

<h3 id="cloud-etl-modernization">☁️ Cloud ETL Modernization</h3>
<p>
<strong>Scenario:</strong> Legacy batch workflows lacked observability and scalability.<br/>
📎 <a href="https://github.com/bashoori/portfolio/tree/main/cloud-etl-modernization-airflow-aws">View Repository</a><br/>
<strong>Solution:</strong> Rebuilt ETL pipelines using Airflow with centralized logging, standardized schemas, and alerting via CloudWatch.<br/>
<strong>Impact:</strong> Faster troubleshooting and improved SLA consistency.<br/>
<strong>Stack:</strong> Airflow · AWS Redshift · CloudWatch
</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/bashoori/portfolio/main/docs/images/CloudETLModernization.png"
       alt="Cloud ETL Modernization" width="720"
       style="border: 1px solid #ddd; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.08);" />
</p>

<hr/>

<!-- Repeat remaining projects using the same structure -->

<!-- ====== Footer ====== -->
<div style="margin-top: 40px;">
  <img src="https://visitor-badge.laobi.icu/badge?page_id=bashoori.portfolio&left_color=lightgrey&right_color=teal&style=flat-square"
       alt="Visitors">
  <img src="https://komarev.com/ghpvc/?username=bashoori&label=Views&color=blueviolet&style=flat-square"
       alt="Views">
</div>
