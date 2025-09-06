
import json, os, sys, subprocess, tempfile, pathlib

def test_metrics_file_created():
  root = pathlib.Path(__file__).resolve().parents[1]
  out = tempfile.NamedTemporaryFile(delete=False).name
  cmd = [
    sys.executable, "-m", "src.recommender",
    "--input", str(root/"data/tracks_features.csv"),
    "--profiles", str(root/"data/user_profiles.json"),
    "--out", out
  ]
  subprocess.check_call(cmd, cwd=root)
  assert os.path.exists(out)
  data = json.loads(open(out).read())
  assert "Lauren" in data and "precision_at_3" in data["Lauren"]
