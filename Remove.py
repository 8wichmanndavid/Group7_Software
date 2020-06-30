import mysql.connector

def REMOVE(mycursor, SKU):
    SKU = str(SKU)
    sqlvar = "DELETE FROM INVENTORY  \
                WHERE SKU =" + SKU + ";\
                DELETE FROM PRODUCTS \
                WHERE SKU =" + SKU + ";"                 
    mycursor.execute(sqlvar)
    
