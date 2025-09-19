-- 📊 SQL: heart_rate_window.sql
-- Goal: For each user, compute 7-day rolling average heart rate and mark the latest entry

SELECT
  user_id,
  heart_rate,
  recorded_at,
  AVG(heart_rate) OVER (
    PARTITION BY user_id
    ORDER BY recorded_at
    ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
  ) AS avg_hr_7d,
  CASE
    WHEN recorded_at = MAX(recorded_at) OVER (PARTITION BY user_id)
    THEN TRUE ELSE FALSE
  END AS is_latest
FROM heart_rate_logs;
