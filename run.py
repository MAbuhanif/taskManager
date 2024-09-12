import sys


# task class to hold individual tasks
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
        self.tasks=[]

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
