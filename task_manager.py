
import os

# File to store the tasks

FILE_NAME = "tasks.txt"

#load tasks from file
def load_tasks():
    tasks ={}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                task_id, title, status = line.strip().split(" | ")
                tasks[int(task_id)] = {"title": title, "status": status}
    return tasks

# save tasks
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task_id, task in tasks.items():
            file.write(f"{task_id} | {task['title']} | {task['status']}\n")

#Add a new task
def add_task(tasks):
    title = input("Enter task title: ")
    task_id = max(tasks.keys(), default=0) + 1
    tasks[task_id] = {"title": title, "status": "incomplete"}
    print(f"Task '{title}' added.")

# view all taks
def view_tasks(tasks):
    if not tasks:
        print("No task available")
    else:
        for task_id, task in tasks.items():
            print(f"[{task_id}] {task['title']} - {task['status']}")

#Mark task as complete

def mark_task_complete(tasks):
    task_id = int(input("Enter task ID to mark as complete: "))
    if task_id in tasks:
        tasks[task_id]["status"] = "complete"
        print(f"Task '{tasks[task_id]['title']} marked as complete.")
    else:
        print("Task ID not found.")

# Delete a task

def delete_task(tasks):
    task_id = int(input("Enter task ID to delete: "))
    if task_id in tasks:
        delete_task = tasks.pop(task_id)
        print(f"Task '{delete_task['title']} deleted.")
    else:
        print("Task ID not found.")