from tkinter import *
from modConnection import *
from modInterface import *
import Queries
import mysql.connector


class Remove_Product(Toplevel):
    def __init__(self, connection, master = None):
        super().__init__(master = master)
        self.geometry("600x600")
        self.textField = "SKU"
        self.theEntries = []
        self.connection = connection
        self.initWindow()
        self.buildForm()

    def initWindow(self):
        self.title("Remove Product")
        self.btnSubmit = Button(self, text = "Submit", command = self.submitForm)
        self.btnSubmit.pack(side = BOTTOM)

    def submitForm(self):
        tempProductList = self.fetchEntries()
        Queries.DbQueries.Remove(self.connection.cursor, tempProductList[0], self.connection)
        self.destroy()

    def buildForm(self):
        aRow = Frame(self)
        aLabel = Label(aRow, width = 15, text = self.textField, anchor = "w")
        anEntry = Entry(aRow)
        aRow.pack(side = TOP, fill = X, padx = 5, pady = 5)
        aLabel.pack(side = LEFT)
        anEntry.pack(side = RIGHT, expand = YES, fill = X)
        self.theEntries.append((self.textField, anEntry))

    def fetchEntries(self):
        tempList = []
        for an_entry in self.theEntries:
            aField = an_entry[0]
            theText = an_entry[1].get()
            tempList.append(theText)

        return tempList
