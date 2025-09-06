
DROP TABLE IF EXISTS Artists;
DROP TABLE IF EXISTS Albums;
DROP TABLE IF EXISTS Songs;
DROP TABLE IF EXISTS PlayCounts;

CREATE TABLE Artists (
  artist_id INTEGER PRIMARY KEY,
  name TEXT NOT NULL
);

CREATE TABLE Albums (
  album_id INTEGER PRIMARY KEY,
  artist_id INTEGER NOT NULL,
  title TEXT NOT NULL,
  release_year INT,
  FOREIGN KEY(artist_id) REFERENCES Artists(artist_id)
);

CREATE TABLE Songs (
  song_id INTEGER PRIMARY KEY,
  album_id INTEGER NOT NULL,
  title TEXT NOT NULL,
  duration_sec INT,
  genre TEXT,
  FOREIGN KEY(album_id) REFERENCES Albums(album_id)
);

CREATE TABLE PlayCounts (
  play_id INTEGER PRIMARY KEY,
  song_id INTEGER NOT NULL,
  played_at DATETIME NOT NULL,
  FOREIGN KEY(song_id) REFERENCES Songs(song_id)
);
