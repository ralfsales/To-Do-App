import functions
import time

now = time.strftime("%d/%b/%Y at %H:%M")
print("Hey there, It is",now)

while True:
    user_action = input("Type add, show, edit, remove or exit: ").strip().lower()

    if user_action.startswith('add'):
        todo = user_action[4:]
        todos = functions.get_todos('todos.txt')
        todos.append(todo + "\n")
        functions.write_todos('todos.txt', todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos('todos.txt')

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            todos = functions.get_todos('todos.txt')
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'
            print("todo edited...", new_todo)
            functions.write_todos('todos.txt', todos)
        except (ValueError, IndexError):
            print("Your command is not valid")
            continue

    elif user_action.startswith('remove'):
        try:
            number = int(user_action[6:])
            todos = functions.get_todos('todos.txt')
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            print(f"{todo_to_remove} was removed from the list.")
            todos.pop(index)
            functions.write_todos('todos.txt', todos)
        except (ValueError, IndexError):
            print("Your command is not valid")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("This command is invalid.")

    print(" ")

print("Bye! See you next time")