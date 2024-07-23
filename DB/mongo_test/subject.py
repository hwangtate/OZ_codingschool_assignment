from pymongo import MongoClient

# def main():
#     """
#     문제 1 : 특정 잘르의 책 찾기
#     :return:
#     """
#     client = MongoClient('mongodb://localhost:27017/')
#     db = client['local']
#     collection = db['books']
#
#     collection.update_many({}, {"$set": {"genre" : "fantasy"}})
#     query = {"genre" : "fantasy"}
#     for doc in collection.find(query):
#          print(doc['title'], doc['author'])

# def main ():
#     """
#     문제 2 감독별 평균 영화 평점 계
#     :return:
#     """
#     client = MongoClient('mongodb://localhost:27017/')
#     db = client['local']
#     collection = db['movies']
#
#     query = [
#         {"$group": {"_id": "$director", "average_rating": {"$avg": "$rating"}}},
#         {"$sort": {"average_rating": -1}}
#     ]
#
#     result = collection.aggregate(query)
#
#     for data in result :
#         print(data)

# def main ():
#     """
#     문제 3 특정 사용자의 최근 행동 조회
#     :return:
#     """
#     client = MongoClient('mongodb://localhost:27017/')
#     db = client['local']
#     collection = db['user_actions']
#
#     query = {"user_id" : 1 }
#
#     result = collection.find(query).sort([("timestamp", -1)]).limit(5)
#
#     for data in result :
#         print(data)

# def main ():
#     """
#     문제 4 출판 연도별 책의 수 계산
#     :return:
#     """
#     client = MongoClient('mongodb://localhost:27017/')
#     db = client['local']
#     collection = db['books']
#
#     query =  [
#         {"$group": {"_id": "$year", "count": {"$sum": 1}}},
#         {"$sort": {"count": -1}}
#     ]
#
#     result = collection.aggregate(query)
#
#     for data in result :
#         print(data)

# def main ():
#     """
#     문제 5 특정 사용자의 행동 유형 업데이트
#     :return:
#     """
#     client = MongoClient('mongodb://localhost:27017/')
#     db = client['local']
#     collection = db['user_actions']
#
#     query = {"user_id" : 1, "action" : "view", "timestamp" : {"$lt" : "datetime(2023, 4, 10)"}}
#     update = {"$set" : {"action" : "seen"}}
#
#     result = collection.update_many(query, update)
#
#     print(f"Updated {result.modified_count} documents.")
#
# if __name__ == "__main__":
#     main()