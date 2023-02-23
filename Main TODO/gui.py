import functionsTODO as fn
import PySimpleGUI as gui
import time

gui.theme('BluePurple')
cloak = gui.Text('', key='cloak')
label = gui.Text('Type in a to-do')
input_box = gui.InputText(tooltip='Enter TO-DO', key='todo')
add_button = gui.Button('Add')
list_box = gui.Listbox(values=fn.get_todos(), key='todos',
                       enable_events=True, size=[45,10])
edit_button = gui.Button('Edit')
complete_button = gui.Button('Complete')
exit_button = gui.Button('Exit')
window = gui.Window('My TODO App',
                    layout = [[cloak],
                              [label],
                              [input_box, add_button],
                              [list_box, edit_button, complete_button],
                              [exit_button]],
                    font=('Helvetica',20))

while True:
    event, values = window.read(timeout=200)
    window['cloak'].update(value=time.strftime('%b %d %Y, %H:%M:%S'))

    match event:
        case 'Add':
            todos = fn.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            fn.write_todos(todos)
            window['todos'].update(values=todos)

        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + '\n'
                todos = fn.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                fn.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                gui.popup('Select Item', 'Please select a to-do first.', font=('Helvetica',20))

        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = fn.get_todos()
                todos.remove(todo_to_complete)
                fn.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                gui.popup('Select Item', 'Please select a to-do first.', font=('Helvetica', 20))

        case 'Exit':
            break

        case 'todos':
            window['todo'].update(value= values['todos'][0])

        case gui.WIN_CLOSED:
            break

window.close()
