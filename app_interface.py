from classes import FitnessApp, User, Trainer, Workout, Exercise
from serializer import JSONSerializer

def test_classes():
    app = FitnessApp()
    user1 = User(name="Ivan", age=30, user_id=1, weight=80, height=180)
    user2 = User(name="Ann", age=25, user_id=2, weight=60, height=165)
    app.add_user(user1)
    app.add_user(user2)

    print(f"Иван BMI: {user1.calculate_bmi():.2f}")
    print(f"Анна BMI: {user2.calculate_bmi():.2f}")

    trainer1 = Trainer(name="Mark", age=35, trainer_id=1)
    trainer2 = Trainer(name="Mary", age=28, trainer_id=2)
    app.add_trainer(trainer1)
    app.add_trainer(trainer2)
    exercise1 = Exercise(name="Sitting", duration=10, calories_burned=50)
    exercise2 = Exercise(name="Jumping", duration=5, calories_burned=30)
    exercise3 = Exercise(name="Running", duration=15, calories_burned=70)

    workout1 = Workout(name="Morning gym")
    workout1.add_exercise(exercise1)
    workout1.add_exercise(exercise2)

    workout2 = Workout(name="Intensive tr")
    workout2.add_exercise(exercise3)

    app.add_workout(workout1)
    app.add_workout(workout2)

    serializer = JSONSerializer(app)
    json_file = "fitness_app_data.json"
    if serializer.save_to_json(json_file):
        print(f"Данные успешно сохранены в файл {json_file}")

    # Десериализация из JSON
    try:
        loaded_app = serializer.load_from_json(json_file)
        print("Данные успешно загружены из файла.")

        print("Пользователи из загруженного приложения:")
        for user in loaded_app.users:
            print(user.to_dict())

        print("Тренеры из загруженного приложения:")
        for trainer in loaded_app.trainers:
            print(trainer.to_dict())

        print("Тренировки из загруженного приложения:")
        for workout in loaded_app.workouts:
            print(workout.to_dict())

    except Exception as e:
        print(f"Ошибка при загрузке данных: {e}")


if __name__ == "__main__":
    test_classes()
