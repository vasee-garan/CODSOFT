tasks = []

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully.")

def view_task():
    if len(tasks) == 0:
        print("No tasks.")
    else:
        print("List of tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def delete_task():
    if len(tasks) == 0:
        print("No tasks to delete.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        choice = int(input("Enter the task number to delete: "))
        if 1 <= choice <= len(tasks):
            del tasks[choice - 1]
            print("Task deleted.")
        else:
            print("Invalid task number.")

def main():
    while True:
        print("\nTO-DO List")
        print("1. Create task")
        print("2. Display tasks")
        print("3. Delete task")
        print("4. Quit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_task()
        elif choice == 2:
            view_task()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()