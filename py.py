import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from a JSON file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save tasks to a JSON file."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(task):
    """Add a new task."""
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print(f"Task added: {task}")

def list_tasks():
    """List all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found!")
    else:
        for idx, task in enumerate(tasks, start=1):
            status = "[✔]" if task["done"] else "[ ]"
            print(f"{idx}. {status} {task['task']}")

def complete_task(task_number):
    """Mark a task as complete."""
    tasks = load_tasks()
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        save_tasks(tasks)
        print("Task marked as complete!")
    else:
        print("Invalid task number!")

def delete_task(task_number):
    """Delete a task."""
    tasks = load_tasks()
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"Deleted task: {removed_task['task']}")
    else:
        print("Invalid task number!")

if __name__ == "__main__":
    while True:
        print("\nTo-Do List CLI")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter task description: ")
            add_task(task)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            list_tasks()
            task_num = int(input("Enter task number to complete: "))
            complete_task(task_num)
        elif choice == "4":
            list_tasks()
            task_num = int(input("Enter task number to delete: "))
            delete_task(task_num)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again!")
