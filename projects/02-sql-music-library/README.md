
# 🎼 SQL Music Library Tracker

**DB:** SQLite

## Setup
```bash
cd projects/02-sql-music-library
sqlite3 music.db < db/schema.sql
sqlite3 music.db < db/seed.sql
```

## Run queries & export CSV
```bash
sqlite3 -header -csv music.db < queries/q1_top5_most_played.sql > reports/q1_top5_most_played.csv
sqlite3 -header -csv music.db < queries/q2_total_plays_by_artist.sql > reports/q2_total_plays_by_artist.csv
sqlite3 -header -csv music.db < queries/q3_stale_songs_30d.sql > reports/q3_stale_songs_30d.csv
```

## Reset DB
```bash
sqlite3 music.db < db/teardown.sql
rm -f music.db
```
