import requests
import os
from datetime import datetime

USERNAME = "chinmay.babar"
PASSWORD = "kohler@123"

ENVS = {
    "dev": "kohler-dev.b.lucidworks.cloud",
    "stg": "kohler-stg.b.lucidworks.cloud",
    "prod": "kohler.b.lucidworks.cloud"
}

BRANDS = [
    "kohler",
    "annsacks",
    "sterling",
    "kohler-canada"
]

PIPELINES = [
    "PLP",
    "PDP",
    "Search"
]

today = datetime.today().strftime("%Y-%m-%d")
BASE_DIR = f"fusion_backups/{today}"

os.makedirs(BASE_DIR, exist_ok=True)

for env, host in ENVS.items():
    for brand in BRANDS:
        for ptype in PIPELINES:

            pipeline_id = f"pipeline_{brand}_{ptype}"

            url = f"https://{host}/api/objects/export?query-pipeline.ids={pipeline_id}&deep=true"

            file_dir = f"{BASE_DIR}/{env}/{brand}"
            os.makedirs(file_dir, exist_ok=True)

            file_path = f"{file_dir}/{ptype}.zip"

            r = requests.get(
                url,
                auth=(USERNAME, PASSWORD),
                timeout=60
            )

            if r.status_code == 200:
                with open(file_path, "wb") as f:
                    f.write(r.content)

                print(f"Saved {pipeline_id}")

            else:
                print(f"Failed {pipeline_id} -> {r.status_code}")