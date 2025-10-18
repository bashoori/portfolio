<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Bita Ashoori | Data Engineering Portfolio</title>
  <style>
    body {
      font-family: "Segoe UI", Arial, sans-serif;
      color: #1E293B;
      background-color: #ffffff;
      margin: 40px;
      line-height: 1.6;
    }

    h1, h2, h3, h4 {
      color: #0078D4;
    }

    a {
      color: #2563EB;
      text-decoration: none;
    }

    a:hover {
      text-decoration: underline;
      color: #0078D4;
    }

    section {
      margin-bottom: 60px;
      padding: 25px;
      border-left: 4px solid #0078D4;
      background-color: #FAFAFA;
      border-radius: 10px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.05);
    }

    img {
      border-radius: 8px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.08);
    }

    .skills-grid {
      display: flex;
      flex-wrap: wrap;
      gap: 20px;
    }

    .skill-card {
      flex: 1;
      min-width: 250px;
      background: #F3F4F6;
      padding: 15px 20px;
      border-radius: 10px;
    }

    footer {
      margin-top: 60px;
      text-align: center;
      color: #666;
      font-size: 0.9em;
    }

    .stack img {
      margin: 3px;
    }

    hr {
      border: none;
      border-top: 2px solid #E5E7EB;
      margin: 40px 0;
    }
  </style>
</head>

<body>

<!-- ====== Header ====== -->
<div style="display: flex; align-items: center; justify-content: space-between; width: 100%; padding-bottom: 25px; border-bottom: 2px solid #eaeaea;">
  <div style="flex: 1;">
    <h1 style="margin: 0;">Bita Ashoori</h1>
    <p style="margin: 6px 0 0; font-size: 1.25em; color: #555;">💼 <strong>Data Engineering Portfolio</strong></p>
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
I’m a <strong>Data Engineer based in Vancouver</strong> with over 5 years of experience spanning <strong>data engineering, business intelligence, and analytics</strong>. 
I specialize in designing <strong>cloud-native ETL/ELT pipelines</strong> and <strong>automating data workflows</strong> that transform raw data into actionable insights.
</p>

<p>
My background includes work across <strong>healthcare, retail, and public-sector</strong> environments, where I’ve delivered scalable and reliable data solutions. 
With 3+ years building <strong>cloud data pipelines</strong> and 2+ years as a <strong>BI/ETL Developer</strong>, I bring strong expertise in 
<strong>Python, SQL, Apache Airflow, and AWS (S3, Lambda, Redshift)</strong>.
</p>

<p>
I’m currently <strong>expanding my skills in Azure and Databricks</strong>, focusing on <strong>modern data stack architectures</strong> — 
including <strong>Delta Lake, Medallion design, and real-time streaming</strong> — to build next-generation data platforms that drive 
<strong>performance, reliability, and business value</strong>.
</p>

<hr/>

<!-- ====== Core Strengths ====== -->
<h2>Core Strengths</h2>
<div class="skills-grid">
  <div class="skill-card">
    <h4>🏗️ Cloud ETL Design</h4>
    <p>ADF, Airflow, Databricks, and PySpark pipelines optimized for scalability, cost, and observability.</p>
  </div>
  <div class="skill-card">
    <h4>📊 Data Modeling & Analytics</h4>
    <p>SQL Server, Delta Lake, and Power BI integration for curated semantic models and performance tuning.</p>
  </div>
  <div class="skill-card">
    <h4>☁️ Cloud Platforms</h4>
    <p>Azure, AWS, and hybrid data solutions enabling secure, automated data workflows.</p>
  </div>
</div>

<hr/>

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

<h2>Highlighted Projects</h2>

