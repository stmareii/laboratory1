
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class User(Person):
    def __init__(self, name, age, user_id, weight, height):
        super().__init__(name, age)
        self.user_id = user_id
        self.weight = weight
        self.height = height
    def calculate_bmi(self):
        return self.weight / (self.height / 100) ** 2

class Trainer(Person):
    def __init__(self, name, age, trainer_id):
        super().__init__(name, age)
        self.trainer_id = trainer_id


class Exercise:
    def __init__(self, name, duration, calories_burned):
        self.name = name
        self.duration = duration
        self.calories_burned = calories_burned


class Workout:
    def __init__(self, name):
        self.name = name
        self.exercises = []

    def add_exercise(self, exercise):
        self.exercises.append(exercise)


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

