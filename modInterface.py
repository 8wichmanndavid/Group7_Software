from tkinter import *
from modConnection import *
import Queries

class Window(Frame):
    
    def __init__(self, connection, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.master.geometry("1000x700")

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

        self.btnSearch = Button(self, text="Search", command=self.search)
        self.btnSearch["width"] = 7
        self.btnSearch.place(x=325, y=50)

        self.btnReset = Button(self, text="Reset", command=self.reset)
        self.btnReset["width"] = 7
        self.btnReset.place(x=400, y=50)

        self.txtDisplay = Text(self, height=35, width=118)
        self.txtDisplay["state"] = "disabled"
        self.txtDisplay.place(x=25, y=90)

        self.btnExpiration = Button(self, text = "Show Expiration Date", command=self.showExpiration)
        self.btnExpiration["width"] = "16"
        self.btnExpiration.place(x = 495, y = 50)

        # Initialize display with all products
        self.reset()

    def client_exit(self):
        self.connection.Disconnect()
        exit()

    def display(self, textOutput):

        # Initialize display box for editing
        self.txtDisplay["state"] = "normal"
        self.txtDisplay.delete("1.0", "end-1c")

        # Display result
        self.txtDisplay.insert(END, textOutput)

        # Disable display box to prevent editing
        self.txtDisplay["state"] = "disabled"

    def reset(self):

        # Clear search box
        self.txtSearch.delete("1.0", "end-1c")

        data = Queries.DbQueries.ShowAll_Inventory(self.connection.cursor)
        output = self.formatResult(data)

        self.display(output)

    def search(self):
        # Get search criteria
        searchBy = self.txtSearch.get("1.0", "end-1c")

        # Determine table column to search by
        if searchBy.isnumeric():
            filterBy = "prod.SKU = " + searchBy
            data = Queries.DbQueries.SearchQuery(self.connection.cursor, filterBy)

        elif searchBy == "":
            data = Queries.DbQueries.ShowAll_Inventory(self.connection.cursor)

        else:
            filterBy = "prod.PROD_NAME = '" + searchBy.lower() + "'"
            data = Queries.DbQueries.SearchQuery(self.connection.cursor, filterBy)

        output = self.formatResult(data)
        self.display(output)

    def formatResult(self, resultList):

        # "View" header
        output = "{:12s}{:25s}{:40s}{:9s}{:7s}{:10s}\n".format(
                    "Quantity", "Brand", "Product", "SKU", "Price", "Department") +\
                    "="*105 + "\n"
        
        for result in resultList:
            output += "{:<12f}{:25s}{:40s}{:<9f}{:<7.2f}{:10s}\n".format(
                result[0], result[1], result[2], result[3], result[4], result[5]
            )
        
        return output

    def showExpiration(self):
        self.txtDisplay["state"] = "normal"
        self.txtDisplay.delete("1.0", "end-1c")

        data = Queries.DbQueries.Expiration(self.connection.cursor)
        output = self.formatExpirationResult(data)
        
        self.txtDisplay.insert(END, output)

    def formatExpirationResult(self, resultList):
        output = "{:40s}{:25s}{:12s}{:12s}{:7s}{:12s}{:7s}\n".format(
                    "Product", "Brand", "Department", "Quantity", "Cost", "Expiration", "SKU") +\
                    "="*115 + "\n"
        
        for result in resultList:
            output += "{:40s}{:25s}{:12s}{:<12f}{:<7.2f}{:12s}{:<9f}\n".format(
                result[0], result[1], result[2], result[3], result[4], str(result[5]), result[6]
            )

        return output
