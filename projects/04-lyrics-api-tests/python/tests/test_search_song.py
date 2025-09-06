
import os, requests
BASE = os.getenv("API_BASE","https://api.deezer.com")
def test_search_returns_200_and_items():
  r = requests.get(f"{BASE}/search", params={"q":"H.E.R."})
  assert r.status_code == 200
  js = r.json()
  assert "data" in js and isinstance(js["data"], list)
