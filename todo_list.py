todo_list = []

def show_menu():
    print("\nTodo List Menu:")
    print("1. View Todo List")
    print("2. Add Todo Item")
    print("3. Remove Todo Item")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    #Check for Choice one
    if choice == "1":
        print("\nTodo List:")
        if todo_list:
            for idx, item in enumerate(todo_list, start=1):
                print(f"{idx}. {item}")
        else:
            print("----------Todo list is empty.----------")

    #Check for Choice Two
    elif choice == "2":
        item = input("Enter the todo item to add: ")
        todo_list.append(item)
        print(f"'{item}' has been added to the todo list.")
    #Check for Choice Three
    elif choice == "3":
        if not todo_list:
            print("----------Todo list is empty.----------")
        else:
            print("\nYour Todo List:")
            for idx, item in enumerate(todo_list, start=1):
                print(f"{idx}. {item}")
            try:
                item_number = int(input("Enter the task number to remove: "))
                if 1 <= item_number <= len(todo_list):
                    removed_item = todo_list.pop(item_number - 1)
                    print(f"'{removed_item}' has been removed from the todo list.")
                else:
                    print("Invalid task number")
            except ValueError:
                    print("Invalid input. Please enter a valid number.")
        
    #Check for  Choice For
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
  