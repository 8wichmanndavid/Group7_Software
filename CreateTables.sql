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
PROD_NAME VARCHAR(50) NOT NULL,
BRAND VARCHAR(30) NOT NULL,
DEPT_NUM NUMERIC(2) REFERENCES DEPARTMENT,
UNIT_PRC NUMERIC(5,2)
);

CREATE TABLE DELIVERY(
DEL_NUM NUMERIC(8) PRIMARY KEY,
DATE_REC DATE
);

CREATE TABLE INVENTORY(
SKU NUMERIC(8) REFERENCES PRODUCTS,
DEL_NUM NUMERIC(8) REFERENCES DELIVERY,
EXPIR_DATE DATE,
QUANTITY NUMERIC(8),
primary key (SKU, DEL_NUM, EXPIR_DATE)
);

#############################################
insert into department
(
dept_num,
dept_name
)
values
('01', "Bakery"),
('02', "Frozen Food"),
('03', "Dairy"),
('04', "Grocery"),
('05', "Produce");

#############################################
insert into delivery
(
del_num,
date_rec
)
values
('12345678', '2020-04-29'),
('87654321', '2020-05-06'),
('45612378', '2020-05-13'),
('78654321', '2020-05-20'),
('87456321', '2020-05-27'),
('45687231', '2020-06-03'),
('14725836', '2020-06-10');

#############################################
insert into products
(
sku,
prod_name,
brand,
dept_num,
unit_prc
)
values
('97577', 'chocolate chip cookies', "four brothers bakery", '01', '5.99'),
('34832', 'chocolate iced cake donuts', "bake shoppe", '01', '6.99'),
('83257', 'double chocolate brownie cookies', "bake shoppe", '01', '4.99'),
('43742', 'glazed donut holes', "bake shoppe", '01', '3.00'),
('103171', 'jumbo blueberry muffins', "bake shoppe", '01', '4.99'),
('34824', 'authentic round sourdough bread', "fresh supermart", '01', '3.99'),
('93275', 'caraway rye bread', "fresh supermart", '01', '3.49'),
('70576', 'home style white bread', "bake shoppe", '01', '2.99'),
('82994', 'honey whole grain bread', "artisan bread", '01', '2.00'),
('85576', 'cinnamon burst bread', "fresh supermart", '01', '2.99'),

('101097', 'cheeseburger sandwich', "@ease", '02', '1.98'),
('906885', 'house cut fries', "alexia", '02', '3.99'),
('890887', 'sweet potato fries', "alexia", '02', '4.43'),
('8219', 'cherry garcia ice cream', "ben & jerrys", '02', '4.99'),
('102303', 'chocopolitan ice cream', "blue bunny", '02', '6.55'),
('87464', 'new york vanilla ice cream', "cass clay", '02', '6.99'),
('100794', 'drumstick cookie dipped', "nestle", '02', '6.98'),
('80231', 'four meat pizza', "bellatoria", '02', '6.98'),
('74719', 'four cheese traditional crust pizza', "digiorno", '02', '3.98'),
('33693', 'sausage original thin pizza', "jacks", '02', '3.99'),

('65833', 'light stick 16oz', "blue bonnet", '03', '0.98'),
('4018', 'margarine sticks', "blue bonnet", '03', '0.98'),
('91583', 'fancy shredded cheddar cheese', "bongards", '03', '2.79'),
('91584', 'fancy shredded colby jack cheese', "bongards", '03', '2.79'),
('87344', '2% milk', "cass clay", '03', '3.79'),
('87318', 'butter quarters', "cass clay", '03', '3.38'),
('87379', 'cottage cheese 2%', "cass clay", '03', '3.59'),
('87355', 'skim milk', "cass clay", '03', '3.69'),
('87076', 'swiss chocolate', "cass clay", '03', '5.48'),
('87372', 'sour cream', "cass clay", '03', '2.28'),

('5524', 'cheerios', "general mills", '04', '3.28'),
('5636', 'honey nut chex', "general mills", '04', '3.28'),
('16019', 'cocoa pebbles', "post", '04', '3.89'),
('5612', 'corn flakes', "kellogg's", '04', '4.49'),
('29221', 'chicken noodle soup', "campbell's", '04', '1.75'),
('6728', 'cream of mushroom soup', "campbell's", '04', '1.19'),
('11800', 'chicken noodle soup', "healthy choice", '04', '2.43'),
('6680', 'chicken ramen noodles', "maruchan", '04', '0.29'),
('69705', 'tomato ketchup', "annies", '04', '3.89'),
('40583', 'tomato ketchup', "heinz", '04', '2.99'),

