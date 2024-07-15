from modules import functions
import FreeSimpleGUI as sg 

# Create the elements that go inside the window
label = sg.Text("Type in a to-do")  # Create a text label
input_box = sg.InputText(tooltip="Enter todo", key="todo")  # Create a text box with a tooltip
add_button = sg.Button("Add")  # Create an "Add" button

# Define the layout of the window
layout = [[label], [input_box, add_button]]  # Arrange the elements in the window

# Create the window with a title and the defined layout
window = sg.Window("My To-Do App", layout, font=('Montserrat'))

# Display the window and keep it open until the user interacts with it
# window.read() in FreeSimpleGUI always return a tuple with exactly two values: event and values

while True:
    event, values = window.read()
    print(event) #add_button
    print(values) #dictionary of inputs (key value pairs of inputs)
    
    if event == "Add":
        todos = functions.get_todos()
        new_todo = values['todo'] + "\n"
        todos.append(new_todo)
        functions.write_todos(todos)
    elif event == sg.WIN_CLOSED:
        break
        

# Close the window when done
window.close()
