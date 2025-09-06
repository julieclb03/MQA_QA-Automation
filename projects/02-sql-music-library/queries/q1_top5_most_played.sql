
WITH last30 AS (
  SELECT * FROM PlayCounts WHERE played_at >= datetime('now','-30 day')
)
SELECT s.title, COUNT(*) AS plays_30d
FROM last30 l
JOIN Songs s ON s.song_id = l.song_id
GROUP BY s.title
ORDER BY plays_30d DESC
LIMIT 5;
