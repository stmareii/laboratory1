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

        for trainer_data in data.get("Trainers", []):
            trainer = Trainer(
                name=trainer_data["Name"],
                age=trainer_data["Age"],
                trainer_id=trainer_data["TrainerID"]
            )
            app.add_trainer(trainer)

        for workout_data in data.get("Workouts", []):
            workout = Workout(name=workout_data["Name"])
            for exercise_data in workout_data.get("Exercises", []):
                exercise = Exercise(
                    name=exercise_data["Name"],
                    duration=exercise_data["Duration"],
                    calories_burned=exercise_data["CaloriesBurned"]
                )
                workout.add_exercise(exercise)
            app.add_workout(workout)
        
        return app
