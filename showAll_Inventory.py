import mysql.connector

def showAll_Inventory(mycursor):
    sqlvar = "SELECT SUM(inv.QUANTITY), prod.BRAND, prod.PROD_NAME, inv.SKU, prod.UNIT_PRC, dept.DEPT_NAME \
                     FROM DEPARTMENT as dept\
                     JOIN PRODUCTS as prod\
                     ON \
                     prod.DEPT_NUM = dept.DEPT_NUM \
                     JOIN INVENTORY as inv\
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
                 
                 
                 
                 
                
                 
                 
