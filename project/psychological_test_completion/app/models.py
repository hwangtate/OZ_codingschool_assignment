from .database import db
from datetime import datetime


class Participant(db.Model):
    __tablename__ = "participant"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))


class Question(db.Model):
    __tablename__ = "question"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255))
    order_num = db.Column(db.Integer, default=0)  
    is_active = db.Column(db.Boolean, default=True)


class Quiz(db.Model):
    __tablename__ = "quiz"
    id = db.Column(db.Integer, primary_key=True)
    participant_id = db.Column(db.Integer, db.ForeignKey("participant.id"))
    question_id = db.Column(db.Integer, db.ForeignKey("question.id"))
    chosen_answer = db.Column(db.String(255))

    participant = db.relationship("Participant", backref="quizzes")
    question = db.relationship("Question", backref="quizzes")

#네 개의 데이터베이스 테이블을 정의 :
# Participant, Admin, Question, Quiz.
# 각 테이블은 관련된 데이터를 저장하며
# Quiz 테이블은 Participant와 Question 테이블과의 관계를 나타낸다