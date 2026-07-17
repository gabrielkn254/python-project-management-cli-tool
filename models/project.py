from models.task import Task
from typing import List

class Project:
    def __init__(self, title, description, due_date, tasks: List['Task'] = []):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.tasks = tasks
    
    def __repr__(self):
        return self.title
    
    def to_dict(self):
        tasks_to_dict = [t.to_dict() for t in self.tasks]
        return {
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "tasks": tasks_to_dict,
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "Project":
        tasks_from_dict = [Task.from_dict(t) for t in data.get("tasks", [])]
        return cls(
            title=data["title"],
            description=data["description"],
            due_date=data["due_date"],
            tasks=tasks_from_dict,           
        )
    
    def add_task(self, task):
        self.tasks.append(task)