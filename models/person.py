class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.projects = []
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty")
        else:
            self._name = value
    
    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value and "." not in value:
            raise ValueError("Invalid email format")
        self._email = value