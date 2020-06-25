from tkinter import *
from modConnection import *
from modInterface import *
import Queries
import mysql.connector

class Add_Product(Toplevel):
    def __init__(self, connection, master = None):
        super().__init__(master = master)
        #self.title("Add/Remove/Update")
        self.geometry("600x600")
        self.textFields = "Department Num", "Department Name", "Delivery Number", "Date Received", "SKU", \
                          "Product Name", "Brand", "Unit Price", "Expiration Date", "Quantity"
        #self.textFields = "Department Num", "SKU", "Product Name", "Brand", "Unit Price"
        #self.textFields = "Department Num", "Department Name"
        self.theEntries = []
        self.connection = connection
        #self.connection = connection
        self.initWindow()
        self.buildForm()
        #self._db = mysql.connector.connect(host="localhost", user="root", password="418733#zepWer", database="testgrocery")
        #self.fetchEntries()
        #self.connection.commit()

    def initWindow(self):
        self.title("Add Product")
        self.btnSubmit = Button(self, text = "Submit", command = self.submitForm)
        self.btnSubmit.pack(side = BOTTOM)
        """
        self.productTextBox = Text(self, height = 1, width = 30)
        self.productTextBox.place(x = 100, y = 25)
        self.productTextLabel = Label(self, text = "Product Name")
        self.productTextLabel.place(x = 50, y = 25)
        """
        """
        self.productTextBoxLabel = Label(self, text = "Product Name").grid(row = 0)
        self.productTextBox = Entry(self)
        self.productTextBox.grid(row=0, column=1)
        """

    def submitForm(self):
        tempProductList = self.fetchEntries()
        Queries.DbQueries.addProductQuery(self.connection.cursor, tempProductList, self.connection)
        #sql_products_insert = "INSERT IGNORE INTO PRODUCTS(PRODUCTS.SKU, PRODUCTS.PROD_NAME, PRODUCTS.BRAND, PRODUCTS.DEPT_NUM, PRODUCTS.UNIT_PRC)VALUES(%s, %s, %s, %s, %s)"
        #sql_products_val = (tempProductList[4], tempProductList[5], tempProductList[6], tempProductList[0], tempProductList[7])
        #mycursor = self.connection.cursor()
        #mycursor.execute(sql_products_insert, sql_products_val)
        #print(self.connection)
        #self.connection.commit()
        #self._db.commit()
        self.destroy()

    def buildForm(self):
        #theEntries = []
        for aField in self.textFields:
            aRow = Frame(self)
            aLabel = Label(aRow, width = 15, text = aField, anchor = "w")
            anEntry = Entry(aRow)
            aRow.pack(side = TOP, fill = X, padx = 5, pady = 5)
            aLabel.pack(side = LEFT)
            anEntry.pack(side = RIGHT, expand = YES, fill = X)
            self.theEntries.append((aField, anEntry))
            #self.theEntries[aField] = anEntry
        #print(self.theEntries)

        #return self.theEntries

    #def getTheEntries(self):
        #tempList = self.theEntries.values()
        
        #return self.theEntries

         
    def fetchEntries(self):
        tempList = []
        for an_entry in self.theEntries:
            aField = an_entry[0]
            theText = an_entry[1].get()
            tempList.append(theText)

        return tempList
            #print('%s: "%s"' % (aField, theText))
    
        
    #def addProduct(self):
        #data = Queries.DbQueries.


    

     



        
