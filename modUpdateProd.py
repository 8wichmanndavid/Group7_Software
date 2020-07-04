from tkinter import *
from modConnection import *
from modInterface import *
import Queries
import mysql.connector

class updateProd(Toplevel):
    def __init__(self, connection, master = None):
        super().__init__(master = master)
        self.geometry("500x500")
        
        self.connection = connection
        self.initWindow()
        self.buildForm()

    def initWindow(self):
        

        self.textFields = "SKU", "Product Name", "Brand", "Department Number", "Unit Price"
        
        
        self.theEntries = []

        
        self.title("Update Product")        
        self.btnSubmit = Button(self, text='Submit', command=self.submitForm)
        self.btnSubmit["width"] = 10 ; self.btnSubmit.place(x=100, y=240)
        self.btnClose = Button(self, text='Cancel', command=self.destroy)
        self.btnClose["width"] = 10 ; self.btnClose.place(x=200, y=240)
        

    def submitForm(self):
        tempList = self.fetchEntries()
        Queries.DbQueries.updateProductQuery(self.connection.cursor, tempList, self.connection)
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
        tempList = []
        for an_entry in self.theEntries:
            aField = an_entry[0]
            theText = an_entry[1].get()
            tempList.append(theText)
        return tempList
    
    

