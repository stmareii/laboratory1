from classes import FitnessApp, User, Trainer, Workout, Exercise
from serializer import JSONSerializer

def main():
    print("Добро пожаловать в приложение FitnessApp!")
    app = None
    serializer = None

    while True:
        print("\nВы хотите создать новый файл или загрузить существующий?")
        print("1. Создать новый файл")
        print("2. Загрузить существующий файл")
        print("3. Выйти из приложения")

        choice = input("Введите номер действия: ")

        if choice == "1":
            app = FitnessApp()
            serializer = JSONSerializer(app)
            print("Новый файл создан.")
            manage_app(app, serializer)

        elif choice == "2":
            file_name = input("Введите название существующего файла (с расширением .json): ")
            try:
                app = JSONSerializer(FitnessApp()).load_from_json(file_name)
                serializer = JSONSerializer(app)
                print("Файл успешно загружен.")
                manage_app(app, serializer)
            except Exception as e:
                print(f"Ошибка при загрузке файла: {e}")

        elif choice == "3":
            print("Выход из приложения. До свидания!")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


def manage_app(app, serializer):
    while True:
        print("\nВыберите действие:")
        print("1. Добавить пользователя")
        print("2. Добавить тренера")
        print("3. Добавить тренировку")
        print("4. Просмотреть данные")
        print("5. Сохранить данные в файл")
        print("6. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            name = input("Введите имя пользователя: ")
            age = int(input("Введите возраст пользователя: "))
            user_id = int(input("Введите ID пользователя: "))
            weight = float(input("Введите вес пользователя (в кг): "))
            height = float(input("Введите рост пользователя (в см): "))
            user = User(name=name, age=age, user_id=user_id, weight=weight, height=height)
            app.add_user(user)
            print("Пользователь добавлен.")

        elif choice == "2":
            name = input("Введите имя тренера: ")
            age = int(input("Введите возраст тренера: "))
            trainer_id = int(input("Введите ID тренера: "))
            trainer = Trainer(name=name, age=age, trainer_id=trainer_id)
            app.add_trainer(trainer)
            print("Тренер добавлен.")

        elif choice == "3":
            workout_name = input("Введите название тренировки: ")
            workout = Workout(name=workout_name)
            while True:
                exercise_name = input("Введите название упражнения: ")
                duration = int(input("Введите продолжительность упражнения (в минутах): "))
                calories = int(input("Введите количество сожженных калорий: "))
                exercise = Exercise(name=exercise_name, duration=duration, calories_burned=calories)
                workout.add_exercise(exercise)
                another = input("Добавить еще одно упражнение? (y/n): ").strip().lower()
                if another == "n":
                    break
            app.add_workout(workout)
            print("Тренировка добавлена.")

        elif choice == "4":
            print("\nВыберите, какие данные вы хотите просмотреть:")
            print("1. Пользователи")
            print("2. Тренеры")
            print("3. Тренировки")
            sub_choice = input("Введите номер действия: ")
            if sub_choice == "1":
                print("\nСписок пользователей:")
                for user in app.users:
                    print(user.to_dict())
            elif sub_choice == "2":
                print("\nСписок тренеров:")
                for trainer in app.trainers:
                    print(trainer.to_dict())
            elif sub_choice == "3":
                print("\nСписок тренировок:")
                for workout in app.workouts:
                    print(workout.to_dict())
            else:
                print("Неверный выбор.")

        elif choice == "5":
            file_name = input("Введите название файла для сохранения (с расширением .json): ")
            if serializer.save_to_json(file_name):
                print(f"Данные успешно сохранены в файл {file_name}.")
            else:
                print("Ошибка при сохранении файла.")

        elif choice == "6":
            print("Возврат в главное меню.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
