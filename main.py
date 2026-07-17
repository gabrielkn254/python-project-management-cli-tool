import argparse

from utils.command_actions import add_user, list_users, add_project, list_projects, add_task, complete_task


def main():
    parser = argparse.ArgumentParser(description="Project Management CLI Tool")
    subparsers = parser.add_subparsers()

    # command: add-user
    add_user_parser = subparsers.add_parser("add-user", help="Create a new user")
    add_user_parser.add_argument("--name", required=True, help="User's name")
    add_user_parser.add_argument("--email", required=True, help="User's email")
    add_user_parser.set_defaults(func=add_user)

    # command: list-users
    list_users_parser = subparsers.add_parser("list-users", help="List all users and their assigned projects")
    list_users_parser.set_defaults(func=list_users)

    # command: add-project
    add_project_parser = subparsers.add_parser("add-project", help="Assign a project to a user")
    add_project_parser.add_argument("--user", required=True, help="User's name assign a project")    
    add_project_parser.add_argument("--title", required=True, help="Project title")
    add_project_parser.add_argument("--description", required=True, help="Project description")
    add_project_parser.add_argument("--due_date", required=False, help="Project due date")
    add_project_parser.set_defaults(func=add_project)

    # command: list-projects
    list_projects_parser = subparsers.add_parser("list-projects", help="List all projects for all or assigned to specific user")
    list_projects_parser.set_defaults(func=list_projects)

    # command: add-task
    add_task_parser = subparsers.add_parser("add-task", help="Add tasks to a specific project")
    add_task_parser.add_argument("--project", required=True, help="Project title to assign a task")
    add_task_parser.add_argument("--task", required=True, help="Task name/title")
    add_task_parser.set_defaults(func=add_task)

    # command: complete-task
    complete_task_parser = subparsers.add_parser("complete-task", help="Update task status to complete")
    complete_task_parser.add_argument("--project", required=True, help="Project title that contains the task")
    complete_task_parser.add_argument("--task", required=True, help="Task title to update status")
    complete_task_parser.set_defaults(func=complete_task)

    # Create args object
    args = parser.parse_args()

    # Handle error with help
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()