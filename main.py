import laws
import menu

def exit(laws):
    laws.save(laws)
    quit()

def add_section(laws):
    title = input("Enter the title of the section: ")
    laws.add_section(laws.Section(title))

def add_article(laws):
    title = input("Enter the title of the article: ")
    laws.add_article(laws.Article(title))

def add_alinea(laws):
    text = input("Enter the text of the alinea: ")
    laws.add_alinea(laws.Alinea(text))
    
laws = laws.load()

current = None

while True:
    choices = {
        "Save": laws.save,
        "Exit": exit
    }
        choices = [thing.title for thing in current]
    index = menu.menu(choices)
    while index > len(choices) or index <= 0:
        print("Invalid choice")
        index = menu.menu(choices)
    
    
    if type(current) == laws.Law:
        choices["Add section"] = add_section
    elif type(current) == laws.Section:
        choices["Add article"] = add_article
    elif type(current) == laws.Article:
        choices["Add alinea"] = add_alinea
    menu.menu_functions(choices, laws=laws)
