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

while True:
    choices = {
        "Save": save,
        "Exit": exit1
    }
    choices2 = [thing.title for thing in current]
    index = menu.menu(choices2)
    while index >= len(choices) or index < 0:
        print("Invalid choice")
        index = menu.menu(choices2)
    
    if type(current) == list:
        current = laws[index]
    elif type(current) == l.Law:
        current = current.sections[index]
    elif type(current) == l.Section:
        current = current.articles[index]
    elif type(current) == l.Article:
        current = current.alineas[index]