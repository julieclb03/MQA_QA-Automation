
# 🎤 Lyrics & Music Metadata API Tests

## Option A: Postman + Newman (HTML report)
```bash
npm install -g newman newman-reporter-htmlextra
cd projects/04-lyrics-api-tests
newman run postman/lyrics_collection.json -e postman/env.example.json -r htmlextra --reporter-htmlextra-export newman-reports/index.html
```

## Option B: Python requests + pytest
```bash
cd projects/04-lyrics-api-tests/python
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
API_BASE=https://api.deezer.com pytest -q
```
