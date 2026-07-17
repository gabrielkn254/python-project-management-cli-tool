from models import User, Project, Task
from .storage import save_db, load_db

# ACTION: add_user
def add_user(args):
    users = load_db()

    # Get user
    user = next((u for u in users if u.email.lower() == args.email.lower()), None)

    # Check if user exist, if not create user
    if not user:
        user = User(args.name, args.email)
        users.append(user)
        save_db(users)

        print(f"Created User: {args.name}")
        return
    print(f"User: {args.name} ({args.email}) already exists.")

# ACTION: list_users
def list_users(args):
    users = load_db()
    if not users:
        print("Database is empty!")
        return
    print("Listing all users")
    for user in users:
        print(f"User: {user.name} ({user.email})")

# ACTION: add_project
def add_project(args):
    users = load_db()
    # Get user from users
    user = next((u for u in users if u.name.lower() == args.user.lower()), None)

    # Check if user exists
    if not user:
        print(f"User: '{args.user}' doesn't exists \nCreate user first.")
        return
    
    # Check if project already exists
    project = next((p for p in user.projects if p.title.lower() == args.title.lower()), None)

    if not project:
        project = Project(args.title, args.description, args.due_date)
        user.assign_project(project)

        print(f"Project: '{args.title}' assigned to '{user.name}'")
        print(user.projects)
        save_db(users)
        return
    
    print(f"Project: '{args.title}' already exists")


# ACTION: list_projects
def list_projects(args):
    users = load_db()


    if not users:
        print("Database is empty!")
        return
    print("Listing all users")
    for user in users:
        print(f"User: [{user.name}]")
        for project in user.projects:
            print(f"    Project: {project.title} | Due: {project.due_date} | '{project.description}'")
            for task in project.tasks:
                print(f"        Task: {task.title} | Status: {'Completed' if task.status else 'Pending'}  |  Assignee: {task.assigned_to}")

# ACTION: add_task
def add_task(args):
    users = load_db()
    
    # Get projects
    projects = []
    for user in users:
        projects.extend(user.projects)

    project = next((p for p in projects if p.title.lower() == args.project.lower()), None)

    # Check if project exists
    if not project:
        print(f"Project: '{args.project}' doesn't exists")
        return
    
    # Check if Task exists
    task_exist = any(t.title.lower() == args.task.lower() for t in project.tasks)
    if not task_exist:
        project.add_task(Task(args.task, user.name))
        print(f"Added Task: '{args.task} to {user.name}: {args.project}")
    
    print(f"Task: '{args.task}' already exists in Project: '{args.project}'")


# ACTION: complete_task
def complete_task(args):
    users = load_db()

    # Get projects
    projects = []
    for user in users:
        projects.extend(user.projects)
    
    # Get project
    project = next((p for p in projects if p.title.lower() == args.project.lower()), None)

    # Check if project exists
    if not project:
        print(f"Project: '{args.project}' doesn't exists")
        return
    
    # Check if Task exists
    task = next(( t for t in project.tasks if t.title.lower() == args.task.lower()), None)

    # Complete task
    if task:
        task.complete_task()
    
    print(f"Task: '{args.task}' doesn't exists in Project: '{args.project}'")
