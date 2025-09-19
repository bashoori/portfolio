-- models/stg_event_logs.sql
SELECT
  event_id,
  user_id,
  event_type,
  feature_name,
  CAST(timestamp AS TIMESTAMP) AS event_time
FROM {{ source('raw', 'event_logs') }}
