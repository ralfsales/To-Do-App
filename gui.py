import FreeSimpleGUI as sg
import functions
import time

sg.theme("SandyBeach")

clock = sg.Text('', key='clock')

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key='todo')
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 15])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('To-Do List',
                   layout=[[clock],
                        [label],
                        [input_box, add_button],
                        [list_box, edit_button, complete_button],
                        [exit_button]],
                   font=('Helvetica',15))

while True:
    event, values = window.read(timeout=1000)
    window['clock'].update(value=time.strftime("%d,%b,%Y at %H:%M"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + "\n"

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 15))

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 15))

        case "Exit":
            break

        case 'todos':
            try:
                window['todo'].update(value=values['todos'][0])
            except IndexError:
                sg.popup("Your list is empty, try adding a todo first", font=("Helvetica", 15))

        case sg.WIN_CLOSED:
            break

window.close()