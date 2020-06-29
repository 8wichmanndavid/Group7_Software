from tkinter import *
import modInterface as interface
import Queries

class LoginWindow(Frame):

    def __init__(self, connection, master = None):
        center_x = master.winfo_screenwidth()/2 - 100
        center_y = master.winfo_screenheight()/2 - 100

        Frame.__init__(self, master)
        self.master = master
        self.master.geometry("200x200+%d+%d" % (center_x,center_y))

        self.connection = connection 
        self.initWindow()

    def initWindow(self):
        self.master.title("Login")
        self.pack(fill=BOTH, expand=1)
        self.connection.Connect()

        self.txtUserName = Entry(self.master)
        self.txtUserName.place(x=40, y=80)

        self.txtPassword = Entry(self.master, show='*')
        self.txtPassword.place(x=40,y=120)

        self.btnLogin = Button(self, text="Login", command=lambda: self.login(interface.Window))
        self.btnLogin["width"] = 7
        self.btnLogin.place(x=40, y=160)

        self.btnClose = Button(self, text="Close", command=self.client_exit)
        self.btnClose.place(x=145, y=5)
    
    def client_exit(self):
        self.connection.Disconnect()
        exit()

    def login(self, _class):

        # Get credentials from screen
        user = self.txtUserName.get()
        password = self.txtPassword.get()

        # Prep error message
        var = StringVar()
        var.set("")

        if Queries.DbQueries.CheckCredentials(self.connection.cursor, user, password):
            print("validation successful. Switching to Inventory Window...")
            self.txtPassword.delete("0", "end")
            root = Tk()
            app = interface.Window(self.connection, root, _class)
            root.mainloop()

        else:
            # Display message to user
            print("Validation failed")
            self.label = Label(self, textvariable=var)
            var.set("Username or Password is invalid")
            self.label.place(x=15, y=50)

    def validateUser(self):

        # Get credentials from screen
        user = self.txtUserName.get("1.0", "end-1c")
        password = self.txtPassword.get()
        isValidUser = False

        # Check database for user
        #queryResult = Queries.DbQueries

        # if len(queryResult) == 1:
        #     isValidUser = True

        return isValidUser