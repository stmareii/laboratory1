import json
from models import FitnessApp, User, Trainer, Workout, Exercise

class JSONSerializer:
    def __init__(self, app: FitnessApp):
        self.app = app

    def save_to_json(self, file_name: str) -> bool:
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(self.app.to_dict(), f, indent=4, ensure_ascii=False)
        return True
    def load_from_json(self, file_name: str) -> FitnessApp:
        with open(file_name, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        app = FitnessApp()
        for user_data in data.get("Users", []):
            user = User(
                name=user_data["Name"],
                age=user_data["Age"],
                user_id=user_data["UserID"],
                weight=user_data["Weight"],
                height=user_data["Height"]
            )
            app.add_user(user)
    