tasks = []  # Store tasks while the program runs.

while True:  # Keep showing the menu until the user exits.
    choice = input("\n1. Add task  2. View tasks  3. Exit: ")

    if choice == "1":
        task = input("Enter a task: ")  # Ask for a new task.
        tasks.append(task)  # Add it to the list.
    elif choice == "2":
        for number, task in enumerate(tasks, start=1):
            print(f"{number}. {task}")  # Show each task with a number.
    elif choice == "3":
        break  # Exit the program.
    else:
        print("Please choose 1, 2, or 3.")
