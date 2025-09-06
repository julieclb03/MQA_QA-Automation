
SELECT s.title
FROM Songs s
LEFT JOIN (
  SELECT song_id, MAX(played_at) AS last_play FROM PlayCounts GROUP BY song_id
) lp ON lp.song_id = s.song_id
WHERE (lp.last_play IS NULL) OR (lp.last_play < datetime('now','-30 day'));
