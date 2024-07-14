import modules
import FreeSimpleGUI as sg


label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")
layout = [[label], [input_box, add_button]]  # Define what will go inside the window (nothing for now)

# Window: Think of this as creating a blank canvas where you can put things like buttons, text boxes, etc.
window = sg.Window("My To-Do App", layout)  # Create the window with a title

window.read()  # Show the window and keep it open

window.close()  # Close the window when done
