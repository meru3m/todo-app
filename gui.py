from modules import functions
import FreeSimpleGUI as sg 

# Create the elements that go inside the window
label = sg.Text("Type in a to-do")  # Create a text label
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")  # Create an "Add" button
list_box = sg.Listbox(values=functions.get_todos(), key='todos', enable_events = True, size=[45,10])
edit_button = sg.Button("Edit")

# Define the layout of the window
layout = [[label], [input_box, add_button], [list_box, edit_button]]  # Arrange the elements in the window

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
        window['todos'].update(values=todos)
        
    elif event == "Edit":
        todo_to_edit = values['todos'][0]  # Get the first selected item from the Listbox
        new_todo =values['todo'] + "\n"

        todos = functions.get_todos()
        index = todos.index(todo_to_edit)
        todos[index] = new_todo
        functions.write_todos(todos)
        window['todos'].update(values=todos)
        
    elif event == "todos":
        #values here is the dictionary, values=['todos] ('todos' is the key) will return the list (value = selected todo in the list) index 0 is the index of the only item(string) in the list
        window['todo'].update(value=values['todos'][0])
        
    elif event == sg.WIN_CLOSED:
        break
        

# Close the window when done
window.close()
