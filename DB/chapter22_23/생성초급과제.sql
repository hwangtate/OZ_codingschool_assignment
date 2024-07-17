USE classicmodels;

-- 1) customers 테이블에 새 고객을 추가하세요.
-- INSERT INTO	customers (customerNumber, customerName, phone) VALUES (501, 'new_taeyeong', '010-1111-1111');

-- 2) products 테이블에 새 제품을 추가하세요.
-- INSERT INTO products (productCode, productName, productLine) VALUES ('spy-tae-02', 'Lambolgini', 'Classic Cars');
-- SELECT * FROM products WHERE productCode = 'spy-tae-02';

-- (3) employees 테이블에 새 직원을 추가하세요.
-- INSERT INTO employees (employeeNumber, lastName, jobTitle) VALUES(1800, 'taeyeong', 'trader');
-- SELECT * FROM employees WHERE employeeNumber = 1800;

-- (4) offices 테이블에 새 사무실을 추가하세요.
-- INSERT INTO offices (officeCode, city) VAlUES ('ameria-01', 'silicon-vally');

-- (5) orders 테이블에 새 주문을 추가하세요.
-- INSERT INTO orders (orderNumber, orderDate) VALUES (100, '2024-07-17');

-- (6) orderdetails 테이블에 주문 상세 정보를 추가하세요.
-- ALTER TABLE orderdetails DROP FOREIGN KEY orderdetails_ibfk_1;
-- INSERT INTO orderdetails (orderNumber, productCode) VALUES (100, 'hi');

-- (7) payments 테이블에 지불 정보를 추가하세요.
-- INSERT INTO payments(customerNumber, checkNumber) VALUES (501, 'check_501');
-- SELECT * FROM payments WHERE customerNumber = 501;

-- (8) **`productlines`** 테이블에 제품 라인을 추가하세요.
-- INSERT INTO productlines (productLine) VALUES ('Legend Cars');
-- SELECT * FROM productlines;

-- (9) customers 테이블에 다른 지역의 고객을 추가하세요.
-- INSERT INTO customers (customerNumber, customerName, phone, addressLine1) VALUES (505,'taetae', '010-8888', '다른지역');
-- SELECT * FROM customers WHERE customerNumber = 505;

-- (10) products 테이블에 다른 카테고리의 제품을 추가하세요.
-- INSERT INTO products (productCode, productName, productLine) VALUES ('spy-tae-03', 'Lambolgini', 'Legend Cars');
-- SELECT * FROM products WHERE productCode = 'spy-tae-03'
