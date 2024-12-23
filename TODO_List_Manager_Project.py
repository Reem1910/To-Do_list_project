tasks = []

def display_menu():
    print("/n TO DO LIST MANAGER")
    print("1.Add Task")
    print("2.View Tasks")
    print("3.Update Task")
    print("4.Delete Task")
    print("5.Exit")

def add_task():
    task = input("Add Task :")
    tasks.append({"name":task,"completed":False})
    print("Task was added successfully!")

def view_tasks():
    if not tasks:
        print("there is not any tasks!")
    else:
        for i, task in enumerate(tasks):
            status = "✓" if task["completed"] else "✗"
            print (f"{i+1}.{task["name"]}[{status}]")

def update_task():
    view_tasks()
    try:
        task_number = int(input("Choose the task's number for update :"))
        if 0 <= task_number < len(tasks):
            tasks[task_number]["completed"] = not tasks[task_number]["completed"]
            print("The Task Was Updated Successfully!")
        else:
            print("Invalid number!")
    except ValueError :
        print("Please enter a valid number!")

def delete_task():
    view_tasks()
    try:
        task_number = int(input("Choose the task's number to delete : ")) -1
        if 0 <= task_number < len(tasks) :
            tasks.pop(task_number)
            print("The task was deleted!")
        else:
            print("Invalid number!")
    except ValueError :
        print("Please enter a valid number!")

#project implementation:

while True:
    display_menu()
    choice = input("Choose the task's no : ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Good Bye!")
        break
    else:
        print("wrong choice")
