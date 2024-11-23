class Person:
    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age: int = age

    def to_dict(self) -> dict:
        return {"Name": self.name, "Age": self.age}


class User(Person):
    def __init__(self, name: str, age: int, user_id: int, weight: float, height: float):
        super().__init__(name, age)
        self.user_id: int = user_id
        self.weight: float = weight
        self.height: float = height

    def calculate_bmi(self) -> float | None:
        try:
            if self.height <= 0:
                raise ValueError("Рост должен быть больше 0.")
            return self.weight / (self.height / 100) ** 2
        except ZeroDivisionError:
            print("Ошибка: Деление на ноль. Проверьте рост.")  # Проверка уже есть, но оставим
            return None
        except Exception as e:
            print(f"Не удалось рассчитать ИМТ: {e}")
            return None

    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update(
            {
                "UserID": self.user_id,
                "Weight": self.weight,
                "Height": self.height,
                "BMI": round(self.calculate_bmi(), 2) if self.calculate_bmi() else "Ошибка расчёта",
            }
        )
        return data


class Trainer(Person):
    def __init__(self, name: str, age: int, trainer_id: int):
        super().__init__(name, age)
        self.trainer_id: int = trainer_id

    def to_dict(self) -> dict:
        data = super().to_dict()
        data.update({"TrainerID": self.trainer_id})
        return data


class Exercise:
    def __init__(self, name: str, duration: int, calories_burned: int):
        self.name: str = name
        self.duration: int = duration
        self.calories_burned: int = calories_burned

    def to_dict(self) -> dict:
        return {
            "Name": self.name,
            "Duration": self.duration,
            "CaloriesBurned": self.calories_burned,
        }


class Workout:
    def __init__(self, name: str):
        self.name: str = name
        self.exercises: list[Exercise] = []

    def add_exercise(self, exercise: Exercise) -> None:
        try:
            if not isinstance(exercise, Exercise):
                raise TypeError("Можно добавлять только объекты класса Exercise.")
            self.exercises.append(exercise)
        except Exception as e:
            print(f"Ошибка при добавлении упражнения: {e}")

    def to_dict(self) -> dict:
        try:
            return {
                "Name": self.name,
                "Exercises": [exercise.to_dict() for exercise in self.exercises],
            }
        except Exception as e:
            print(f"Ошибка при преобразовании тренировки в словарь: {e}")
            return {}


class FitnessApp:
    def __init__(self):
        self.users: list[User] = []
        self.trainers: list[Trainer] = []
        self.workouts: list[Workout] = []

    def add_user(self, user: User) -> None:
        try:
            if not isinstance(user, User):
                raise TypeError("Можно добавлять только объекты класса User.")
            self.users.append(user)
        except Exception as e:
            print(f"Ошибка при добавлении пользователя: {e}")

    def add_trainer(self, trainer: Trainer) -> None:
        try:
            if not isinstance(trainer, Trainer):
                raise TypeError("Можно добавлять только объекты класса Trainer.")
            self.trainers.append(trainer)
        except Exception as e:
            print(f"Ошибка при добавлении тренера: {e}")

    def add_workout(self, workout: Workout) -> None:
        try:
            if not isinstance(workout, Workout):
                raise TypeError("Можно добавлять только объекты класса Workout.")
            self.workouts.append(workout)
        except Exception as e:
            print(f"Ошибка при добавлении тренировки: {e}")

    def to_dict(self) -> dict:
        try:
            return {
                "Users": [user.to_dict() for user in self.users],
                "Trainers": [trainer.to_dict() for trainer in self.trainers],
                "Workouts": [workout.to_dict() for workout in self.workouts],
            }
        except Exception as e:
            print(f"Ошибка при преобразовании приложения в словарь: {e}")
            return {}
