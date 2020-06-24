#import modInterface as interface
import modLoginWindow as login
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

    host="puff.mnstate.edu"
    port=3306
    database="nathan-heidt_books"
    user="nathan-heidt"
    password="Oblivion4$"

    connection = conn.Connection(host, user, password, database)

    root = Tk()
    app = login.LoginWindow(connection, root)
    root.mainloop()

main()
