-- models/nps_scores.sql
SELECT
  user_id,
  feedback_score,
  DATE(timestamp) AS feedback_date,
  CASE
    WHEN feedback_score >= 9 THEN 'Promoter'
    WHEN feedback_score >= 7 THEN 'Passive'
    ELSE 'Detractor'
  END AS nps_category
FROM {{ source('raw', 'nps_feedback') }}