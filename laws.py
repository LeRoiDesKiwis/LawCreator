import database

def load(db):
    # load the laws from the database
    laws = []
    for law in db.query("SELECT * FROM Laws"):
        law_id = law[0]
        law_title = law[1]
        sections = []
        for section in db.query("SELECT * FROM Section WHERE LawID = %s", (law_id,)):
            section_id = section[0]
            section_title = section[2]
            articles = []
            for article in db.query("SELECT * FROM Article WHERE SectionID = %s", (section_id,)):
                article_id = article[0]
                article_title = article[2]
                alineas = []
                for alinea in db.query("SELECT * FROM Alinea WHERE ArticleID = %s", (article_id,)):
                    alinea_id = alinea[0]
                    alinea_text = alinea[2]
                    alineas.append(Alinea(alinea_text))
                articles.append(Article(article_title, alineas))
            sections.append(Section(section_title, articles))
        laws.append(Law(law_title, sections))
    return laws

def save(laws, db):
    #use "ON DUPLICATE KEY UPDATE" to update or save the laws in the database
    for law in laws:
        law_id = db.query("INSERT INTO laws (Title) VALUES (%s) ON DUPLICATE KEY UPDATE Title = %s", (law.title, law.title)).lastrowid
        for section in law.sections:
            section_id = db.query("INSERT INTO sections (LawID, Title) VALUES (%s, %s) ON DUPLICATE KEY UPDATE Title = %s", (law_id, section.title, section.title)).lastrowid
            for article in section.articles:
                article_id = db.query("INSERT INTO articles (SectionID, Title) VALUES (%s, %s) ON DUPLICATE KEY UPDATE Title = %s", (section_id, article.title, article.title)).lastrowid
                for alinea in article.alineas:
                    db.query("INSERT INTO alineas (ArticleID, Text) VALUES (%s, %s) ON DUPLICATE KEY UPDATE Text = %s", (article_id, alinea.text, alinea.text))

class Alinea:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return " "*6+self.title

class Article:
    def __init__(self, title, alineas=[]):
        self.title = title
        self.alineas = alineas
    
    def add_alinea(self, alinea):
        self.alineas.append(alinea)

    def __str__(self):
        # return a string with the title and the alineas with good format
        temp = ""
        for i in range(len(self.alineas)):
            alinea = self.alineas[i]
            temp += f"    {i+1}.{alinea}\n"
        return self.title + "\n" + temp

    def __iter__(self):
        return iter(self.alineas)

class Section:
    def __init__(self, title, articles=[]):
        self.title = title
        self.articles = articles

    def add_article(self, article):
        self.articles.append(article)

    def __str__(self):
        # return a string with the title and the articles with good format
        temp = ""
        for i in range(len(self.articles)):
            article = self.articles[i]
            temp += f"  {i+1}. {article}\n"
        return self.title + "\n" + temp
    
    def __iter__(self):
        return iter(self.articles)

class Law:
    def __init__(self, title, sections=[]):
        self.title = title
        self.sections = sections

    def add_section(self, section):
        self.sections.append(section)

    def __str__(self):
        # return a string with the title and the sections with good format
        temp = ""
        for i in range(len(self.sections)):
            section = self.sections[i]
            temp += f"{i+1}. {section}\n"
        return self.title + "\n" + temp
    
    def __iter__(self):
        return iter(self.sections)
