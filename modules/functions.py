FILEPATH = 'todos.txt'

def get_todos(filepath=FILEPATH):
    """Read a text file and return the list of to-do items"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()  #reads all the lines from the file and stores them as a list of strings in the variable todos_local.
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """Write the to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
        
        
""" 
-This block of code will only execute if the script is run directly.
-It prevents certain code from being executed when the module is imported.        
-If the script is executed directly (e.g., by running python script_name.py from the command line), __name__ will be "__main__", and the code inside this block will execute.
-If the script is imported as a module in another script, the code inside this block will not execute.
"""
if __name__ == "__main__":
    print(get_todos())
    
