
import json, argparse, pandas as pd
import os    # <-- add this line

def parse():
  ap = argparse.ArgumentParser()
  ap.add_argument("--input", required=True)
  ap.add_argument("--profiles", required=True)
  ap.add_argument("--out", required=True)
  return ap.parse_args()

def score(track, profile):
  genre_ok = any(track.get(f"genre_{g}",0)==1 for g in profile["genres"])
  tempo_penalty = 0 if track["tempo"] <= profile["max_tempo"] else -1
  target = {"chill": (0.45, 0.5), "worship": (0.4, 0.6)}.get(profile["mood"], (0.5,0.5))
  target_energy, target_valence = target
  sim = 1 - abs(track["valence"]-target_valence) - abs(track["energy"]-target_energy)
  return (1 if genre_ok else 0) + tempo_penalty + sim

def main():
  args = parse()
  df = pd.read_csv(args.input)
  with open(args.profiles) as f:
    profiles = json.load(f)
  metrics = {}
  for prof in profiles:
    scored = df.copy()
    scored["score"] = scored.apply(lambda r: score(r.to_dict(), prof), axis=1)
    recs = scored.sort_values("score", ascending=False).head(3).to_dict(orient="records")
    valid = [ (row["tempo"]<=prof["max_tempo"]) and any(row.get(f"genre_{g}",0)==1 for g in prof["genres"]) for row in recs ]
    precision = sum(valid)/len(recs)
    metrics[prof["user"]] = {"precision_at_3": precision, "recs":[{"title":r["title"],"score":round(float(r["score"]),3)} for r in recs]}
  os.makedirs(os.path.dirname(args.out), exist_ok=True)
  with open(args.out,"w") as f:
    json.dump(metrics,f,indent=2)

if __name__=="__main__":
  main()
