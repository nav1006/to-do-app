import functionsTODO as fn
import PySimpleGUI as gui

label = gui.Text('Type in a to-do')
input_box = gui.InputText(tooltip='Enter TO-DO', key='todo')
add_button = gui.Button('Add')
window = gui.Window('My TODO App', layout = [[label], [input_box, add_button]],
                    font=('Helvetica',20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = fn.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            fn.write_todos(todos)

        case gui.WIN_CLOSED:
            break

window.close()
