import pymysql.cursors

# 데이터베이스 연결 설정
connection = pymysql.connect(
    host='127.0.0.1',  # 데이터베이스 서버 주소
    user='root',       # 데이터베이스 사용자 이름
    password='1025',  # 데이터베이스 비밀번호
    db='airbnb',       # 데이터베이스 이름
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

cursor = connection.cursor()

# 1. 새로운 제품 추가: Python 스크립트를 사용하여 'Products' 테이블에 새로운 제품을 추가하세요. 예를 들어, "Python Book"이라는 이름의 제품을 29.99달러 가격으로 추가합니다.
# first_problem = "INSERT INTO Products (productName, price, stockQuantity ) VALUES ('Python Book', 29.99, 100)"
# cursor.execute(first_problem)
# connection.commit()

# 2. 고객 목록 조회: 'Customers' 테이블에서 모든 고객의 정보를 조회하는 Python 스크립트를 작성하세요.
# second_problem = "SELECT * FROM Customers"
# cursor.execute(second_problem)
# customers = cursor.fetchall()
# print(customers)

# 3.제품 재고 업데이트: 제품이 주문될 때마다 'Products' 테이블의 해당 제품의 재고를 감소시키는 Python 스크립트를 작성하세요.
# order = 2
# product_name = 'Common Information'
# third_problem = "UPDATE Products SET stockQuantity = stockQuantity - %d WHERE productName = 'Common Information'"
# cursor.execute(third_problem %order)
# connection.commit() #이렇게 하면 되긴 하는데 뭔가 찜찜합니다

# 4. **고객별 총 주문 금액 계산**: 'Orders' 테이블을 사용하여 각 고객별로 총 주문 금액을 계산하는 Python 스크립트를 작성하세요.
# fourth_problem = "SELECT totalAmount FROM Orders"
# cursor.execute(fourth_problem)
# total_amount = cursor.fetchall()
# for i in total_amount:
#     print(i)

# 5. **고객 이메일 업데이트**: 고객의 이메일 주소를 업데이트하는 Python 스크립트를 작성하세요. 고객 ID를 입력받고, 새로운 이메일 주소로 업데이트합니다.
# fifth_problem = "UPDATE Customers SET email = 'iloveozcoding' WHERE customerID = 1 "
# cursor.execute(fifth_problem)
# connection.commit()

# 6. **주문 취소**: 주문을 취소하는 Python 스크립트를 작성하세요. 주문 ID를 입력받아 해당 주문을 'Orders' 테이블에서 삭제합니다.
# order_id = int(input("주문하실 ID를 입력해주세요."))
# sixth_problem = "DELETE FROM Orders WHERE orderID = %d"
# cursor.execute(sixth_problem %order_id )
# connection.commit()

#7. **특정 제품 검색**: 제품 이름을 기반으로 'Products' 테이블에서 제품을 검색하는 Python 스크립트를 작성하세요.
# search_product = input("검색하실 제품명을 입력해주세요.")
# seventh_problem = "SELECT productName FROM Products WHERE productName = '%s' "
# cursor.execute(seventh_problem %search_product)
# search_result = cursor.fetchone()
# print(search_result)

# 8. **특정 고객의 모든 주문 조회**: 고객 ID를 기반으로 그 고객의 모든 주문을 조회하는 Python 스크립트를 작성하세요.
# search_order = int(input("조회하실 ID를 입력해주세요."))
# eighth_problem = "SELECT * FROM Orders WHERE customerID = %d"
# cursor.execute(eighth_problem %search_order)
# search_order_result = cursor.fetchall()
# print(search_order_result)

# 9. **가장 많이 주문한 고객 찾기**: 'Orders' 테이블을 사용하여 가장 많은 주문을 한 고객을 찾는 Python 스크립트를 작성하세요.
# ninth_problem =  """
# SELECT customerId, COUNT(*) AS orderCount
# FROM Orders
# GROUP BY customerId
# ORDER BY orderCount DESC
# LIMIT 1;
# """
# cursor.execute(ninth_problem)
# result = cursor.fetchone()
# print(result)

connection.close() 