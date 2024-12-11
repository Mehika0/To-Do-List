def display_menu():
    print("\n=== To-Do List Manager ===")
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Mark a Task as Done")
    print("4. Delete a Task")
    print("5. Exit")
    print("==========================")

def view_todo_list(todo_list):
    if not todo_list:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            status = "[✓]" if task['done'] else "[ ]"
            print(f"{index}. {status} {task['task']}")

def add_task(todo_list):
    task = input("\nEnter the task: ")
    todo_list.append({'task': task, 'done': False})
    print(f"Task '{task}' added successfully!")

def mark_task_done(todo_list):
    view_todo_list(todo_list)
    if todo_list:
        try:
            task_num = int(input("\nEnter the task number to mark as done: ")) - 1
            if 0 <= task_num < len(todo_list):
                todo_list[task_num]['done'] = True
                print(f"Task '{todo_list[task_num]['task']}' marked as done!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

def delete_task(todo_list):
    view_todo_list(todo_list)
    if todo_list:
        try:
            task_num = int(input("\nEnter the task number to delete: ")) - 1
            if 0 <= task_num < len(todo_list):
                removed_task = todo_list.pop(task_num)
                print(f"Task '{removed_task['task']}' deleted successfully!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

def main():
    todo_list = []
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")
        if choice == '1':
            view_todo_list(todo_list)
        elif choice == '2':
            add_task(todo_list)
        elif choice == '3':
            mark_task_done(todo_list)
        elif choice == '4':
            delete_task(todo_list)
        elif choice == '5':
            print("\nThank you for using the To-Do List Manager. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
