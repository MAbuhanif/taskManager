import sys


# task class to hold individual tasks
class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def __repr__(self):
        status = "Done" if self.completed else "Pending"
        return f"[{status}] {self.description}"
