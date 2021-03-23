import requests
import json

r = requests.get(f"https://jobs.github.com/positions.json?search=python")
if r != 200:
    data = json.dumps(r.json(), indent=4)
else:
    print(f"ERROR: {r.status_code}, {r.reason}")

with open("dump.json", "w") as f:
    f.write(data)