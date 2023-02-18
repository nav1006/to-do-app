import functionsTODO as fn
import PySimpleGUI as gui

label = gui.Text('Type in a to-do')
input_box = gui.InputText(tooltip='Enter TO-DO')
add_button = gui.Button('Add')
window = gui.Window('My TODO App', layout = [[label], [input_box, add_button]])
window.read()
window.close()
