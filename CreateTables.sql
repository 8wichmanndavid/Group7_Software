DROP TABLE IF EXISTS SALES;
DROP TABLE IF EXISTS EMPLOYEES;
DROP TABLE IF EXISTS INVENTORY;
DROP TABLE IF EXISTS DELIVERY;
DROP TABLE IF EXISTS PRODUCTS;
DROP TABLE IF EXISTS DEPARTMENT;


CREATE TABLE DEPARTMENT(
DEPT_NUM NUMERIC(2) PRIMARY KEY,
DEPT_NAME VARCHAR(30) NOT NULL
);

CREATE TABLE PRODUCTS(
SKU NUMERIC(8) PRIMARY KEY,
PROD_NAME NUMERIC(2) REFERENCES DEPARTMENT,
BRAND VARCHAR(30) NOT NULL,
DEPT_NUM NUMERIC(2) REFERENCES DEPARTMENT,
UNIT_PRC NUMERIC(5,2)
);

CREATE TABLE DELIVERY(
DEL_NUM NUMERIC(8) PRIMARY KEY,
DATE_REC DATETIME
);

CREATE TABLE INVENTORY(
SKU NUMERIC(8) REFERENCES PRODUCTS,
DEL_NUM NUMERIC(8) REFERENCES DELIVERY,
EXPIR_DATE DATE,
QUANTITY NUMERIC(8),
primary key (SKU, DEL_NUM, EXPIR_DATE)
);

CREATE TABLE EMPLOYEES(
EMP_NUM NUMERIC(8) PRIMARY KEY,
F_NAME VARCHAR(30) NOT NULL,
M_INIT VARCHAR(1) NOT NULL,
L_NAME VARCHAR(30) NOT NULL,
DEPT_NUM NUMERIC(2) REFERENCES DEPARTMENT,
CRIDENCIALS VARCHAR(30) NOT NULL
);

CREATE TABLE SALES(
SALE_NUM NUMERIC(8) PRIMARY KEY,
EMP_NUM NUMERIC(8) REFERENCES EMPLOYEES,
SALE_PRICE NUMERIC(8,2) NOT NULL
)