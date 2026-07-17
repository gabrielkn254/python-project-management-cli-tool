# Summative Lab: Python Project Management CLI Tool
This a python-based cli tool that helps administrators to managed to managed users, projects and tasks through structured CLI commands.

## Features
1. Creating and listing users via the command line.
2. Adding projects to specific users and displaying their associated projects.
3. Assigning tasks to projects and marking them as complete.
4. Editing and persisting project/task data using file I/O.
5. Navigating the tool with clear, user-friendly CLI commands.
6. Managing data relationships like one-to-many (users to projects) and many-to-many (projects to tasks with contributors).
7. Create and manage users, projects, and tasks.

## Capabilities
1. Admins can manage users and projects.
2. Each user can have one or more projects.
3. Each project can have one or more tasks.
4. User id auto-generation

## Technologies Used

### Languages:
- Python & it's built in packages

### Package Manager
- Pipenv: Both managing packages and virtual env.

### External dependacies
- Rich: To format cli outputs
- Pytest --dev: To test command action functions

### Workflow
- Git: Code workflow managing tool
- Github: Store remote repo

## Getting Started
To run this program you will need to fork this repo, and install on your local machine.

### Installation
1. Fork & clone this repo
```bash
git clone https://github.com/gabrielkn254/python-project-management-cli-tool
```
2. Navigate to the cloned repo
```bash
cd python-project-management-cli-tool
```
3. Install dependacies
```bash
pipenv install
```
4. Run CLI entry
```bash
python main.py
```

### Command Actions
1. List users
```bash
python main.py list-users
```
2. Add user
```bash
python main.py add-user --name Grace --email grace@gmail.com
```
3. Add a project to a user
```bash
python main.py add-project --user Grace --title "News analyzer" --description "A tool to assess articles" --due-date "19-07-2026"
```
4. Add a task to a project
```bash
python main.py add-task --project "News analyzer" --task "set up remote repo"
```
5. List all projects
```bash
python main.py list-projects
```
6. Mark a task as complete
```bash
python main.py complete-task --project "News analyzer" --task "set up remote repo"
```

## License
This project is licensed under the MIT License.