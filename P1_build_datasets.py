from pathlib import Path
import pandas as pd
import json

f_json = "data/current-projects.json"

data = []

for f_json in Path("data").glob("*_current-projects.json"):
    with open(f_json) as FIN:
        js = json.load(FIN)

        data.extend(js["projects"])


for page in data:
    for key in ["resources", "requestedResources"]:
        if key in page:
            del page[key]

df = pd.DataFrame(data)
key = "requestNumber"
df = df.sort_values(key)
df = df.drop_duplicates(subset=[key])
df = df.set_index(key)

f_save = Path(f_json).with_suffix(".csv")

# We don't know how many pages so we just grab extra, kill those
f_save = "data/consolidated_projects.csv"
df.to_csv(f_save)

print(df)
