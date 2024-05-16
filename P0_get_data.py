import requests
import tempfile
import os
import time
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

f_name = "current-projects-u.json"
f_save = Path("data") / f_name
target_url = "https://nairrpilot.org/app/site/data/" + f_name

if not is_file_not_older_than_one_day(f_save):
    r = requests.get(target_url)
    print(f"Downloading {target_url}")
    
    assert r.ok

    with open(f_save, 'wb') as FOUT:
        FOUT.write(r.content)
        
    print(f"Saved {f_save}")

