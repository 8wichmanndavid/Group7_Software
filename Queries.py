import mysql.connector

class DbQueries:
    @classmethod
    def ShowAll_Inventory(self, mycursor):
        sqlvar = "SELECT SUM(inv.QUANTITY), prod.BRAND, prod.PROD_NAME, inv.SKU, prod.UNIT_PRC, dept.DEPT_NAME \
                 FROM GroceryApp_DEPARTMENT as dept\
                 JOIN GroceryApp_PRODUCTS as prod ON prod.DEPT_NUM = dept.DEPT_NUM \
                 JOIN GroceryApp_INVENTORY as inv ON inv.SKU = prod.SKU \
                 GROUP BY \
                 dept.DEPT_NAME, \
                 prod.PROD_NAME, \
                 prod.BRAND, \
                 prod.UNIT_PRC, \
                 inv.SKU"
                     
        mycursor.execute(sqlvar)
        result = mycursor.fetchall()
        
        return result

    @classmethod
    def Expiration(self, mycursor):
        sqlvar = "SELECT PROD.PROD_NAME, PROD.BRAND, DEPT.DEPT_NAME, INV.QUANTITY, PROD.UNIT_PRC, INV.EXPIR_DATE, PROD.SKU\
                FROM GroceryApp_PRODUCTS AS PROD\
                JOIN GroceryApp_INVENTORY AS INV ON PROD.SKU = INV.SKU\
                JOIN GroceryApp_DEPARTMENT AS DEPT ON DEPT.DEPT_NUM = PROD.DEPT_NUM\
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

    @classmethod
    def SearchQuery(self, mycursor, searchBy):
        sqlvar = ("SELECT SUM(inv.QUANTITY), prod.BRAND, prod.PROD_NAME, inv.SKU, prod.UNIT_PRC, dept.DEPT_NAME \
                     FROM GroceryApp_DEPARTMENT as dept\
                     JOIN GroceryApp_PRODUCTS as prod ON prod.DEPT_NUM = dept.DEPT_NUM \
                     JOIN GroceryApp_INVENTORY as inv ON inv.SKU = prod.SKU \
                     WHERE " + searchBy + 
                     " GROUP BY \
                     dept.DEPT_NAME, \
                     prod.PROD_NAME, \
                     prod.BRAND, \
                     prod.UNIT_PRC, \
                     inv.SKU")

        mycursor.execute(sqlvar)
        result = mycursor.fetchall()
        
        return result

    @classmethod
    def CheckCredentials(self, mycursor, empNum, password):
        tmp = str(empNum)
        sqlvar = "SELECT CREDENTIALS FROM EMPLOYEES\
                  WHERE EMP_NUM = " + tmp + ";"

        return password == mycursor.execute(sqlvar)

    @classmethod
    def Remove(self, mycursor, sku):
        tmp = str(sku)
        sqlvar = "DELETE FROM INVENTORY\
                  WHERE SKU = " + tmp + ";\
                  DELETE FROM PRODUCTS\
                  WHERE SKU = " + tmp + ";"

        mycursor.execute(sqlvar)