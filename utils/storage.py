import json
from models import User, Project, Task

DB_PATH = "./data/db.json"

# Load data from db.json
def load_db() -> list:
    try:
        with open(DB_PATH, "r") as file:
            data = json.load(file)
            users = []
            for item in data["users"]:
                users.append(User.from_dict(item))
        return users
    
    except (json.JSONDecodeError, FileNotFoundError, PermissionError):
        return []

# Save data to db.json
def save_db(users: list):
    data = {
        "users":[user.to_dict() for user in users]
    }

    with open(DB_PATH, "w") as file:
        json.dump(data, file, indent=4)