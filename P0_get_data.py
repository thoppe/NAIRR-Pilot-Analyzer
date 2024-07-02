import requests
import tempfile
import os
import time
import json
from pathlib import Path


def is_file_not_older_than_one_day(f):
    # Check if the given file is more than one day old.
    if not Path(f).exists():
        return False

    # Get the current time in seconds since the epoch
    current_time = time.time()

    # Get the modification time of the file
    modification_time = os.path.getmtime(f)

    # Calculate the time difference in seconds
    time_difference = current_time - modification_time

    # Check if the file is more than one day old (86400 seconds in a day)
    return time_difference < 86400


f_name = "current-projects.json"
target_url = "https://submit-nairr.xras.org/" + f_name


target_pages = 10

for n in range(1, target_pages + 1):
    f_save = Path("data") / f"{n:03d}_{f_name}"

    if not is_file_not_older_than_one_day(f_save):
        params = {"page": n}
        r = requests.get(target_url, params=params)
        print(f"Downloading {target_url}")

        assert r.ok

        js = json.loads(r.content)

        with open(f_save, "w") as FOUT:
            FOUT.write(json.dumps(js, indent=2))

        print(f"Saved {f_save}")
