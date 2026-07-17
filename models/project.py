from models.task import Task
class Project:
    def __init__(self, title, description, due_date, user_id):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.tasks = []
        self.owner = user_id
    
    def __repr__(self):
        return self.title
    
    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "tasks": self.tasks,
            "owner": self.owner
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "Project":
        tasks = [Task.from_dict(t) for t in data.get("tasks", [])]
        return cls(
            title=data["title"],
            description=data["description"],
            due_date=data["due_date"],
            tasks=tasks,
            owner=data["owner"]            
        )
    
    def add_task(self, task):
        self.tasks.append(task)