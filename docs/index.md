<!-- ====== Page Background Wrapper ====== -->
<div style="background:linear-gradient(to bottom, #f8fafc, #eef2f7);padding:36px 18px;">

  <!-- ====== Content Container ====== -->
  <div style="max-width:1000px;margin:0 auto;background:#ffffff;padding:32px 28px;border-radius:16px;box-shadow:0 10px 30px rgba(0,0,0,0.05);">

    <!-- ====== Projects ====== -->
    <h2>Selected Projects</h2>

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
      </p>
    </div>

    <img src="analysis/output/combined_report.png" 
         style="width:100%;border-radius:10px;margin-top:14px;border:1px solid #e5e7eb;box-shadow:0 6px 16px rgba(0,0,0,0.05);">

    
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

  </div>
</div>
