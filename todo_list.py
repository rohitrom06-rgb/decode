

tasks = []
next_id = 1  # simple auto-incrementing id



def input_new_task():
    """Collects a new task title from the user (raw input capture)."""
    title = input("Enter task description: ").strip()
    return title


def input_task_id(prompt="Enter task ID: "):
    """Collects a task ID from the user, validated as an integer."""
    raw = input(prompt).strip()
    try:
        return int(raw)
    except ValueError:
        return None



def add_task(title):
    """Appends a new task to the volatile container. O(1) amortized."""
    global next_id
    if not title:
        print(" -> Task description cannot be empty.\n")
        return
    tasks.append({"id": next_id, "title": title, "done": False})
    print(f" -> Task #{next_id} added.\n")
    next_id += 1


def complete_task(task_id):
    """Marks a task as done by scanning the list for a matching id. O(n)."""
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            print(f" -> Task #{task_id} marked complete.\n")
            return
    print(f" -> No task found with ID {task_id}.\n")


def delete_task(task_id):
    """Removes a task from the list. O(n), since remaining elements shift."""
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print(f" -> Task #{task_id} deleted.\n")
            return
    print(f" -> No task found with ID {task_id}.\n")



def display_tasks():
    """Renders the current state of the volatile container to the user."""
    print("\n----- DecodeLabs To-Do List -----")
    if not tasks:
        print(" (empty)")
    for task in tasks:
        status = "[x]" if task["done"] else "[ ]"
        print(f" {status} #{task['id']}: {task['title']}")
    print("----------------------------------\n")


def display_menu():
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")



def main():
    while True:
        display_menu()                          # OUTPUT
        choice = input("Choose an option: ").strip()  # INPUT

        if choice == "1":
            title = input_new_task()             # INPUT
            add_task(title)                      # PROCESS
        elif choice == "2":
            display_tasks()                      # OUTPUT
        elif choice == "3":
            task_id = input_task_id()            # INPUT
            if task_id is not None:
                complete_task(task_id)           # PROCESS
        elif choice == "4":
            task_id = input_task_id("Enter ID of task to delete: ")  # INPUT
            if task_id is not None:
                delete_task(task_id)             # PROCESS
        elif choice == "5":
            print("Exiting DecodeLabs To-Do List. Goodbye!")
            break
        else:
            print(" -> Invalid option, try again.\n")


if __name__ == "__main__":
    main()
