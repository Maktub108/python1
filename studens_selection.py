import random

def choose_students(students, number_to_choose=5):
    # Удаляем дубликаты
    unique_students = list(set(students))

    if len(unique_students) < number_to_choose:
        print("Недостаточно уникальных учащихся для выбора.")
        return []

    # Выбираем уникальные имена
    chosen_students = random.sample(unique_students, number_to_choose)
    return chosen_students

# Список учащихся (возможны дубликаты)
students = [
    "Алексей", "Мария", "Иван", "Ольга", "Петр",
    "Елена", "Николай", "Анна", "Дмитрий", "Светлана", "Алексей"
]

# Выбор имен
selected_students = choose_students(students)

# Вывод результата
if selected_students:
    print("Выбранные учащиеся для ответа на уроке:")
    for student in selected_students:
        print(student)

