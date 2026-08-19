import json
from pathlib import Path

DATABASE_FILE = Path("database.json")

def load_item(key):
    with open(DATABASE_FILE, "r") as file:
        data = json.load(file)

    return data.get(key, [])

