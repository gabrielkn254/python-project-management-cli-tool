from models.person import Person
from models.project import Project

class User(Person):
    def __init__(self, name, email, user_id: int = None):
        super().__init__(name, email)
        self.id = id
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "projects": self.projects
        }
    
    def __repr__(self):
        return self.name
    
    @classmethod
    def from_dict(cls, data: dict) -> "User":
        projects = [Project.from_dict(p) for p in data.get("projects", [])]
        return cls(
            id=data["id"],
            name=data["name"],
            email=data["email"],
            projects=projects
            )
    
    def assign_project(self, project):
        self.projects.append(project)
        project.owner = self
    