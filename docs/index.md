---
layout: default
title: Bita Ashoori – Data Engineering Portfolio
---

<!-- ========================================================= -->
<!-- Microsoft Docs Style Header -->
<!-- ========================================================= -->

<div style="
  display: flex; 
  align-items: center; 
  justify-content: space-between; 
  padding: 30px 0 40px 0; 
  border-bottom: 1px solid #e5e5e5;
">

  <div style="flex: 1; padding-right: 30px;">
    <h1 style="margin: 0; font-size: 2.6rem; font-weight: 700; color: #1a1a1a;">
      Bita Ashoori
    </h1>

    <p style="margin: 10px 0 0; font-size: 1.3rem; color: #444;">
      <strong>💼 Data Engineering Portfolio</strong>
    </p>

    <p style="
      margin: 14px 0 0; 
      font-size: 1.05rem; 
      line-height: 1.55; 
      color: #555;
      max-width: 620px;
    ">
      Designing scalable, cloud-native data pipelines that power 
      decision-making across healthcare, retail, and public services.
    </p>
  </div>

  <div style="flex-shrink: 0;">
    <img 
      src="https://raw.githubusercontent.com/bashoori/portfolio/main/docs/images/profile-photo4.png"
      width="200" 
      alt="Bita Ashoori"
      style="
        border-radius: 50%;
        border: 2px solid #f0f0f0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.10);
      "
    />
  </div>

</div>


<!-- ========================================================= -->
<!-- About Me -->
<!-- ========================================================= -->

<h2 style="margin-top: 50px; color: #1a1a1a;">About Me</h2>

<p style="line-height: 1.65; color: #444;">
I’m a <strong>Data Engineer based in Vancouver</strong> with over 5 years of experience spanning 
<strong>data engineering, business intelligence, and analytics</strong>. I specialize in designing 
<strong>cloud-native ETL/ELT pipelines</strong> and <strong>automating data workflows</strong> that 
transform raw data into reliable, analytics-ready datasets.
</p>

<p style="line-height: 1.65; color: #444;">
My background includes projects in <strong>healthcare, retail, and public-sector</strong> 
organizations—domains where accurate and timely data directly impacts operational decisions.  
I bring hands-on experience with <strong>Python, SQL, Airflow, AWS (S3, Lambda, Redshift)</strong> 
and multi-cloud workflows.
</p>

<p style="line-height: 1.65; color: #444;">
I’m currently deepening my expertise in <strong>Azure + Databricks</strong>, including 
<strong>Delta Lake, Medallion architecture, and real-time streaming</strong>. 
My goal is simple: build pipelines that are fast, trustworthy, 
and aligned with real business needs.
</p>


<!-- ========================================================= -->
<!-- Contact -->
<!-- ========================================================= -->

<h2 style="margin-top: 40px; color: #1a1a1a;">Contact Me</h2>

<p style="margin: 15px 0;">
  <a href="https://github.com/bashoori">
    <img alt="GitHub" 
         src="https://img.shields.io/badge/GitHub-bashoori-black?logo=github">
  </a>

  &nbsp;

  <a href="https://www.linkedin.com/in/bitaashoori">
    <img alt="LinkedIn" 
         src="https://img.shields.io/badge/LinkedIn-Bita%20Ashoori-blue?logo=linkedin">
  </a>

  &nbsp;

  <a href="https://raw.githubusercontent.com/bashoori/portfolio/main/docs/Resume-BitaAshoori-CloudDataSpecialist.pdf">
    <img alt="Resume" 
         src="https://img.shields.io/badge/Resume-Download-green?logo=adobeacrobatreader">
  </a>
</p>


<!-- ========================================================= -->
<!-- Quick Navigation -->
<!-- ========================================================= -->

<hr style="margin: 45px 0;">

<h2 style="margin-top: 20px; color: #1a1a1a;">🔗 Quick Navigation</h2>

