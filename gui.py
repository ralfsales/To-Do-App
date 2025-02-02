import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window('To-Do List', layout=[[label], [input_box, add_button]])
window.read()
window.close()

print("That is all")