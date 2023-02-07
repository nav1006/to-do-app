FILEPATH = 'todoStore.txt'

def get_todos(filepath=FILEPATH):
    """
    Read the text file and returns the list of items in it.
    :param filepath: path of the text file
    :return: list of items in it
    """
    with open(filepath, 'r') as file_def:
        todos_def = file_def.readlines()
    return todos_def


def write_todos(todos_arg, filepath=FILEPATH):
    """
    Write the todos items list in the text file
    :param todos_arg: todos item list
    :param filepath:path of text file
    :return: does not return anything
    """
    with open(filepath, 'w') as file_def:
        file_def.writelines(todos_arg)
    # this doesnt require any return statement