import laws as l
import menu
import database
import tokens

db = database.Database('localhost', tokens.user, tokens.password, 'laws')

def add_section(laws):
    title = input("Enter the title of the section: ")
    laws.add_section(laws.Section(title))

def add_article(laws):
    title = input("Enter the title of the article: ")
    laws.add_article(laws.Article(title))

def add_alinea(laws):
    text = input("Enter the text of the alinea: ")
    laws.add_alinea(laws.Alinea(text))
    
laws = l.load(db)

def save():
    l.save(laws, db)

def exit1():
    save()
    exit(0)

current = laws
previous = None

while True:
    choices = [thing.title for thing in current]
    if(hasattr(current, 'parent')):
        choices.append("Return")
    choices.append('Print')

    index, name = menu.menu(choices)
    while index > len(choices) or index < 0:
        print("Invalid choice")
        index = menu.menu(choices)
    
    if name == "Return":
        current = current.parent
    elif name == "Print":
        if type(current) == list:
            for law in current:
                print("\n"+str(law))
        else:
            print("\n"+str(current))
    elif type(current) == list:
        current = laws[index]
    elif type(current) == l.Law:
        current = current.sections[index]
    elif type(current) == l.Section:
        current = current.articles[index]
    elif type(current) == l.Article:
        print("\n"+(current.alineas[index]).format()+"\n")