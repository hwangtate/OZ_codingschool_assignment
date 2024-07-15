import mysql.connector
from faker import Faker
import random 

"""
더미 데이터 생성
"""
#데이터 베이스 연결
db_connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '1025',
    database = 'testdatabase'
)

cursor = db_connection.cursor()

#랜덤 유저 데이터 더미 생성
faker = Faker()

for _ in range(100):
    username = faker.user_name()
    email = faker.email()

    sql = "INSERT INTO users(username, email) VALUES(%s, %s)"
    values = (username, email)

    cursor.execute(sql, values)

# 랜덤 주문 데이터 더미 생성
cursor.execute("SELECT user_id FROM users")
valued_user_id = [row[0] for row in cursor.fetchall()]

for _ in range(100):
    user_id = random.choice(valued_user_id)
    product_name = faker.word()
    quantity = random.randint(1, 10)

    sql = "INSERT INTO orders(user_id, product_name, quantity) VALUES(%s, %s, %s)"
    values = (user_id, product_name, quantity)
    cursor.execute(sql, values)


db_connection.commit()
cursor.close
db_connection.close()

