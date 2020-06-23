import modInterface as interface
import modConnection as conn
from tkinter import *

def main():
    ''' 
    CONNECTION INFORMATION
    ----------------------
    Uncomment and add/change information as needed to access
    your specific database. Host and port are for campus DB.
    Port number may not be necessary if running a MySQL DB
    on the same machine as the program.
    '''

    host="localhost"
    # port=3306
    database="testgrocery"
    user="root"
    password="418733#zepWer"

    connection = conn.Connection(host, user, password, database)

    root = Tk()
    app = interface.Window(connection, root)
    root.mainloop()

main()
