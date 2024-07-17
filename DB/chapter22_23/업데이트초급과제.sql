-- (1) customers 테이블에서 특정 고객의 주소를 갱신하세요.
-- UPDATE customers
-- SET addressLine1 = 'taeyeonghome'
-- WHERE customerNumber = 103

-- (2) products 테이블에서 특정 제품의 가격을 갱신하세요.
-- UPDATE products
-- SET buyPrice = 300
-- WHERE productCode = 'S10_1678'

-- (3) employees 테이블에서 특정 직원의 직급을 갱신하세요.
-- UPDATE employees 
-- SET jobTitle = 'subpresident'
-- WHERE employeeNumber = 1002

-- (4) offices 테이블에서 특정 사무실의 전화번호를 갱신하세요.
-- SET SQL_SAFE_UPDATES = 0;
-- UPDATE offices 
-- SET phone = '982'
-- WHERE officeCode = '2'

-- (5) orders 테이블에서 특정 주문의 상태를 갱신하세요.
-- UPDATE orders
-- SET status = 'done'
-- WHERE orderNumber = 10100

-- (6) orderdetails 테이블에서 특정 주문 상세의 수량을 갱신하세요.
-- UPDATE orderdetails
-- SET quantityOrdered = 123
-- WHERE orderNumber = 10100

-- (7) payments 테이블에서 특정 지불의 금액을 갱신하세요.
-- UPDATE payments
-- SET amount = 100
-- WHERE customerNumber = 353

-- (8) productlines 테이블에서 특정 제품 라인의 설명을 갱신하세요.
-- UPDATE productlines
-- SET textDescription = '황태영 짱이다'
-- WHERE productLine = 'Classic Cars'

-- (9) customers 테이블에서 특정 고객의 이메일을 갱신하세요.
-- UPDATE customers
-- SET addressline1 = '황태영이메일레전드'
-- WHERE customerNumber = 112

