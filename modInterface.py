from tkinter import *
from modConnection import *

class Window(Frame):
    displayHeader = "{:s}{:s}{:s}\n".format("ID", "Product", "Department") + \
                    "============================\n"
    
    def __init__(self, connection, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.master.geometry("500x500")

        self.connection = connection
        self.initWindow()

    def initWindow(self):
        self.master.title("Inventory Management")
        self.pack(fill=BOTH, expand=1)
        self.connection.Connect()
        
        self.btnQuit = Button(self, text="Exit", command=self.client_exit)
        self.btnQuit.place(x=5, y=5)

        self.txtSearch = Text(self, height=1, width=30)
        self.txtSearch.place(x=25, y=50)

        self.btnSearch = Button(self, text="Search", command=self.display)
        self.btnSearch["width"] = 7
        self.btnSearch.place(x=325, y=50)

        self.btnReset = Button(self, text="Reset", command=self.reset)
        self.btnReset["width"] = 7
        self.btnReset.place(x=410, y=50)

        self.txtDisplay = Text(self, height=24, width=55)
        self.txtDisplay["state"] = "disabled"
        self.txtDisplay.place(x=25, y=90)

        self.reset()

    def client_exit(self):
        self.connection.Disconnect()
        exit()

    def display(self):

        # Initialize display box for editing
        self.txtDisplay["state"] = "normal"
        self.txtDisplay.delete("1.0", "end-1c")

        # Get search criteria
        searchBy = self.txtSearch.get("1.0", "end-1c")

        # Query database
        if searchBy.isalpha(): 
            filterBy = "lastName = " + "'" + searchBy + "'"
            data = self.connection.ExecuteQuery("Authors", where=filterBy)

        elif searchBy.isnumeric():
            filterBy = "authorId = " + "'" + searchBy + "'"
            data = self.connection.ExecuteQuery("Authors", where=filterBy)
        
        else:
            data = self.connection.ExecuteQuery("Authors")

        # Format result
        output = self.format(data)

        # Display result
        self.txtDisplay.insert(END, output)

        # Disable display box to prevent editing
        self.txtDisplay["state"] = "disabled"

    def reset(self):
        self.txtSearch.delete("1.0", "end-1c")
        self.display()

    def format(self, resultList):
        output = Window.displayHeader
        
        # TODO: Clean results of punctuation and format spacing to align with header
        for result in resultList:
            output += str(result) + "\n"

        return output
