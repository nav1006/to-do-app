import functionsTODO as fn
import time

now = time.strftime('%b %d %Y, %H:%M:%S')
print('It is: ', now)
while True:
    user_action = input("Enter add, show, edit, remove or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todos = fn.get_todos()
        todo = user_action[4:] + '\n'
        todos.append(todo)
        fn.write_todos(todos_arg=todos)

    elif user_action.startswith('show'):
        todos = fn.get_todos()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            item = item.title()
            print(f'{index + 1}. {item}')

    elif user_action.startswith('edit'):
        try:
            todos = fn.get_todos()
            editNum = int(user_action[5:])
            todos[editNum - 1] = input("Enter new todo: ") + '\n'
            fn.write_todos(todos)

        except ValueError:
            print('Invalid Command')
            continue
        except IndexError:
            print('There is no item with that number.')
            continue

    elif user_action.startswith('remove'):
        try:
            removeNum = int(user_action[7:])
            todos = fn.get_todos()
            todo_to_remove = todos[removeNum - 1].strip('\n')
            todos.pop(removeNum - 1)
            fn.write_todos(todos)
            print(f"Todo {todo_to_remove} was removed from the list.")

        except IndexError:
            print('There is no item with that number.')
            continue
        except ValueError:
            print('Invalid Command')
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Command is not valid!")

print('Bye!')
