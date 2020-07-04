from tkinter import *
from modConnection import *
from modInterface import *
import Queries
import mysql.connector

class AddEmployee(Toplevel):
    def __init__(self, connection, master = None):
        super().__init__(master = master)
        self.geometry("500x300")
        self.textFields = "Employee Number", "First Name", "Middle Initial", "Last Name", "Department #", "Password"
        self.theEntries = []
        self.connection = connection
        self.initWindow()
        self.buildForm()

    def initWindow(self):
        self.title("Add Employee")        
        self.btnSubmit = Button(self, text='Submit', command=self.submitForm)
        self.btnSubmit["width"] = 10 ; self.btnSubmit.place(x=100, y=200)
        self.btnClose = Button(self, text='Cancel', command=self.destroy)
        self.btnClose["width"] = 10 ; self.btnClose.place(x=200, y=200)
        

    def submitForm(self):
        empList = self.fetchEntries()
        Queries.DbQueries.addCred(self.connection.cursor, empList, self.connection)
        self.destroy()

    def buildForm(self):
        for aField in self.textFields:
            aRow = Frame(self)
            aLabel = Label(aRow, width = 15, text = aField, anchor = "w")
            anEntry = Entry(aRow)
            aRow.pack(side = TOP, fill = X, padx = 5, pady = 5)
            aLabel.pack(side = LEFT)
            anEntry.pack(side = RIGHT, expand = YES, fill = X)
            self.theEntries.append((aField, anEntry))

    def fetchEntries(self):
        empList = []
        for an_entry in self.theEntries:
            aField = an_entry[0]
            theText = an_entry[1].get()
            empList.append(theText)

        return empList