<!-- PROJECT 1 -->
<section>
  <h3>🛒 Azure ADF Retail Pipeline</h3>
  <p><strong>Scenario:</strong> Retail organizations needed an automated cloud pipeline to consolidate and analyze sales data from multiple regions.</p>
  <p><strong>Solution:</strong> Built a cloud-native ETL using Azure Data Factory with parameterized pipelines, incremental loads, and monitoring.</p>
  <p><strong>Impact:</strong> Automated data refresh cycles, improving reporting efficiency by 45%.</p>
  <p class="stack">
    <img src="https://img.shields.io/badge/Azure_Data_Factory-0078D4?logo=microsoftazure&logoColor=white">
    <img src="https://img.shields.io/badge/Azure_SQL_Database-CC2927?logo=microsoftsqlserver&logoColor=white">
    <img src="https://img.shields.io/badge/Power_BI-F2C811?logo=powerbi&logoColor=white">
  </p>
  📎 <a href="https://github.com/bashoori/azure-adf-retail-pipeline">View GitHub Repo</a>
</section>

<!-- PROJECT 2 -->
<section>
  <h3>🏗️ End-to-End Data Pipeline with Databricks</h3>
  <p><strong>Scenario:</strong> Built a complete ETL using the Medallion Architecture (Bronze → Silver → Gold) in Databricks.</p>
  <p><strong>Impact:</strong> Improved data reliability and reduced transformation latency via automated processing.</p>
  <p class="stack">
    <img src="https://img.shields.io/badge/Azure_Databricks-FF3621?logo=databricks&logoColor=white">
    <img src="https://img.shields.io/badge/Delta_Lake-025E8C?logo=apachespark&logoColor=white">
    <img src="https://img.shields.io/badge/Power_BI-F2C811?logo=powerbi&logoColor=white">
  </p>
  📎 <a href="https://github.com/bashoori/databricks-lakehouse-pipeline">View GitHub Repo</a>
</section>

<!-- PROJECT 3 -->
<section>
  <h3>☁️ Cloud ETL Modernization</h3>
  <p><strong>Scenario:</strong> Legacy workflows lacked scalability and centralized monitoring.</p>
  <p><strong>Solution:</strong> Migrated pipelines to Airflow + AWS Redshift with unified logging and error handling.</p>
  <p class="stack">
    <img src="https://img.shields.io/badge/Airflow-017CEE?logo=apacheairflow&logoColor=white">
    <img src="https://img.shields.io/badge/AWS_Redshift-232F3E?logo=amazonaws&logoColor=white">
  </p>
  📎 <a href="https://github.com/bashoori/portfolio/tree/main/cloud-etl-modernization-airflow-aws">View GitHub Repo</a>
</section>

<!-- PROJECT 4 -->
<section>
  <h3>🛠️ Airflow AWS Modernization</h3>
  <p><strong>Scenario:</strong> Migrated Windows Task Scheduler jobs into modular Airflow DAGs with Docker.</p>
  <p><strong>Impact:</strong> Reduced manual errors by 50% and improved job monitoring/alerting.</p>
  <p class="stack">
    <img src="https://img.shields.io/badge/Airflow-017CEE?logo=apacheairflow&logoColor=white">
    <img src="https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white">
    <img src="https://img.shields.io/badge/AWS_S3-FF9900?logo=amazonaws&logoColor=white">
  </p>
  📎 <a href="https://github.com/bashoori/portfolio/tree/main/airflow-aws-modernization">View GitHub Repo</a>
</section>

<!-- PROJECT 5 -->
<section>
  <h3>⚡ Real-Time Marketing Pipeline</h3>
  <p><strong>Scenario:</strong> Simulated real-time campaign data ingestion for faster marketing insights.</p>
  <p><strong>Impact:</strong> Reduced reporting lag from 24h → 1h with PySpark + Delta.</p>
  <p class="stack">
    <img src="https://img.shields.io/badge/PySpark-3A7EE2?logo=apachespark&logoColor=white">
    <img src="https://img.shields.io/badge/AWS_S3-FF9900?logo=amazonaws&logoColor=white">
  </p>
  📎 <a href="https://github.com/bashoori/portfolio/tree/main/real-time-marketing-pipeline">View GitHub Repo</a>
</section>

