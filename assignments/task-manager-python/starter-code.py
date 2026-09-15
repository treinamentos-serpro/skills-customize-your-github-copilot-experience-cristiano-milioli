tasks = []


def show_menu():
    print("--- Task Manager ---")
    print("1. Add task")
    print("2. List tasks")
    print("3. Mark task as done")
    print("4. Remove task")
    print("5. Exit")


def add_task():
    # Solicite título da tarefa
    # Adicione a tarefa à lista
    pass


def list_tasks():
    # Mostre todas as tarefas com id, título e status
    pass


def mark_task_done():
    # Solicite o id da tarefa e marque como concluída
    pass


def remove_task():
    # Solicite o id da tarefa e remova da lista
    pass


while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        mark_task_done()
    elif choice == "4":
        remove_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")
