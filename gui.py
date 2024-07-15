import FreeSimpleGUI as sg 

# Create the elements that go inside the window
label = sg.Text("Type in a to-do")  # Create a text label
input_box = sg.InputText(tooltip="Enter todo")  # Create a text box with a tooltip
add_button = sg.Button("Add")  # Create an "Add" button

# Define the layout of the window
layout = [[label], [input_box, add_button]]  # Arrange the elements in the window

# Create the window with a title and the defined layout
window = sg.Window("My To-Do App", layout)

# Display the window and keep it open until the user interacts with it
window.read()

# Close the window when done
window.close()
