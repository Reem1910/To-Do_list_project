import json
import os

# File to store tasks
TASKS_FILE = "tasks.json"

# Load tasks from the file if it exists
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks to the file
def save_tasks():
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Initialize tasks (load from file at startup)
tasks = load_tasks()

def display_menu():
    print("\n📋 TO DO LIST MANAGER")
    print("1️⃣  Add Task")
    print("2️⃣  View Tasks")
    print("3️⃣  Update Task")
    print("4️⃣  Delete Task")
    print("5️⃣  Exit")

def add_task():
    task = input("📝 Add Task: ")
    tasks.append({"name": task, "completed": False})
    save_tasks()
    print("✅ Task added successfully!")

def view_tasks():
    if not tasks:
        print("⚠️ No tasks available!")
    else:
        print("\n📌 Task List:")
        for i, task in enumerate(tasks):
            status = "✅" if task["completed"] else "❌"
            print(f"{i+1}. {task['name']} [{status}]")

def update_task():
    view_tasks()
    try:
        task_number = int(input("🔄 Choose task number to update: ")) - 1
        if 0 <= task_number < len(tasks):
            tasks[task_number]["completed"] = not tasks[task_number]["completed"]
            save_tasks()
            print("✅ Task updated successfully!")
        else:
            print("❌ Invalid number!")
    except ValueError:
        print("⚠️ Please enter a valid number!")

def delete_task():
    view_tasks()
    try:
        task_number = int(input("🗑️ Choose task number to delete: ")) - 1
        if 0 <= task_number < len(tasks):
            tasks.pop(task_number)
            save_tasks()
            print("🗑️ Task deleted successfully!")
        else:
            print("❌ Invalid number!")
    except ValueError:
        print("⚠️ Please enter a valid number!")

# Run the To-Do List Manager
while True:
    display_menu()
    choice = input("🔢 Choose an option: ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("👋 Goodbye!")
        break
    else:
        print("⚠️ Invalid choice, please try again!")