<!-- PROJECT 6 -->
<section>
  <h3>🎮 Real-Time Player Pipeline</h3>
  <p><strong>Scenario:</strong> Built real-time analytics for player activity to optimize engagement.</p>
  <p><strong>Impact:</strong> Reduced reporting lag from hours → seconds for live ops insights.</p>
  <p class="stack">
    <img src="https://img.shields.io/badge/Kafka-231F20?logo=apachekafka&logoColor=white">
    <img src="https://img.shields.io/badge/Spark-025E8C?logo=apachespark&logoColor=white">
  </p>
  📎 <a href="https://github.com/bashoori/portfolio/tree/main/real-time-player-pipeline">View GitHub Repo</a>
</section>

<!-- PROJECT 7 -->
<section>
  <h3>📈 PySpark Sales Pipeline</h3>
  <p><strong>Scenario:</strong> Scalable PySpark ETL for large sales datasets to improve BI accuracy.</p>
  <p><strong>Impact:</strong> 40% faster transformations using Delta Lake optimizations.</p>
  <p class="stack">
    <img src="https://img.shields.io/badge/PySpark-3A7EE2?logo=apachespark&logoColor=white">
    <img src="https://img.shields.io/badge/AWS_S3-FF9900?logo=amazonaws&logoColor=white">
  </p>
  📎 <a href="https://github.com/bashoori/portfolio/tree/main/pyspark-sales-pipeline">View GitHub Repo</a>
</section>

<!-- PROJECT 8 -->
<section>
  <h3>🏥 FHIR Healthcare Pipeline</h3>
  <p><strong>Scenario:</strong> FHIR healthcare data cleaning and transformation with analytics-ready outputs.</p>
  <p><strong>Impact:</strong> Cut preprocessing time by 60% with better data quality.</p>
  <p class="stack">
    <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white">
    <img src="https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white">
  </p>
  📎 <a href="https://github.com/bashoori/portfolio/tree/main/healthcare-FHIR-data-pipeline">View GitHub Repo</a>
</section>

<!-- PROJECT 9 -->
<section>
  <h3>🚀 Real-Time Event Processing with AWS Kinesis, Glue & Athena</h3>
  <p><strong>Scenario:</strong> Real-time clickstream pipeline using Kinesis → Glue → Athena.</p>
  <p><strong>Impact:</strong> Built reusable pattern for clickstream analytics pipelines.</p>
  <p class="stack">
    <img src="https://img.shields.io/badge/AWS_Kinesis-FF9900?logo=amazonaws&logoColor=white">
    <img src="https://img.shields.io/badge/AWS_Glue-232F3E?logo=amazonaws&logoColor=white">
  </p>
  📎 <a href="https://github.com/bashoori/Real-Time-Event-Processing-with-AWS-Kinesis-Glue-Athena">View GitHub Repo</a>
</section>

<!-- PROJECT 10 -->
<section>
  <h3>🔍 LinkedIn Scraper (Lambda)</h3>
  <p><strong>Scenario:</strong> Automated job tracking using AWS Lambda and BeautifulSoup.</p>
  <p><strong>Impact:</strong> Streamlined job search analytics and lead generation.</p>
  <p class="stack">
    <img src="https://img.shields.io/badge/AWS_Lambda-FF9900?logo=awslambda&logoColor=white">
    <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white">
  </p>
  📎 <a href="https://github.com/bashoori/portfolio/tree/main/linkedIn-job-scraper">View GitHub Repo</a>
</section>

<!-- ====== Visitor & Footer ====== -->
<div style="margin-top:40px;display:flex;align-items:center;gap:8px;">
  <img src="https://visitor-badge.laobi.icu/badge?page_id=bashoori.portfolio&left_color=lightgrey&right_color=teal&style=flat-square" height="18" />
  <img src="https://komarev.com/ghpvc/?username=bashoori&label=Views&color=blueviolet&style=flat-square" height="18" />
</div>

<footer>
  © 2025 Bita Ashoori | Built using HTML & GitHub Pages
</footer>

</body>
</html>
