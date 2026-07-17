from utils import command_actions
from models import User, Project, Task

# 1. HELPER CLASSES

class MockArgs:
    """Simulates the namespace object returned by argparse."""
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

class MockConsole:
    """Intercepts rich console prints for evaluation."""
    def __init__(self):
        self.last_output = None
        self.last_style = None

    def print(self, message, style=None):
        self.last_output = str(message)
        self.last_style = style


# 2. PYTEST CASES

def test_add_user_success(monkeypatch):
    """Test adding a brand new user successfully."""
    db_state = []
    saved_state = []
    mock_console = MockConsole()

    # Monkeypatch storage functions and rich console
    monkeypatch.setattr(command_actions, "load_db", lambda: db_state)
    monkeypatch.setattr(command_actions, "save_db", lambda data: saved_state.extend(data))
    monkeypatch.setattr(command_actions, "console", mock_console)

    args = MockArgs(name="Alice", email="alice@test.com")
    command_actions.add_user(args)

    assert len(db_state) == 1
    assert "Created User: Alice" in mock_console.last_output
    assert mock_console.last_style == "green"


def test_add_user_duplicate(monkeypatch):
    """Test that a duplicate email prevents user creation."""
    existing_user = User("Alice", "alice@test.com")
    db_state = [existing_user]
    mock_console = MockConsole()
    
    save_called = False
    def mock_save(data):
        nonlocal save_called
        save_called = True

    monkeypatch.setattr(command_actions, "load_db", lambda: db_state)
    monkeypatch.setattr(command_actions, "save_db", mock_save)
    monkeypatch.setattr(command_actions, "console", mock_console)

    args = MockArgs(name="Alice Replica", email="alice@test.com")
    command_actions.add_user(args)

    assert save_called is False
    assert "already exists" in mock_console.last_output
    assert mock_console.last_style == "orange"


def test_add_project_user_missing(monkeypatch):
    """Test project assignment failure when the user target doesn't exist."""
    mock_console = MockConsole()
    
    monkeypatch.setattr(command_actions, "load_db", lambda: [])
    monkeypatch.setattr(command_actions, "console", mock_console)

    args = MockArgs(user="GhostUser", title="Cloud Deploy")
    command_actions.add_project(args)

    assert "doesn't exists" in mock_console.last_output
    assert mock_console.last_style == "red"


def test_add_project_success(monkeypatch):
    """Test successfully assigning a project to an existing user."""
    user = User("Bob", "bob@test.com")
    user.projects = []
    mock_console = MockConsole()

    monkeypatch.setattr(command_actions, "load_db", lambda: [user])
    monkeypatch.setattr(command_actions, "save_db", lambda data: None)
    monkeypatch.setattr(command_actions, "console", mock_console)

    args = MockArgs(user="Bob", title="Engine Fix", description="Fixing engine core", due_date="2026-12-05")
    command_actions.add_project(args)

    assert len(user.projects) == 1
    assert user.projects[0].title == "Engine Fix"
    assert "assigned to" in mock_console.last_output
    assert mock_console.last_style == "green"


def test_complete_task_success(monkeypatch):
    """Test marking a pending task as complete."""
    task = Task("Write Documentation", "Bob")
    task.status = False # Task is incomplete/pending
    
    # Simple mock for complete_task inside the model if needed
    def mock_complete():
        task.status = True
    monkeypatch.setattr(task, "complete_task", mock_complete)

    project = Project("Docs Engine", "Summary info", "2026")
    project.tasks = [task]
    
    user = User("Bob", "bob@test.com")
    user.projects = [project]
    
    mock_console = MockConsole()

    monkeypatch.setattr(command_actions, "load_db", lambda: [user])
    monkeypatch.setattr(command_actions, "save_db", lambda data: None)
    monkeypatch.setattr(command_actions, "console", mock_console)

    args = MockArgs(project="Docs Engine", task="Write Documentation")
    command_actions.complete_task(args)

    assert task.status is True
    assert "marked complete" in mock_console.last_output
    assert mock_console.last_style == "green"