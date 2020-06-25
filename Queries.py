import mysql.connector

class DbQueries:
    @classmethod
    def ShowAll_Inventory(self, mycursor):
        sqlvar = "SELECT SUM(inv.QUANTITY), prod.BRAND, prod.PROD_NAME, inv.SKU, prod.UNIT_PRC, dept.DEPT_NAME \
                 FROM DEPARTMENT as dept\
                 JOIN PRODUCTS as prod ON prod.DEPT_NUM = dept.DEPT_NUM \
                 JOIN INVENTORY as inv ON inv.SKU = prod.SKU \
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
                FROM PRODUCTS AS PROD\
                JOIN INVENTORY AS INV ON PROD.SKU = INV.SKU\
                JOIN DEPARTMENT AS DEPT ON DEPT.DEPT_NUM = PROD.DEPT_NUM\
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
                     FROM DEPARTMENT as dept\
                     JOIN PRODUCTS as prod ON prod.DEPT_NUM = dept.DEPT_NUM \
                     JOIN INVENTORY as inv ON inv.SKU = prod.SKU \
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
    def addProductQuery(self, mycursor, productList):
        #print(productList)
        #self._db = mysql.connector.connect(host="localhost", user="root", password="418733#zepWer", database="testgrocery")
        
        sql_department_insert = "INSERT IGNORE INTO DEPARTMENT(DEPARTMENT.DEPT_NUM, DEPARTMENT.DEPT_NAME)VALUES(%s, %s)"
        sql_department_val = (productList[0], productList[1])

        sql_delivery_insert = "INSERT IGNORE INTO DELIVERY(DELIVERY.DEL_NUM, DELIVERY.DATE_REC)VALUES(%s, %s)"
        sql_delivery_val = (productList[2], productList[3])  
        
        sql_products_insert = "INSERT IGNORE INTO PRODUCTS(PRODUCTS.SKU, PRODUCTS.PROD_NAME, PRODUCTS.BRAND, PRODUCTS.DEPT_NUM, PRODUCTS.UNIT_PRC)VALUES(%s, %s, %s, %s, %s)"
        sql_products_val = (productList[4], productList[5], productList[6], productList[0], productList[7])
        
        sql_inventory_insert = "INSERT IGNORE INTO INVENTORY(INVENTORY.SKU, INVENTORY.DEL_NUM, INVENTORY.EXPIR_DATE, INVENTORY.QUANTITY)VALUES(%s, %s, %s, %s)"
        sql_inventory_val = (productList[4], productList[2], productList[8], productList[9])
        
        mycursor.execute(sql_department_insert, sql_department_val)
        mycursor.execute(sql_delivery_insert, sql_delivery_val)
        mycursor.execute(sql_products_insert, sql_products_val)
        mycursor.execute(sql_inventory_insert, sql_inventory_val)

        #self._db.commit()
