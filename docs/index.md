<style>
  * {
    box-sizing: border-box;
  }

  img {
    max-width: 100%;
    height: auto;
  }

  .page-shell {
    background: linear-gradient(180deg, #f7fafc 0%, #edf3f8 100%);
    padding: 40px 20px;
  }

  .content-shell {
    max-width: 1100px;
    margin: 0 auto;
    background: #ffffff;
    padding: 36px 32px;
    border-radius: 20px;
    box-shadow: 0 14px 36px rgba(15, 23, 42, 0.08);
    border: 1px solid #e8eef5;
  }

  .hero-section {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 36px;
    flex-wrap: wrap;
    padding-bottom: 28px;
    border-bottom: 1px solid #e8eef5;
  }

  .hero-text {
    flex: 1;
    min-width: 300px;
    min-width: 0;
  }

  .hero-image-wrap {
    flex-shrink: 0;
  }

  .project-layout {
    display: grid;
    grid-template-columns: minmax(0, 1.45fr) minmax(280px, 0.95fr);
    gap: 22px;
    align-items: stretch;
    margin-top: 14px;
  }

  .project-main,
  .project-side-stack,
  .project-side-card,
  .focus-card,
  .whatido-card,
  .section-card,
  .footer-shell {
    min-width: 0;
  }

  .project-side-stack {
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  .github-mini-card {
    overflow: hidden;
  }

  .github-mini-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 12px;
    flex-wrap: wrap;
  }

  .github-badge-wrap {
    max-width: 100%;
    overflow: hidden;
  }

  .github-badge-wrap img {
    display: block;
    max-width: 100%;
    height: auto;
  }

  .project-link {
    color: #2563eb;
    font-weight: 600;
    text-decoration: none;
    overflow-wrap: anywhere;
    word-break: break-word;
  }

  .footer-shell {
    margin-top: 38px;
    padding-top: 18px;
    border-top: 1px solid #e8eef5;
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 16px;
    align-items: center;
  }

  @media (max-width: 900px) {
    .project-layout {
      display: grid !important;
      grid-template-columns: 1fr !important;
      gap: 16px !important;
    }
  }

  @media (max-width: 768px) {
    .page-shell {
      padding: 20px 12px;
    }

    .content-shell {
      padding: 22px 16px;
      border-radius: 16px;
    }

    .hero-section {
      gap: 20px;
      padding-bottom: 22px;
    }

    .hero-text {
      min-width: 0;
      width: 100%;
    }

    .hero-image-wrap {
      width: 100%;
      display: flex;
      justify-content: center;
    }

    .hero-image {
      width: 140px !important;
      height: 140px !important;
    }

    .project-layout {
      display: grid !important;
      grid-template-columns: 1fr !important;
      gap: 16px !important;
    }

    .github-mini-row {
      align-items: flex-start;
    }

    h1 {
      font-size: 2.2em !important;
    }

    h2 {
      font-size: 1.65em !important;
    }

    h3 {
      line-height: 1.35;
    }
  }

  @media (max-width: 480px) {
    .content-shell {
      padding: 18px 14px;
    }

    .page-shell {
      padding: 14px 8px;
    }

    .hero-image {
      width: 120px !important;
      height: 120px !important;
    }

    h1 {
      font-size: 1.9em !important;
    }

    h2 {
      font-size: 1.45em !important;
    }
  }
</style>

<!-- ====== Page Background Wrapper ====== -->
<div class="page-shell" style="background:linear-gradient(180deg, #f7fafc 0%, #edf3f8 100%);padding:40px 20px;">

  <!-- ====== Content Container ====== -->
  <div class="content-shell" style="max-width:1100px;margin:0 auto;background:#ffffff;padding:36px 32px;border-radius:20px;box-shadow:0 14px 36px rgba(15,23,42,0.08);border:1px solid #e8eef5;">

    <!-- ====== Header ====== -->
    <div class="hero-section" style="display:flex;align-items:center;justify-content:space-between;gap:36px;flex-wrap:wrap;padding-bottom:28px;border-bottom:1px solid #e8eef5;">

      <div class="hero-text" style="flex:1;min-width:300px;">

        <div style="display:inline-block;font-size:0.85em;color:#4b6fa9;font-weight:700;letter-spacing:2px;text-transform:uppercase;background:#f3f7fd;padding:8px 14px;border-radius:999px;margin-bottom:14px;">
          Data Engineer
        </div>

        <h1 style="margin:0;font-size:3em;color:#0f172a;line-height:1.1;font-weight:800;">
          Bita Ashoori
        </h1>

        <p style="margin:16px 0 0;font-size:1.28em;color:#334155;max-width:680px;line-height:1.5;">
          I design data systems that turn fragmented and unreliable data into something teams can actually trust.
        </p>

        <p style="margin:18px 0 0;color:#64748b;line-height:1.75;max-width:700px;font-size:1.03em;">
          I bring 5 years of experience across data engineering and business intelligence, including 3 years focused on data engineering and 2 years in BI, working in healthcare and e-commerce environments.
        </p>

        <p style="margin:12px 0 0;color:#64748b;line-height:1.75;max-width:700px;font-size:1.03em;">
          I have built and maintained data pipelines and analytical datasets using SQL Server, Python, SSIS, Apache Airflow, Azure, and Power BI, with a focus on turning fragmented source data into structured, reliable systems.
        </p>

        <p style="margin:12px 0 0;color:#64748b;line-height:1.75;max-width:700px;font-size:1.03em;">
          My work emphasizes data quality, validation, and modeling decisions so the data behaves correctly and can be trusted in real use.
        </p>

        <div style="display:flex;flex-wrap:wrap;gap:12px;margin-top:22px;">
          <a href="https://github.com/bashoori" style="text-decoration:none;color:#1d4ed8;font-weight:600;background:#f8fbff;border:1px solid #dce8f8;padding:10px 16px;border-radius:12px;">GitHub</a>
          <a href="https://www.linkedin.com/in/bitaashoori" style="text-decoration:none;color:#1d4ed8;font-weight:600;background:#f8fbff;border:1px solid #dce8f8;padding:10px 16px;border-radius:12px;">LinkedIn</a>
        </div>

        <p style="margin:18px 0 0;color:#64748b;font-size:1.02em;">
          📍 Vancouver, BC
        </p>

      </div>

      <!-- ====== Profile Image ====== -->
      <div class="hero-image-wrap" style="flex-shrink:0;">
        <div class="hero-image" style="width:190px;height:190px;border-radius:50%;overflow:hidden;border:4px solid #f8fafc;box-shadow:0 10px 24px rgba(15,23,42,0.12);background:#fff;">
          <img
            src="https://raw.githubusercontent.com/bashoori/portfolio/main/docs/images/profile_resized.jpg"
            alt="Bita Ashoori"
            style="width:100%;height:100%;object-fit:cover;object-position:center;" />
        </div>
      </div>

    </div>

    <!-- ====== Current Focus ====== -->
    <div class="section-card" style="margin-top:28px;background:linear-gradient(180deg, #f9fbff 0%, #f3f7fc 100%);border:1px solid #e3ebf5;border-radius:16px;padding:22px 24px;">
      <h2 style="margin:0 0 12px;color:#0f172a;font-size:2em;">Current Focus</h2>
      <p style="margin:0;color:#475569;max-width:860px;line-height:1.75;font-size:1.03em;">
        Advancing skills in Microsoft Fabric and lakehouse architecture, with active preparation for DP-700. Open to new data engineering opportunities.
      </p>
    </div>

    <!-- ====== Summary Highlights ====== -->
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;margin-top:22px;">
      <div class="focus-card" style="background:#ffffff;border:1px solid #e6edf5;border-radius:14px;padding:18px 20px;box-shadow:0 4px 14px rgba(15,23,42,0.04);">
        <div style="font-size:1.5em;margin-bottom:8px;">✔</div>
        <div style="color:#0f172a;font-weight:700;margin-bottom:4px;">5 years of experience</div>
        <div style="color:#64748b;line-height:1.6;">Across data engineering and business intelligence</div>
      </div>

      <div class="focus-card" style="background:#ffffff;border:1px solid #e6edf5;border-radius:14px;padding:18px 20px;box-shadow:0 4px 14px rgba(15,23,42,0.04);">
        <div style="font-size:1.5em;margin-bottom:8px;">⚙</div>
        <div style="color:#0f172a;font-weight:700;margin-bottom:4px;">Core tools</div>
        <div style="color:#64748b;line-height:1.6;">SQL Server, Python, SSIS, Airflow, Azure, Power BI</div>
      </div>

      <div class="focus-card" style="background:#ffffff;border:1px solid #e6edf5;border-radius:14px;padding:18px 20px;box-shadow:0 4px 14px rgba(15,23,42,0.04);">
        <div style="font-size:1.5em;margin-bottom:8px;">🏥</div>
        <div style="color:#0f172a;font-weight:700;margin-bottom:4px;">Industries</div>
        <div style="color:#64748b;line-height:1.6;">Healthcare and e-commerce environments</div>
      </div>
    </div>

    <!-- ====== What I Do ====== -->
    <h2 style="margin-top:34px;color:#0f172a;font-size:2em;">What I Do</h2>

    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:18px;margin-top:14px;">

      <div class="whatido-card" style="background:#f9fbff;border:1px solid #e3ebf5;border-radius:16px;padding:22px 20px;box-shadow:0 6px 18px rgba(15,23,42,0.04);">
        <div style="font-size:1.6em;margin-bottom:8px;">🔗</div>
        <h3 style="margin:0 0 12px;color:#111827;">Data Pipelines</h3>
        <ul style="margin:0;padding-left:18px;color:#475569;line-height:1.8;">
          <li>Design reliable workflows</li>
          <li>Handle messy real-world data</li>
          <li>Ensure consistent delivery</li>
        </ul>
      </div>

      <div class="whatido-card" style="background:#f9fbff;border:1px solid #e3ebf5;border-radius:16px;padding:22px 20px;box-shadow:0 6px 18px rgba(15,23,42,0.04);">
        <div style="font-size:1.6em;margin-bottom:8px;">🗂</div>
        <h3 style="margin:0 0 12px;color:#111827;">Data Modeling</h3>
        <ul style="margin:0;padding-left:18px;color:#475569;line-height:1.8;">
          <li>Structure datasets for analysis</li>
          <li>Define business logic</li>
          <li>Support trusted reporting</li>
        </ul>
      </div>

      <div class="whatido-card" style="background:#f9fbff;border:1px solid #e3ebf5;border-radius:16px;padding:22px 20px;box-shadow:0 6px 18px rgba(15,23,42,0.04);">
        <div style="font-size:1.6em;margin-bottom:8px;">☁</div>
        <h3 style="margin:0 0 12px;color:#111827;">Modern Platforms</h3>
        <ul style="margin:0;padding-left:18px;color:#475569;line-height:1.8;">
          <li>Move workflows to cloud</li>
          <li>Apply lakehouse patterns</li>
          <li>Improve performance</li>
        </ul>
      </div>

    </div>

    <!-- ====== Projects ====== -->
    <h2 style="margin-top:38px;color:#0f172a;font-size:2em;">Selected Projects</h2>

    <div class="project-layout" style="display:grid;grid-template-columns:minmax(0,1.45fr) minmax(280px,0.95fr);gap:22px;align-items:stretch;margin-top:14px;">

      <!-- ====== TransLink Project ====== -->
      <div class="project-main" style="background:#f9fbff;border:1px solid #e3ebf5;border-radius:18px;padding:24px;box-shadow:0 8px 22px rgba(15,23,42,0.05);">
        <div style="font-size:1.4em;margin-bottom:8px;">🚍</div>
        <h3 style="margin:0 0 14px;color:#0f172a;font-size:1.7em;">TransLink GTFS Data Warehouse</h3>

        <p style="color:#64748b;line-height:1.8;margin:0 0 14px;">
          <strong style="color:#111827;">Problem:</strong> Transit GTFS data appears structured but contains hidden complexities such as non-standard time values (beyond 24:00), loosely connected tables, and lack of validation.
        </p>

        <p style="color:#334155;line-height:1.8;margin:0 0 14px;">
          Built a medallion-style data warehouse (Bronze, Silver, Gold) to transform raw transit feeds into validated, analysis-ready datasets.
          Introduced time normalization and data quality checks to prevent silent failures.
        </p>

        <p style="color:#64748b;line-height:1.8;margin:0 0 16px;">
          <strong style="color:#111827;">Result:</strong> Enabled reliable analysis of transit patterns and operational insights.
          🔗 <a class="project-link" href="https://github.com/bashoori/transit_data_warehouse" style="color:#2563eb;font-weight:600;text-decoration:none;">View on GitHub</a>
        </p>

        <div style="overflow:hidden;border-radius:14px;border:1px solid #e5e7eb;background:#ffffff;box-shadow:0 6px 16px rgba(15,23,42,0.04);">
          <img
            src="https://raw.githubusercontent.com/bashoori/transit_data_warehouse/main/analysis/output/translink_visual.png"
            alt="TransLink GTFS Data Warehouse Analysis"
            style="width:100%;display:block;" />
        </div>
      </div>

      <!-- ====== Side Dashboard / Credibility Stack ====== -->
      <div class="project-side-stack" style="display:flex;flex-direction:column;gap:16px;">

        <div class="project-side-card" style="background:#ffffff;border:1px solid #e3ebf5;border-radius:16px;padding:18px 20px;box-shadow:0 8px 22px rgba(15,23,42,0.05);">
          <h3 style="margin:0 0 12px;color:#0f172a;font-size:1.35em;">Project Snapshot</h3>
          <p style="margin:0;color:#475569;line-height:1.75;">
            Built on real transit data, with medallion architecture, time normalization, and validation designed to make the data usable for analysis.
          </p>
        </div>

        <div class="project-side-card" style="background:#ffffff;border:1px solid #e3ebf5;border-radius:16px;padding:18px 20px;box-shadow:0 8px 22px rgba(15,23,42,0.05);">
          <h3 style="margin:0 0 12px;color:#0f172a;font-size:1.35em;">Signals</h3>
          <ul style="margin:0;padding-left:18px;color:#475569;line-height:1.8;">
            <li>Real GTFS dataset</li>
            <li>Time-aware dimensional modeling</li>
            <li>Pipeline validation across layers</li>
            <li>Analysis-ready outputs and visuals</li>
          </ul>
        </div>

      </div>

    </div>

    <!-- ====== Insights ====== -->
    <h2 style="margin-top:38px;color:#0f172a;font-size:2em;">Insights & Writing</h2>

    <div class="section-card" style="background:#f9fbff;border:1px solid #e3ebf5;border-radius:16px;padding:22px 24px;margin-top:12px;box-shadow:0 6px 18px rgba(15,23,42,0.04);">
      <p style="color:#64748b;max-width:820px;line-height:1.75;margin:0 0 12px;">
        I write about real data engineering challenges, focusing on things that break in production and how to design around them.
      </p>

      <ul style="margin:0;padding-left:20px;color:#475569;line-height:1.85;">
        <li>Why pipelines fail silently and how to detect it</li>
        <li>Schema drift is not just a bug, it’s a design problem</li>
        <li>When to use Spark vs Pandas in real workflows</li>
      </ul>

      <div style="margin-top:14px;">
        <a href="https://www.linkedin.com/in/bitaashoori/recent-activity/all/" style="color:#2563eb;font-weight:600;text-decoration:none;">
          Read posts on LinkedIn →
        </a>
      </div>
    </div>

    <!-- ====== Learning Course ====== -->
    <h2 style="margin-top:34px;color:#0f172a;font-size:2em;">Learning Course</h2>

    <div class="section-card" style="background:#f9fbff;border:1px solid #e3ebf5;border-radius:16px;padding:22px 24px;margin-top:12px;box-shadow:0 6px 18px rgba(15,23,42,0.04);">
      <p style="color:#64748b;line-height:1.75;margin:0;">
        Building a <strong style="color:#111827;">DP-900 Azure Data Fundamentals</strong> Practice Test,
        detailed explanations, and answer walkthroughs designed for real understanding. (Coming Soon!)
      </p>
    </div>

    <!-- 
    <div style="margin-top:10px;">
      <a href="YOUR_UDEMY_LINK_HERE" style="color:#2563eb;font-weight:500;">
        View course on Udemy →
      </a>
    </div>
    -->

    <!-- ====== Education & Certifications ====== -->
    <h2 style="margin-top:34px;color:#0f172a;font-size:2em;">Education & Certifications</h2>

    <div class="section-card" style="background:#f9fbff;border:1px solid #e3ebf5;border-radius:16px;padding:22px 24px;margin-top:12px;box-shadow:0 6px 18px rgba(15,23,42,0.04);">
      <p style="margin:0 0 12px;color:#111827;"><strong>Microsoft Certified: Azure Data Fundamentals (DP-900)</strong></p>
      <p style="margin:0 0 12px;color:#111827;"><strong>Academy Accreditation - Databricks Fundamentals</strong> — Databricks</p>
      <p style="margin:0 0 12px;color:#111827;"><strong>Academy Accreditation - Generative AI Fundamentals</strong> — Databricks</p>
      <p style="margin:0 0 12px;color:#111827;"><strong>20778 Analyzing Data with Power BI</strong> — New Horizons</p>
      <p style="margin:0 0 12px;color:#111827;">
        <strong>BCIT, Associate Certificate in Applied Database Administration & Design</strong>
      </p>
      <p style="margin:0 0 12px;color:#111827;">
        <strong>Azad University (IAU), Bachelor of Applied Science (BASc), Applied Mathematics in Computer Science</strong><br/>
      </p>
      <p style="margin:0;color:#64748b;">
        Currently preparing for <strong style="color:#111827;">Microsoft Fabric Data Engineer (DP-700)</strong>
      </p>
    </div>

    <!-- ====== Footer ====== -->
    <div class="footer-shell" style="margin-top:38px;padding-top:18px;border-top:1px solid #e8eef5;display:flex;justify-content:space-between;flex-wrap:wrap;gap:16px;align-items:center;">

      <div>
        <a href="https://github.com/bashoori" style="color:#2563eb;text-decoration:none;">GitHub</a> ·
        <a href="https://www.linkedin.com/in/bitaashoori" style="color:#2563eb;text-decoration:none;">LinkedIn</a>
      </div>

      <div style="color:#6b7280;">
        Open to collaboration and data conversations
      </div>

      <div class="github-badge-wrap">
        <img src="https://komarev.com/ghpvc/?username=bashoori&color=0e75b6&label=Views" alt="Views" />
      </div>

    </div>

  </div>
</div>
