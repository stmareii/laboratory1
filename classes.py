class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def to_dict(self):
        return {"Name": self.name, "Age": self.age}


class User(Person):
    def __init__(self, name, age, user_id, weight, height):
        super().__init__(name, age)
        self.user_id = user_id
        self.weight = weight
        self.height = height

    def calculate_bmi(self):
        return self.weight / (self.height / 100) ** 2
    def to_dict(self):
        data = super().to_dict()
        data.update(
            {
                "UserID": self.user_id,
                "Weight": self.weight,
                "Height": self.height,
                "BMI": round(self.calculate_bmi(), 2),
            }
        )
        return data


class Trainer(Person):
    def __init__(self, name, age, trainer_id):
        super().__init__(name, age)
        self.trainer_id = trainer_id
    def to_dict(self):
        data = super().to_dict()
        data.update({"TrainerID": self.trainer_id})
        return data


class Exercise:
    def __init__(self, name, duration, calories_burned):
        self.name = name
        self.duration = duration
        self.calories_burned = calories_burned
    def to_dict(self):
        return {
            "Name": self.name,
            "Duration": self.duration,
            "CaloriesBurned": self.calories_burned,
        }


class Workout:
    def __init__(self, name):
        self.name = name
        self.exercises = []

    def add_exercise(self, exercise):
        self.exercises.append(exercise)
    def to_dict(self):
        return {
            "Name": self.name,
            "Exercises": [exercise.to_dict() for exercise in self.exercises],
        }


class FitnessApp:
    def __init__(self):
        self.users = []
        self.trainers = []
        self.workouts = []

    def add_user(self, user):
        self.users.append(user)

    def add_trainer(self, trainer):
        self.trainers.append(trainer)

    def add_workout(self, workout):
        self.workouts.append(workout)
    def to_dict(self):
        return {
            "Users": [user.to_dict() for user in self.users],
            "Trainers": [trainer.to_dict() for trainer in self.trainers],
            "Workouts": [workout.to_dict() for workout in self.workouts],
        }