from pathlib import Path
import pandas as pd
import json

f_json = "data/current-projects-u.json"

with open(f_json) as FIN:
    js = json.load(FIN)

# Check that we only have one page (not sure what it means if it changes)
assert js["pages"] == 1

js = js["projects"]

for page in js:
    for key in ["resources", "requestedResources"]:
        if key in page:
            del page[key]

df = pd.DataFrame(js)
key = "requestNumber"
df = df.sort_values(key).set_index(key)

f_save = Path(f_json).with_suffix(".csv")
df.to_csv(f_save)

print(df)
