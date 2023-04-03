def print_menu(choices):
    for i, choice in enumerate(choices):
        print(i, choice)

def menu(choices):
    print_menu(choices)
    choice = int(input("Enter your choice: "))
    return choice-1

# dictionary of choices with the function to call as value
def menu_functions(choices, **kwargs):
    print_menu(list(choices.keys()))
    choice = int(input("Enter your choice: "))
    return list(choices.values())[choice-1](kwargs)