
INSERT INTO Artists (artist_id, name) VALUES (1,'LDB'),(2,'Fauntleroy'),(3,'H.E.R.');

INSERT INTO Albums (album_id, artist_id, title, release_year) VALUES
 (1,1,'Life in C Major',2025),
 (2,2,'After Hours',2023),
 (3,3,'City Lights',2024);

INSERT INTO Songs (song_id, album_id, title, duration_sec, genre) VALUES
 (1,1,'Meant to Be',210,'R&B'),
 (2,1,'Holy Ground',240,'Gospel'),
 (3,2,'Late Night',200,'R&B'),
 (4,3,'Blue Hour',230,'Alt R&B');

-- Plays (spread across last 40 days)
INSERT INTO PlayCounts (song_id, played_at) VALUES
 (1, datetime('now','-1 day')),
 (1, datetime('now','-2 day')),
 (1, datetime('now','-10 day')),
 (2, datetime('now','-35 day')),
 (3, datetime('now','-3 day')),
 (3, datetime('now','-4 day')),
 (4, datetime('now','-7 day')),
 (4, datetime('now','-15 day'));
