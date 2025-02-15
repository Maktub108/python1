# Создай класс Task, который позволяет управлять задачами (делами). У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено). Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.

class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"{self.description} (Срок: {self.due_date}, Статус: {status})"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        new_task = Task(description, due_date)
        self.tasks.append(new_task)

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
        else:
            print("Такой задачи не существует.")

    def list_current_tasks(self):
        current_tasks = [task for task in self.tasks if not task.completed]
        if current_tasks:
            print("Текущие задачи:")
            for i, task in enumerate(current_tasks):
                print(f"{i}. {task}")
        else:
            print("Нет текущих задач.")


task_manager = TaskManager()
task_manager.add_task("Сделать домашнее задание на python", "2025-02-15")
task_manager.add_task("Купить продукты", "2025-02-16")

task_manager.list_current_tasks()

task_manager.mark_task_completed(0)

task_manager.list_current_tasks()