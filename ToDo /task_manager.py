import json

tasks = {}

def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_tasks():
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f)

def edit_task():
    task_name = input("Enter the name of the task to edit: ")
    if task_name in tasks:
        new_task_name = input("Enter the new name of the task: ")
        tasks[new_task_name] = tasks.pop(task_name)
        print(f"Task '{task_name}' has been renamed to '{new_task_name}'.")
        status = input(f"Mark task '{new_task_name}' as completed? (y/n): ")
        if status.lower() == 'y':
            tasks[new_task_name] = True
            print(f"Task '{new_task_name}' has been marked as completed.")
    else:
        print(f"Task '{task_name}' was not found in the to-do list.")

tasks = load_tasks()

while True:
    action = input("Would you like to add, edit, remove, complete, or uncomplete a task? Type 'list', 'save', or 'quit' to exit: ")
    
    if action == "add":
        task_name = input("Enter the name of the task: ")
        tasks[task_name] = False
        print(f"Task '{task_name}' has been added to the to-do list.")
    elif action == "edit":
        edit_task()
    elif action == "remove":
        task_name = input("Enter the name of the task to remove: ")
        if task_name in tasks:
            del tasks[task_name]
            print(f"Task '{task_name}' has been removed from the to-do list.")
        else:
            print(f"Task '{task_name}' was not found in the to-do list.")
    elif action == "complete":
        task_name = input("Enter the name of the task to complete: ")
        if task_name in tasks:
            tasks[task_name] = True
            print(f"Task '{task_name}' has been marked as completed.")
        else:
            print(f"Task '{task_name}' was not found in the to-do list.")
    elif action == "uncomplete":
        task_name = input("Enter the name of the task to uncomplete: ")
        if task_name in tasks:
            tasks[task_name] = False
            print(f"Task '{task_name}' has been marked as not completed.")
        else:
            print(f"Task '{task_name}' was not found in the to-do list.")
    elif action == "list":
        print("Current to-do list:")
        for task_name, completed in tasks.items():
            status = "completed" if completed else "not completed"
            print(f"- {task_name} ({status})")
    elif action == "save":
        save_tasks()
        print("To-do list saved to file.")
    elif action == "quit":
        save_tasks()
        break
    else:
        print("Invalid action. Please type 'add', 'edit', 'remove', 'complete', 'uncomplete', 'list', 'save', or 'quit'.")
