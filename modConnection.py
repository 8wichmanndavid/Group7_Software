import mysql.connector
from mysql.connector import Error

class Connection:
    def __init__(self, host, user, password, database, port=3306):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port

    def Connect(self):
        try:
            print("Connecting to database", self.database + "...")
            self.connection = mysql.connector.connect(
                host = self.host, 
                user = self.user, 
                password = self.password, 
                database = self.database,
                port = self.port
            )
            self.cursor = self.connection.cursor()
            print("Connection to", self.database, "successful")
        except Error as e:
            print("Error: ", e)

    def Disconnect(self):
        print("Closing connection...")
        self.cursor.close()
        self.connection.close()
        print("Connection terminated")
