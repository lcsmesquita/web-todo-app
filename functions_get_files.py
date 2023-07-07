FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH): 
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print(get_todos())

# this if __name__ == "__main__" is used to refer directly to the file that is written
# in this example, we used it so we can get that print only when we are executing directly the program
# that has this function. As you know, this program here is imported in another one, what makes all this code
# run in the other program, so, we used the if name main so this part of the code can only be executed with we run
# THIS application  only.