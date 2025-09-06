
SELECT a.name AS artist, COUNT(*) AS total_plays
FROM PlayCounts p
JOIN Songs s ON s.song_id = p.song_id
JOIN Albums al ON al.album_id = s.album_id
JOIN Artists a ON a.artist_id = al.artist_id
GROUP BY a.name
ORDER BY total_plays DESC;
