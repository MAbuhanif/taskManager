import sys


class Task:
    """
    Represents an individual task with a description and completion status.
    """
    def __init__(self, description):
        """
        Initialize a new Task instance
        """
        self.description = description
        self.completed = False

    def __repr__(self):
        """
        Returns a string representation of task
        """
        status = "Done" if self.completed else "Pending"
        return f"[{status}] {self.description}"


class TaskManager:
    """
    Manages a list of tasks, providing methods to add, view, complete and remove tasks.
    """
    def __init__(self):
        """
        Initializes a new Taskmanager instance with an empty task list.
        """
        self.tasks = []

    def add_task(self, description):
        """
        Adds a new task to the list
        """
        task = Task(description)
        self.tasks.append(task)
        print(f"Task '{description}' added.")

    def view_tasks(self):
        """
        Displays all tasks in the list with their status and position.
        """
        if not self.tasks:
            print("No tasks available.")
        else:
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task}")

    def mark_task_completed(self, task_no):
        """
        Marks a specified task as completed.
        """
        if 0 < task_no <= len(self.tasks):
            self.tasks[task_no - 1].completed = True
            print(f"Task {task_no} marked as completed.")
        else:
            print("Invalid task number.")

    def remove_task(self, task_no):
        """
        Removes a specified task from the list.
        """
        if 0 < task_no <= len(self.tasks):
            removed_task = self.tasks.pop(task_no - 1)
            print(f"Task '{removed_task.description}' removed.")
        else:
            print("Invalid task number.")


def display_menu():
    """
    Displays the main menu option for the task manager.
    """
    print("\nTask Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Remove Task")
    print("5. Exit")


def get_valid_choice():
    """
    Prompts the user for a valid menu choice.
    """
    while True:
        choice = input("\nChoose an option: ")
        if choice.isdigit() and 1 <= int(choice) <= 5:
            return int(choice)
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


def get_valid(manager, action):
    """
    Prompts the user for a valid task number based on the current task list.
    """
    while True:
        task_no = input(f"Enter task number to {action}: ")
        if task_no.isdigit() and 1 <= int(task_no) <= len(manager.tasks):
            return int(task_no)
        else:
            print(f"Invalid task no.valid number b/n 1 &{len(manager.tasks)}")


def main():
    """
    The main function to run the task manager program.
    """
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
                task_no = get_valid(manager, "mark as completed")
                manager.mark_task_completed(task_no)
            else:
                print("No tasks available to mark as completed.")
        elif choice == 4:
            if manager.tasks:
                task_no = get_valid(manager, "remove")
                manager.remove_task(task_no)
            else:
                print("No tasks available to remove.")
        elif choice == 5:
            print("Exiting...")
            sys.exit()


if __name__ == "__main__":
    main()
