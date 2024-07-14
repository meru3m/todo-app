from modules import functions
import time


now = time.strftime("%b %d, %Y %H:%M:%S")
print("The time is below")
print('It is', now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    if user_action.startswith('add'):
        todo = user_action[4:]
        
        todos = functions.get_todos()

        todos.append(todo + '\n') #placed before reopening the file for writing to ensure that the new todo item is added to the list of todos before the list is written back to the file.
        
        functions.write_todos(todos)
        
    elif user_action.startswith('show'):
        todos = functions.get_todos()
            
        # new_todos = [item.strip("\n") for item in todos]
        
        for index, item in enumerate(todos): #enumerate gets both index and item of a list.
            item = item.strip("\n")
            row = f"{index + 1}-{item}"
            print(row)
            
    elif user_action.startswith('edit'):
        try:    
            number = int(user_action[5:]) - 1
            
            todos = functions.get_todos()
            
            new_todo = input(f'Enter a new todo: ')
            todos[number] = new_todo + '\n'
            
            functions.write_todos(todos)
            
        except ValueError:
            print('Your command is not valid!')   
            continue 

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            
            todos = functions.get_todos()
                
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            
            functions.write_todos(todos) 
                
            message = f"Todo '{todo_to_remove.upper()}' is completed."
            print(message)
        except IndexError:
            print('Item not found')
            continue
        except ValueError:
            print('Command is not valid!')
            continue
        
    elif user_action.startswith('exit'):
        break
    
    else:
        print("Command is not valid")

print("Bye!")