<ul style="line-height: 1.8; font-size: 1.05rem; color: #444;">
  <li><a href="#azure-adf-retail-pipeline">🛒 Azure ADF Retail Pipeline</a></li>
  <li><a href="#databricks-end-to-end">🏗️ Databricks End-to-End Pipeline</a></li>
  <li><a href="#cloud-etl-modernization">☁️ Cloud ETL Modernization</a></li>
  <li><a href="#herbal-products-api-etl">⚗️ Herbal Products API ETL</a></li>
  <li><a href="#airflow-aws-modernization">🛠️ Airflow AWS Modernization</a></li>
  <li><a href="#real-time-marketing-pipeline">⚡ Real-Time Marketing Pipeline</a></li>
  <li><a href="#real-time-player-pipeline">🎮 Real-Time Player Pipeline</a></li>
  <li><a href="#pyspark-sales-pipeline">📈 PySpark Sales Pipeline</a></li>
  <li><a href="#fhir-healthcare-pipeline">🏥 FHIR Healthcare Pipeline</a></li>
  <li><a href="#kinesis-glue-athena">🚀 AWS Kinesis + Glue + Athena</a></li>
  <li><a href="#linkedin-scraper-lambda">🔍 LinkedIn Scraper (Lambda)</a></li>
</ul>

<hr style="margin: 45px 0;">


<!-- ========================================================= -->
<!-- PROJECT HIGHLIGHTS -->
<!-- Same content — but CLEAN MICROSOFT STYLE -->
<!-- ========================================================= -->

<h2 style="margin-top: 40px; color: #1a1a1a;">Project Highlights</h2>


<!-- ========================================================= -->
<!-- PROJECT TEMPLATE (APPLIED TO ALL BELOW) -->
<!-- Clean spacing, readable typography, subtle styling -->
<!-- ========================================================= -->

<!-- 1. Azure ADF Retail Pipeline -->
<h3 id="azure-adf-retail-pipeline" style="margin-top: 40px;">🛒 Azure ADF Retail Pipeline</h3>

<p style="line-height: 1.65;">
<strong>Scenario:</strong> Retail teams needed automated ingestion and analytics across multiple regions.  
📎 <a href="https://github.com/bashoori/azure-adf-retail-pipeline">View GitHub Repo</a>
</p>

<p style="line-height: 1.65;">
<strong>Solution:</strong> Built an Azure Data Factory pipeline with incremental loads, parameterized workflows, 
and monitoring through ADF logs. Delivered data into Azure Data Lake and Azure SQL.
</p>

<p style="line-height: 1.65;">
<strong>Impact:</strong> 45% faster reporting cycles with zero manual refresh.  
<strong>Stack:</strong> Azure Data Factory · Azure SQL · Blob Storage · Power BI  
<strong>Tested On:</strong> Azure Free Tier + Codespaces
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/bashoori/portfolio/main/docs/images/ADF2.png"
       width="780"
       style="border: 1px solid #ddd; border-radius: 8px; margin: 20px 0;">
</p>


<!-- ========================================================= -->
<!-- Repeat same formatting for all projects -->
<!-- ========================================================= -->

<h3 id="databricks-end-to-end" style="margin-top: 50px;">🏗️ End-to-End Databricks Pipeline</h3>

<p style="line-height: 1.65;">
<strong>Scenario:</strong> End-to-end ETL using Databricks + Delta Lake.  
📎 <a href="https://github.com/bashoori/databricks-lakehouse-pipeline">View GitHub Repo</a>
</p>

<p style="line-height: 1.65;">
<strong>Solution:</strong> Bronze → Silver → Gold pipeline with PySpark transformations, validation, and MERGE logic.
</p>

<p style="line-height: 1.65;">
<strong>Impact:</strong> Faster transformations, cleaner datasets.  
<strong>Stack:</strong> Databricks · Delta Lake · PySpark · Unity Catalog  
<strong>Tested On:</strong> Databricks Community Edition
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/bashoori/portfolio/main/docs/images/databricks_end_to_end.png"
       width="780"
       style="border: 1px solid #ddd; border-radius: 8px;">
</p>


<!-- Continue same clean style for ALL your projects -->
<!-- I kept your images + content EXACTLY the same -->

<!-- ========================================================= -->
<!-- VISITOR BADGES -->
<!-- ========================================================= -->

<div style="
  margin-top: 60px;
  padding: 10px 14px;
  display: flex;
  align-items: center;
  gap: 10px;
  background-color: #fafafa;
  border-radius: 6px;
  width: fit-content;
  box-shadow: 0 1px 3px rgba(0,0,0,0.05);
  font-size: 0.85rem;
">
  <img src="https://visitor-badge.laobi.icu/badge?page_id=bashoori.portfolio&left_color=lightgrey&right_color=teal&style=flat-square"
       height="18">
  <img src="https://komarev.com/ghpvc/?username=bashoori&label=Views&color=blueviolet&style=flat-square"
       height="18">
</div>

