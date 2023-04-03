import mysql.connector

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()

    def query(self, query, params=None):
        self.cursor.execute(query, params)
        self.connection.commit()
        return self.cursor

    def __del__(self):
        self.connection.close()

