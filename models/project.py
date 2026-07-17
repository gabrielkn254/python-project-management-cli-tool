class Project:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.tasks = []
    
    def __repr__(self):
        return self.title
    
    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "tasks": self.tasks
        }
    
    def add_task(self, task):
        self.tasks.append(task)