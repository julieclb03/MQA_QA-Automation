
# 🥁 Beat Store E2E (Selenium + Pytest)

### Setup
```bash
cd projects/05-beat-store-regression
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

### Run (headless)
```bash
pytest -q --alluredir=reports/allure-results
```

**Tip:** Set `BASE_URL` to a music-themed demo site if you have one. Default uses a harmless demo.
