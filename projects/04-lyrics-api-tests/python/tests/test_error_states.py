
import os, requests
BASE = os.getenv("API_BASE","https://api.deezer.com")
def test_nonexistent_resource_returns_reasonable_error():
  r = requests.get(f"{BASE}/track/000000")
  assert r.status_code in (200,404)
