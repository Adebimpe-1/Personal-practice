tasks = []

def load_tasks():
    try:
        with open('tasks.txt', 'r') as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass

def save_tasks():
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def add_task(task):
    tasks.append(task)

def list_tasks():
    if not tasks:
        print("No tasks.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def main():
    load_tasks()
    while True:
        choice = input(f"What would you like to do? 1.Add task 2.View tasks 3.Exit: ")
        if choice == '1':
            task = input("Enter task: ")
            add_task(task)
            save_tasks()
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            break
        else:
            print("Invalid choice")

main()
