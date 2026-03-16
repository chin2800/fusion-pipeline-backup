import shutil
import os
from datetime import datetime, timedelta

BACKUP_DIR = "fusion_backups"

last_week = (datetime.today() - timedelta(days=7)).strftime("%Y-%m-%d")
path = os.path.join(BACKUP_DIR, last_week)

if os.path.isdir(path):
    shutil.rmtree(path)
    print(f"Deleted old backup: {path}")
else:
    print("No old backup found")