('96979', 'iceberg lettuce', "pasar", '05', '1.78'),
('31109', 'romaine lettuce', "calorganic", '05', '2.48'),
('82629', 'Bulk peanuts unsalted in shell', "Jimmy Carter Farms ", '05', '1.98'),
('8673', 'baby peeled carrots', "green giant", '05', '1.48'),
('19353', 'baby boy tomatoes', "bushel boy", '05', '3.98'),
('103162', 'mandarins', "halo", '05', '7.99'),
('102517', 'blackberries', "driscoll", '05', '3.48'),
('8782', 'strawberries', "driscoll", '05', '2.50'),
('83680', 'apples-braeburn', "dole", '05', '5.98'),
('8702', 'baby bella whole mushrooms', "green giant", '05', '2.50'),
('64834', 'bananas', "dole", '05', '0.20');

#############################################
insert into inventory
(
sku,
del_num,
expir_date,
quantity
)
values
('4018', '12345678', '2020-05-13', '200'),
('4018', '78654321', '2020-06-03', '200'),
('5524', '12345678', '2020-07-03', '85'),
('5612', '12345678', '2020-07-03', '85'),
('5636', '12345678', '2020-07-03', '85'),
('6680', '12345678', '2030-01-01', '775'),
('6728', '14725836', '2030-07-03', '100'),
('8219', '12345678', '2020-05-13', '15'),
('8219', '78654321', '2020-05-27', '15'),
('8219', '14725836', '2020-07-03', '15'),
('8673', '87456321', '2020-06-26', '50'),
('8702', '45687231', '2020-06-11', '200'),
('8782', '45687231', '2020-06-30', '85'),
('11800', '87654321', '2020-07-31', '85'),
('16019', '45612378', '2020-07-03', '85'),
('19353', '78654321', '2030-06-14', '775'),
('19353', '14725836', '2030-07-14', '775'),
('29221', '14725836', '2030-09-11', '100'),
('31109', '45612378', '2020-06-03', '100'),
('31109', '45687231', '2020-07-04', '100'),
('33693', '87456321', '2020-07-04', '275'),
('34824', '78654321', '2020-05-27', '10'),
('34824', '87456321', '2020-06-03', '10'),
('34824', '45687231', '2020-06-10', '10'),
('34824', '14725836', '2020-06-17', '10'),
('34832', '14725836', '2020-07-04', '15'),
('40583', '78654321', '2020-07-04', '100'),
('43742', '45687231', '2020-07-04', '28'),
('64834', '45687231', '2020-06-25', '1000'),
('64834', '14725836', '2020-07-04', '1000'),
('65833', '87654321', '2020-07-04', '67'),
('69705', '12345678', '2020-10-04', '400'),
('70576', '14725836', '2020-06-24', '9'),
('74719', '87654321', '2020-09-04', '843'),
('80231', '45612378', '2020-08-04', '1009'),
('82629', '78654321', '2020-07-04', '8000'),
('82994', '45687231', '2020-06-21', '10'),
('83257', '78654321', '2020-07-04', '6600'),
('83680', '87456321', '2020-07-04', '19'),
('85576', '87456321', '2020-06-24', '55'),
('87076', '14725836', '2020-07-04', '100'),
('87318', '45687231', '2020-07-04', '44'),
('87355', '14725836', '2020-06-30', '480'),
('87372', '45687231', '2020-07-04', '80'),
('87379', '45687231', '2020-07-04', '50'),
('87464', '45612378', '2020-07-04', '1800'),
('91583', '45687231', '2020-06-14', '160'),
('93275', '87456321', '2020-07-04', '4'),
('96979', '45687231', '2020-06-09', '400'),
('96979', '14725836', '2020-07-04', '400'),
('97577', '87456321', '2020-07-04', '3300'),
('100794', '12345678', '2020-06-15', '18'),
('100794', '14725836', '2020-07-04', '48'),
('101097', '12345678', '2020-08-04', '60'),
('102303', '87654321', '2020-07-04', '40'),
('102517', '87456321', '2020-06-09', '10'),
('102517', '14725836', '2020-07-04', '120'),
('103162', '14725836', '2020-07-04', '105'),
('103171', '45687231', '2020-06-11', '8'),
('890887', '78654321', '2020-08-04', '330'),
('906885', '45612378', '2020-08-04', '756');







