import FreeSimpleGUI as sg
import functions

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos("todos.txt"), key='todos',
                      enable_events=True, size=[30, 8])
edit_button = sg.Button("Edit")

window = sg.Window('To-Do List',
                   layout=[[label], [input_box, add_button],[list_box,edit_button]],
                   font=('Helvetica',20))

while True:
    event, values = window.read()

    match event:
        case "Add":
            todos = functions.get_todos("todos.txt")
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos("todos.txt",todos)
            window['todos'].update(values=todos)

        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos("todos.txt")
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos("todos.txt",todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break

window.close()