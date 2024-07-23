from pymongo import MongoClient

# MongoDB 서버에 연결
client = MongoClient('mongodb://localhost:27017/')
print(client)

# DB 선택 or 만들기
db = client['example_db']
print(db)

# 콜렌셕 선택 or 만들기
collection = db['example_collection']
print(collection)

#새 문서 삽입
# example_document = {"name" : "Jone", "age" : 30, "city" : "Seoul"}
# collection.insert_one(example_document)

#모든 문서 조회
# for doc in collection.find():
#     print(doc)

#조건에 맞는 문서 조회
# query = {"name" : "Jone"}
# for doc in collection.find(query):
#     print(doc)

#하나의 문서 업데이트
# collection.update_one({"name" : "Jone"}, {"$set" : {"age" : 31}})
# for doc in collection.find():
#      print(doc)

#하나의 문서 삭제
collection.delete_one({"name" : "Jone"})

#콜렉션 삭제
db.drop_collection("example_collection")

client.drop_database("example_db")