-- models/user_sessions.sql
SELECT
  user_id,
  MIN(event_time) AS session_start,
  MAX(event_time) AS session_end,
  COUNT(*) AS total_events
FROM {{ ref('stg_event_logs') }}
GROUP BY user_id
