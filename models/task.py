class Task:
    def __init__(self, title, assigned_to):
        self.title = title
        self.status = False
        self.assigned_to = assigned_to
    
    def __repr__(self):
        return self.title
    
    def to_dict(self):
        return {
            "title": self.title,
            "status": "Completed" if self.status else "Incomplete",
            "assigned_to": self.assigned_to
        }
    def complete_task(self):
        self.status = True
        print(f"Task: {self.title} marked complete")