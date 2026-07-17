from models import User, Project, Task
from .storage import save_db, load_db

from rich.console import Console
from rich.table import Table

console = Console()
table = Table()

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

        console.print(f" ✔ Created User: {args.name}", style="green")
        return
    console.print(f"➖ User: {args.name} ({args.email}) already exists.", style="orange")

# ACTION: list_users
def list_users(args):
    users = load_db()
    if not users:
        console.print("Database is empty!", style="red")
        return

    # Create table
    table = Table(title="Users")
    table.add_column("ID", justify="center", style="cyan", no_wrap=True)
    table.add_column("Name", style="magenta")
    table.add_column("Email", justify="center", style="green")
    
    for user in users:
        table.add_row(str(user.id), user.name, user.email)
    console.print(table)

# ACTION: add_project
def add_project(args):
    users = load_db()
    # Get user from users
    user = next((u for u in users if u.name.lower() == args.user.lower()), None)

    # Check if user exists
    if not user:
        console.print(f"❌ User: '{args.user}' doesn't exists \nCreate user first.", style="red")
        return
    
    # Check if project already exists
    project = next((p for p in user.projects if p.title.lower() == args.title.lower()), None)

    if not project:
        project = Project(args.title, args.description, args.due_date)
        user.assign_project(project)

        console.print(f" ✔  Project: '{args.title}' assigned to '{user.name}'", style="green")
        save_db(users)
        return
    
    console.print(f" ❌ Project: '{args.title}' already exists", style="orange")


# ACTION: list_projects
def list_projects(args):
    users = load_db()


    if not users:
        console.print(" ❌ Database is empty!", style="red")
        return
    
    # Create table
    table = Table(title="Projects")
    table.add_column("Project Title", style="cyan")
    table.add_column("Description", style="magenta")
    table.add_column("Due Date", justify="center", style="green")
    table.add_column("Tasks", justify="center", style="yellow")
    
    console.print("Listing all users", style="blue")
    for user in users:
        print(f"User: [{user.name}] Projects:")
        for project in user.projects:
            
            tasks = [f" {index}. {task.title} | Status: {'Completed' if task.status else 'Pending'}  |  Assigned_to: {task.assigned_to}" for index, task in enumerate(project.tasks, start=1)]

            table.add_row(project.title.upper(), project.description, project.due_date, tasks[0] if tasks else "No tasks")

            console.print(table)


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
        console.print(f"❌ Project: [{args.project}] doesn't exists", style="red")
        return
    
    # Check if Task exists
    task_exist = any(t.title.lower() == args.task.lower() for t in project.tasks)
    if not task_exist:
        project.add_task(Task(args.task, user.name))
        console.print(f" ✔ Added Task: [{args.task}] to [{user.name}: {args.project}]", style="green")
        save_db(users)
    
    console.print(f" ➖ Task: [{args.task}] already exists in Project: [{args.project}]", style="orange")


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
        console.print(f"❌ Project: [{args.project}] doesn't exists", style="red")
        return
    
    # Check if Task exists
    task = next(( t for t in project.tasks if t.title.lower() == args.task.lower()), None)

    # Complete task
    if task:
        if task.status:
            console.print(f"➖ Task: [{args.task}] is already completed", style="orange")
            return
        task.complete_task()
        save_db(users)
        console.print(f"✔ Task: '{task.title}' marked complete", style="green")
        return
    
    console.print(f"❌ Task: [{args.task}] doesn't exists in Project: [{args.project}]", style="red")
