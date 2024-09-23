import sys


# Task class to hold individual tasks
class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def __repr__(self):
        status = "Done" if self.completed else "Pending"
        return f"[{status}] {self.description}"


# TaskManager class to manage the list of tasks
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print(f"Task '{description}' added.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task}")

    def mark_task_completed(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1].completed = True
            print(f"Task {task_number} marked as completed.")
        else:
            print("Invalid task number.")

    def remove_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task.description}' removed.")
        else:
            print("Invalid task number.")


def display_menu():
    print("\nTask Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Remove Task")
    print("5. Exit")


def get_valid_choice():
    while True:
        choice = input("\nChoose an option: ")
        if choice.isdigit() and 1 <= int(choice) <= 5:
            return int(choice)
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


def get_valid(manager, action):
    while True:
        task_number = input(f"Enter task number to {action}: ")
        if task_number.isdigit() and 1 <= int(task_number) <= len(manager.tasks):
            return int(task_number)
        else:
            print(f"Invalid task no.valid number b/n 1 &{len(manager.tasks)}")


def main():
    manager = TaskManager()

    while True:
        display_menu()
        choice = get_valid_choice()

        if choice == 1:
            description = input("Enter task description: ")
            if description.strip():
                manager.add_task(description)
            else:
                print("Task description cannot be empty.")
        elif choice == 2:
            manager.view_tasks()
        elif choice == 3:
            if manager.tasks:
                task_number = get_valid(manager, "mark as completed")
                manager.mark_task_completed(task_number)
            else:
                print("No tasks available to mark as completed.")
        elif choice == 4:
            if manager.tasks:
                task_number = get_valid(manager, "remove")
                manager.remove_task(task_number)
            else:
                print("No tasks available to remove.")
        elif choice == 5:
            print("Exiting...")
            sys.exit()


if __name__ == "__main__":
    main()
