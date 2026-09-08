import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "expenses.json"

def save_data(expense_data):
    with open(DATA_FILE, "w") as file:
        json.dump(expense_data, file, indent=4)

def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError :
        print("File not found, starting with empty database")
        return {}
    except json.JSONDecodeError:
        print("Database corrupted, starting with empty database")
        return {}