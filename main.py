import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    title = input("Enter task: ")
    deadline = input("Enter deadline: ")
    priority = input("Enter priority (High/Medium/Low): ")

    task = {
        "title": title,
        "deadline": deadline,
        "priority": priority,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)

    print("Task added successfully!")


def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    print("\n===== YOUR TASKS =====")

    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"

        print(f"\n{i}. {task['title']}")
        print(f"   Deadline: {task['deadline']}")
        print(f"   Priority: {task['priority']}")
        print(f"   Status: {status}")


def complete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    number = int(input("\nEnter task number to complete: "))

    if 1 <= number <= len(tasks):
        tasks[number - 1]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed!")
    else:
        print("Invalid task number.")


def delete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    number = int(input("\nEnter task number to delete: "))

    if 1 <= number <= len(tasks):
        deleted = tasks.pop(number - 1)
        save_tasks(tasks)
        print(f"Deleted: {deleted['title']}")
    else:
        print("Invalid task number.")


def main():
    tasks = load_tasks()

    while True:
        print("\n===== STUDENT STUDY PLANNER =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            print("Thank you for using Student Study Planner!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()