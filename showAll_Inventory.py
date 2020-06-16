import mysql.connector

def showAll_Inventory(mycursor):
    sqlvar = "SELECT FORMAT(SUM(inv.QUANTITY), 0), prod.BRAND, prod.PROD_NAME, FORMAT(inv.SKU, 0), FORMAT(prod.UNIT_PRC, 2), dept.DEPT_NAME \
                     FROM GroceryApp_DEPARTMENT as dept\
                     JOIN GroceryApp_PRODUCTS as prod\
                     ON \
                     prod.DEPT_NUM = dept.DEPT_NUM \
                     JOIN GroceryApp_INVENTORY as inv\
                     ON \
                     inv.SKU = prod.SKU \
                     GROUP BY \
                     dept.DEPT_NAME, \
                     prod.PROD_NAME, \
                     prod.BRAND, \
                     prod.UNIT_PRC, \
                     inv.SKU"
                     
    mycursor.execute(sqlvar)
    result = mycursor.fetchall()

    return result
                 
                 
                 
                 
                
                 
                 
