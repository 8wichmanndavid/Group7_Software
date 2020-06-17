from tkinter import *
from modConnection import *
import showAll_Inventory as showAll
import Expiration as exp

class Window(Frame):

    # Format spacing for 'View' header and query results
    defaultHeaderSpacing = "{:12s}{:25s}{:40s}{:9s}{:7s}{:10s}\n"
    defaultValueSpacing = "{:<12f}{:25s}{:40s}{:<9f}{:<7.2f}{:10s}\n"
    defaultHeader = defaultHeaderSpacing.format("Quantity", "Brand", "Product", "SKU", "Price", "Department") + \
                    "="*100 + "\n"

    expirationHeaderSpacing = "{:40s}{:25s}{:12s}{:12s}{:7s}{:12s}{:9s}\n"
    expirationValueSpacing = "{:40s}{:25s}{:12s}{:<12f}{:<7.2f}{:12s}{:<9f}\n"
    expirationHeader = expirationHeaderSpacing.format("Product", "Brand", "Department", "Quantity", "Price", "Expiration", "SKU") +\
                    "="*115 + "\n"
    
    def __init__(self, connection, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.master.geometry("900x700")

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

        self.btnExpir = Button(self, text="Expire", command=self.getExpirationDates)
        self.btnExpir["width"] = 7
        self.btnExpir.place(x=470, y=50)

        self.txtDisplay = Text(self, height=35, width=105)
        self.txtDisplay["state"] = "disabled"
        self.txtDisplay.place(x=25, y=90)

        self.reset()

    def client_exit(self):
        self.connection.Disconnect()
        exit()

    def getExpirationDates(self):
        self.master.geometry("1000x700")
        self.txtDisplay["width"] = 118
        # Initialize display box for editing
        self.txtDisplay["state"] = "normal"
        self.txtDisplay.delete("1.0", "end-1c")

        data = exp.expiration(self.connection.cursor)
        output = self.formatExp(data)

        # Display result
        self.txtDisplay.insert(END, output)

        # Disable display box to prevent editing
        self.txtDisplay["state"] = "disabled"

    def display(self):

        # Initialize display box for editing
        self.txtDisplay["state"] = "normal"
        self.txtDisplay.delete("1.0", "end-1c")

        # Get search criteria
        searchBy = self.txtSearch.get("1.0", "end-1c")

        # Query database
        if searchBy.isnumeric():
            filterBy = "prod.SKU = " + searchBy 
            data = self.connection.ExecuteQueryLiteral(
                    "SELECT SUM(inv.QUANTITY), prod.BRAND, prod.PROD_NAME, inv.SKU, prod.UNIT_PRC, dept.DEPT_NAME \
                     FROM GroceryApp_DEPARTMENT as dept\
                     JOIN GroceryApp_PRODUCTS as prod ON prod.DEPT_NUM = dept.DEPT_NUM \
                     JOIN GroceryApp_INVENTORY as inv ON inv.SKU = prod.SKU \
                     WHERE " + filterBy + 
                     " GROUP BY \
                     dept.DEPT_NAME, \
                     prod.PROD_NAME, \
                     prod.BRAND, \
                     prod.UNIT_PRC, \
                     inv.SKU"
            )
        
        elif searchBy == "":
            data = showAll.showAll_Inventory(self.connection.cursor)
        
        else: 
            filterBy = "prod.PROD_NAME = '" + searchBy.lower() + "'" 
            data = self.connection.ExecuteQueryLiteral(
                    "SELECT SUM(inv.QUANTITY), prod.BRAND, prod.PROD_NAME, inv.SKU, prod.UNIT_PRC, dept.DEPT_NAME \
                     FROM GroceryApp_DEPARTMENT as dept\
                     JOIN GroceryApp_PRODUCTS as prod ON prod.DEPT_NUM = dept.DEPT_NUM \
                     JOIN GroceryApp_INVENTORY as inv ON inv.SKU = prod.SKU \
                     WHERE " + filterBy + 
                     " GROUP BY \
                     dept.DEPT_NAME, \
                     prod.PROD_NAME, \
                     prod.BRAND, \
                     prod.UNIT_PRC, \
                     inv.SKU"
            )
    
        # Format result
        output = self.format(data)

        # Display result
        self.txtDisplay.insert(END, output)

        # Disable display box to prevent editing
        self.txtDisplay["state"] = "disabled"

    def reset(self):
        self.txtSearch.delete("1.0", "end-1c")
        self.display()

        self.master.geometry("900x700")
        self.txtDisplay["width"] = 105

    def format(self, resultList):
        output = Window.defaultHeader
        
        for result in resultList:
            output += Window.defaultValueSpacing.format(
                result[0], result[1], result[2], result[3], result[4], result[5]
            )

        return output

    def formatExp(self, resultList):
        output = Window.expirationHeader
        
        for result in resultList:
            output += "{:40s}{:25s}{:12s}{:<12f}{:<7.2f}{:12s}{:<9f}\n".format(
                result[0], result[1], result[2], result[3], result[4], str(result[5]), result[6]
            )

        return output