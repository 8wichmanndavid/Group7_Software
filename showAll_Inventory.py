import mysql.connector

def showAll_Inventory(mycursor):
    sqlvar = "SELECT PRODUCTS.PROD_NAME, PRODUCTS.BRAND, DEPARTMENT.DEPT_NAME, SUM(INVENTORY.QUANTITY), PRODUCTS.UNIT_PRC, INVENTORY.SKU \
                     FROM DEPARTMENT \
                     JOIN PRODUCTS \
                     ON \
                     PRODUCTS.DEPT_NUM = DEPARTMENT.DEPT_NUM \
                     JOIN INVENTORY \
                     ON \
                     INVENTORY.SKU = PRODUCTS.SKU \
                     GROUP BY \
                     DEPARTMENT.DEPT_NAME, \
                     PRODUCTS.PROD_NAME, \
                     PRODUCTS.BRAND, \
                     PRODUCTS.UNIT_PRC, \
                     INVENTORY.SKU"
                     
    mycursor.execute(sqlvar)
    result = mycursor.fetchall()

    return result
                 
                 
                 
                 
                
                 
                 
