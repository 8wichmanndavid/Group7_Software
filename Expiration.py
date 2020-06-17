import mysql.connector

def expiration(mycursor):
    sqlvar = "SELECT\
                PROD_NAME,\
                BRAND,\
                DEPT_NAME,\
                QUANTITY,\
                UNIT_PRC,\
                EXPIR_DATE,\
                PROD.SKU\
                FROM GroceryApp_PRODUCTS AS PROD\
                JOIN GroceryApp_INVENTORY AS INV\
                ON PROD.SKU = INV.SKU\
                JOIN GroceryApp_DEPARTMENT AS DEPT\
                ON DEPT.DEPT_NUM = PROD.DEPT_NUM\
                ORDER BY\
                EXPIR_DATE,\
                DEPT_NAME, \
                PROD_NAME ,\
                QUANTITY,\
                BRAND ,\
                UNIT_PRC, \
                PROD.SKU"
                     
    mycursor.execute(sqlvar)
    result = mycursor.fetchall()
    return result
