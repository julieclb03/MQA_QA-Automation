
# 🤖 AI-Powered Music Recommendation Validator

### Setup
```bash
cd projects/03-ai-recs-validator
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

### Run
```bash
python -m src.recommender --input data/tracks_features.csv --profiles data/user_profiles.json --out reports/metrics.json
pytest -q
```
