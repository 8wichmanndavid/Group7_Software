from tkinter import *
import modInterface as interface
import Queries

class LoginWindow(Frame):

    def __init__(self, connection, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.master.geometry("400x400")

        self.connection = connection 
        self.initWindow()

    def initWindow(self):
        self.master.title("Login")
        self.pack(fill=BOTH, expand=1)
        self.connection.Connect()

        self.txtUserName = Entry(self.master)
        self.txtUserName.place(x=30, y=50)

        self.txtPassword = Entry(self.master, show='*')
        self.txtPassword.place(x=30,y=90)

        self.btnLogin = Button(self, text="Login", command=lambda: self.login(interface.Window))
        self.btnLogin["width"] = 7
        self.btnLogin.place(x=30, y=130)

    def login(self, _class):
        var = StringVar()
        var.set("")
        #if self.validateUser():
        if True:
            self.txtPassword.delete("0", "end")
            root = Tk()
            app = interface.Window(self.connection, root, _class)
            root.mainloop()

        else:
            # Display message to user
            self.label = Label(self, textvariable=var)
            var.set("Username or Password is invalid")
            self.label.place(x=50, y=5)

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