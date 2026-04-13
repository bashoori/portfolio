<!-- ====== Page Background Wrapper ====== -->
<div style="background:linear-gradient(to bottom, #f8fafc, #eef2f7);padding:36px 18px;">

  <!-- ====== Content Container ====== -->
  <div style="max-width:1000px;margin:0 auto;background:#ffffff;padding:32px 28px;border-radius:16px;box-shadow:0 10px 30px rgba(0,0,0,0.05);">

    <!-- ====== Header ====== -->
    <div style="display:flex;align-items:center;justify-content:space-between;gap:32px;flex-wrap:wrap;padding-bottom:24px;border-bottom:1px solid #eaeaea;">

      <div style="flex:1;min-width:280px;">
        
        <div style="font-size:0.9em;color:#3b6ea8;font-weight:600;margin-bottom:8px;">
          Data Engineer
        </div>

        <h1 style="margin:0;font-size:2.4em;color:#1f2937;">Bita Ashoori</h1>

        <p style="margin:10px 0 0;font-size:1.1em;color:#4b5563;">
          I design data systems that turn fragmented and unreliable data into something teams can actually trust.
        </p>

        <p style="margin:14px 0 0;max-width:600px;color:#6b7280;line-height:1.6;">
          I bring 5 years of experience across data engineering and business intelligence, including 3 years focused on data engineering and 2 years in BI, working in healthcare and e-commerce environments.
        </p>

        <p style="margin:14px 0 0;color:#6b7280;line-height:1.6;">
          I have built and maintained data pipelines and analytical datasets using SQL Server, Python, SSIS, Apache Airflow, Azure, and Power BI, with a focus on turning fragmented source data into structured, reliable systems.
        </p>

        <p style="margin:14px 0 0;color:#6b7280;line-height:1.6;">
          My work emphasizes data quality, validation, and modeling decisions so the data behaves correctly and can be trusted in real use.
        </p>

        <p style="margin:16px 0 0;color:#6b7280;">
          📍 Vancouver, BC &nbsp; | &nbsp;
          <a href="https://github.com/bashoori"><strong>GitHub</strong></a> &nbsp; | &nbsp;
          <a href="https://www.linkedin.com/in/bitaashoori"><strong>LinkedIn</strong></a>
        </p>

      </div>

      <div style="flex-shrink:0;">
        <img
          src="https://raw.githubusercontent.com/bashoori/portfolio/main/docs/images/profile-photo4.png"
          width="180"
          alt="Bita Ashoori"
          style="border-radius:50%;border:3px solid #f1f1f1;box-shadow:0 6px 14px rgba(0,0,0,0.08);" />
      </div>

    </div>

    <!-- ====== Current Focus ====== -->
    <h2 style="margin-top:28px;">Current Focus</h2>
    <p style="color:#6b7280;">
      Advancing skills in Microsoft Fabric and lakehouse architecture, with active preparation for DP-700. Open to new data engineering opportunities.
    </p>

    <!-- ====== What I Do ====== -->
    <h2 style="margin-top:32px;">What I Do</h2>

    <div style="display:flex;gap:24px;flex-wrap:wrap;">
      <div style="flex:1;min-width:240px;">
        <h3>Data Pipelines</h3>
        <ul>
          <li>Design reliable workflows</li>
          <li>Handle messy real-world data</li>
          <li>Ensure consistent delivery</li>
        </ul>
      </div>

      <div style="flex:1;min-width:240px;">
        <h3>Data Modeling</h3>
        <ul>
          <li>Structure datasets for analysis</li>
          <li>Define business logic</li>
          <li>Support trusted reporting</li>
        </ul>
      </div>

      <div style="flex:1;min-width:240px;">
        <h3>Modern Platforms</h3>
        <ul>
          <li>Move workflows to cloud</li>
          <li>Apply lakehouse patterns</li>
          <li>Improve performance</li>
        </ul>
      </div>
    </div>

    <hr style="margin:32px 0;"/>

    <!-- ====== Projects ====== -->
    <h2>Selected Projects</h2>

    <!-- TransLink Project -->
    <div style="background:#f9fbff;border:1px solid #e6edf5;border-radius:10px;padding:22px;margin-bottom:16px;">
      <h3 style="margin-top:0;">TransLink GTFS Data Warehouse</h3>

      <p style="color:#6b7280;margin-top:6px;">
        <strong>Problem:</strong> Transit GTFS data appears structured but contains hidden complexities such as non-standard time values (beyond 24:00), loosely connected tables, and lack of validation, leading to unreliable analysis.
      </p>

      <p>
        Designed and built a medallion-style data warehouse (Bronze, Silver, Gold) to transform raw transit feeds into validated, analysis-ready datasets.
        Normalized GTFS time values and introduced a date dimension to enable accurate time-based analysis.
        Implemented data quality checks across layers to detect schema issues, null values, and duplicates early, preventing silent data failures.
      </p>

      <p>
        Modeled fact and dimension tables to support analysis of trip behavior, service distribution, and route utilization, and generated visual reports to highlight peak demand patterns and operational insights.
      </p>

      <p style="color:#6b7280;margin-bottom:0;">
  <strong>Result:</strong> Enabled reliable analysis of transit service patterns, including peak-hour demand, route-level trip distribution, and trip duration variability, turning raw GTFS data into a usable analytical model.
  🔗 <a href="https://github.com/bashoori/transit_data_warehouse" style="color:#2563eb;font-weight:500;">View on GitHub</a>
     </p>
    </div>

    <img
      src="https://raw.githubusercontent.com/bashoori/transit_data_warehouse/main/analysis/output/translink_visual.png"
      alt="TransLink GTFS Data Warehouse Analysis"
      style="width:100%;border-radius:10px;margin-top:14px;margin-bottom:24px;border:1px solid #e5e7eb;box-shadow:0 6px 16px rgba(0,0,0,0.05);">

    <!-- Other Projects -->
    <div style="background:#f9fbff;border:1px solid #e6edf5;border-radius:10px;padding:22px;margin-bottom:16px;">
      <h3 style="margin-top:0;">Azure ADF Retail Pipeline</h3>
      <p style="color:#6b7280;margin-top:6px;">
        <strong>Problem:</strong> Retail data from multiple regions was inconsistent and difficult to trust, making reporting unreliable.
      </p>
      <p>
        Built a pipeline in Azure Data Factory with incremental loading and monitoring to standardize data and support reliable refresh cycles.
      </p>
      <p style="color:#6b7280;margin-bottom:0;">
        <strong>Result:</strong> Reduced inconsistencies in reporting datasets and improved day-to-day data reliability.
      </p>
    </div>

    <div style="background:#f9fbff;border:1px solid #e6edf5;border-radius:10px;padding:20px;margin-bottom:16px;">
      <h3 style="margin-top:0;">Databricks Lakehouse Pipeline</h3>
      <p style="color:#6b7280;margin-top:6px;">
        <strong>Problem:</strong> Raw data lacked structure and consistency, making it difficult to use for analysis.
      </p>
      <p>
        Designed a medallion architecture pipeline using PySpark and Delta Lake to transform raw data into clean, analytics-ready datasets.
      </p>
      <p style="color:#6b7280;margin-bottom:0;">
        <strong>Result:</strong> Improved data quality and created structured layers for reliable downstream reporting.
      </p>
    </div>

    <div style="background:#f9fbff;border:1px solid #e6edf5;border-radius:10px;padding:20px;margin-bottom:16px;">
      <h3 style="margin-top:0;">Cloud ETL Modernization</h3>
      <p style="color:#6b7280;margin-top:6px;">
        <strong>Problem:</strong> Legacy ETL workflows were difficult to maintain and lacked visibility into failures.
      </p>
      <p>
        Rebuilt ETL pipelines using Airflow and AWS to improve orchestration, logging, and consistency across data workflows.
      </p>
      <p style="color:#6b7280;margin-bottom:0;">
        <strong>Result:</strong> Increased pipeline reliability and made failures easier to detect and troubleshoot.
      </p>
    </div>

      <!-- ====== Insights ====== -->
    <h2>Insights & Writing</h2>
    
    <p style="color:#6b7280;">
      I write about real data engineering challenges, focusing on things that break in production and how to design around them.
    </p>
    
    <ul style="margin-top:10px;color:#4b5563;">
      <li>Why pipelines fail silently and how to detect it</li>
      <li>Schema drift is not just a bug, it’s a design problem</li>
      <li>When to use Spark vs Pandas in real workflows</li>
    </ul>
    
    <div style="margin-top:8px;">
      <a href="https://www.linkedin.com/in/bitaashoori/recent-activity/all/" style="color:#2563eb;font-weight:500;">
        Read posts on LinkedIn →
      </a>
    </div>

    <!-- ====== Learning Course ====== -->
    <h2 style="margin-top:28px;">Learning Course</h2>
    
    <p style="color:#6b7280;">
      Building a <strong>DP-900 Azure Data Fundamentals</strong> course with practice questions,
      detailed explanations, and answer walkthroughs designed for real understanding. (Coming Soon!)
    </p>
    
    <div style="margin-top:8px;">
      <a href="YOUR_UDEMY_LINK_HERE" style="color:#2563eb;font-weight:500;">
        View course on Udemy →
      </a>
    </div>


    <!-- ====== Footer ====== -->
    <h2 style="margin-top:32px;">Stay Connected</h2>

    <div style="display:flex;justify-content:space-between;flex-wrap:wrap;gap:16px;">
      <div>
        <a href="https://github.com/bashoori">GitHub</a> ·
        <a href="https://www.linkedin.com/in/bitaashoori">LinkedIn</a>
      </div>

      <div style="color:#6b7280;">
        Open to collaboration and data conversations
      </div>

      <div>
        <img src="https://visitor-badge.laobi.icu/badge?page_id=bashoori.portfolio">
      </div>
    </div>

  </div>
</div>
