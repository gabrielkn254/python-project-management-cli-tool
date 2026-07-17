from models.person import Person
from models.project import Project
from typing import List

class User(Person):
    id_counter = 1

    def __init__(self, name, email, id: int = None, projects: List['Project'] = []):
        super().__init__(name, email)
        self.id = id
        self.projects = projects

        if self.id is None:
            self.id = User.id_counter
            User.id_counter += 1
        else:
            if self.id >= User.id_counter:
                User.id_counter = self.id + 1
    
    def to_dict(self):
        projects_to_dict = [p.to_dict() for p in self.projects]
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "projects": projects_to_dict
        }
    
    def __repr__(self) -> str:
        return self.name
    
    @classmethod
    def from_dict(cls, data: dict) -> "User":
        projects_from_dict = [Project.from_dict(p) for p in data.get("projects", [])]
        return cls(
            id=data["id"],
            name=data["name"],
            email=data["email"],
            projects=projects_from_dict
            )
    
    def assign_project(self, project):
        self.projects.append(project)