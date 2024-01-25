import os

def display_menu():
    print("\nTodo List Menu:")
    print("1. View tasks")
    print("2. Add task")
    print("3. Update task")
    print("4. Delete task")
    print("5. Exit")

def view_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks found.")
            else:
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks found. Create a new task to get started.")

def add_task():
    task = input("Enter the task: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully!")

def update_task():
    view_tasks()
    try:
        task_number = int(input("Enter the task number to update: "))
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if 1 <= task_number <= len(tasks):
                new_task = input("Enter the updated task: ")
                tasks[task_number - 1] = new_task + "\n"
                with open("tasks.txt", "w") as file:
                    file.writelines(tasks)
                print("Task updated successfully!")
            else:
                print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_task():
    view_tasks()
    try:
        task_number = int(input("Enter the task number to delete: "))
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if 1 <= task_number <= len(tasks):
                del tasks[task_number - 1]
                with open("tasks.txt", "w") as file:
                    file.writelines(tasks)
                print("Task deleted successfully!")
            else:
                print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting the Todo List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    if not os.path.isfile("tasks.txt"):
        with open("tasks.txt", "w"):
            pass  # Create an empty file if it doesn't exist

    main()
