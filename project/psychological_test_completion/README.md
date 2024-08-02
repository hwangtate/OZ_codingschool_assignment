```
events {
  worker_connections 1024;
}

http {
  server {
      listen 80;
      server_name _;

      location / {
          proxy_pass http://flaskapp:5000;
          proxy_set_header Host $host;
          proxy_set_header X-Real-IP $remote_addr;
          proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
          proxy_set_header X-Forwarded-Proto $scheme;
      }
  }
}
```
### Nginx.conf파일은 Nginx가 포트 80에서 수신한 요청을 flaskapp:5000에 있는 Flask로 전달하도록 하는 파일입니다.
```
#!/bin/bash

# 데이터베이스 초기화
flask init-db

# Gunicorn으로 Flask 애플리케이션 실행
exec gunicorn -w 4 -b 0.0.0.0:5000 "app:create_app()"
```
### entrypoint.sh 파일은 Flask 애플리케이션의 데이터베이스를 초기화하고, Gunicorn을 사용하여 4개의 워커 프로세스로 Flask 애플리케이션을 실행합니다애플리케이션은 모든 네트워크 인터페이스의 5000번 포트에서 수신 대기합니다
```
from app import create_app

application = create_app()

if __name__ == "__main__":
    application.run()
```
### Flask 애플리케이션을 설정하고 실행하는 스크립트입니다.
```
import logging
from logging.config import fileConfig

from flask import current_app

from alembic import context

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)
logger = logging.getLogger("alembic.env")


def get_engine():
    try:
        # this works with Flask-SQLAlchemy<3 and Alchemical
        return current_app.extensions["migrate"].db.get_engine()
    except (TypeError, AttributeError):
        # this works with Flask-SQLAlchemy>=3
        return current_app.extensions["migrate"].db.engine


def get_engine_url():
    try:
        return get_engine().url.render_as_string(hide_password=False).replace("%", "%%")
    except AttributeError:
        return str(get_engine().url).replace("%", "%%")


# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
config.set_main_option("sqlalchemy.url", get_engine_url())
target_db = current_app.extensions["migrate"].db

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def get_metadata():
    if hasattr(target_db, "metadatas"):
        return target_db.metadatas[None]
    return target_db.metadata


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=get_metadata(), literal_binds=True)

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """

    # this callback is used to prevent an auto-migration from being generated
    # when there are no changes to the schema
    # reference: http://alembic.zzzcomputing.com/en/latest/cookbook.html
    def process_revision_directives(context, revision, directives):
        if getattr(config.cmd_opts, "autogenerate", False):
            script = directives[0]
            if script.upgrade_ops.is_empty():
                directives[:] = []
                logger.info("No changes in schema detected.")

    conf_args = current_app.extensions["migrate"].configure_args
    if conf_args.get("process_revision_directives") is None:
        conf_args["process_revision_directives"] = process_revision_directives

    connectable = get_engine()

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=get_metadata(), **conf_args
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
```
# 위 env.py 파일은...
### 1. 설정 및 로깅 초기화
### 2. 엔진과 엔진 URL 가져오기
### 3. 메타데이터 설정
### 4. 마이그레이션 설정
### 5. 마이그레이션 모드 결정
```
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
```
### database.py 파일은 sqlalchemy 데이터베이스 객체 초기화 및  db 객체는 나중에 플라스크 설정 및 데이터베이스 모델 정의용
```
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
```
### 네 개의 데이터베이스 테이블을 정의 : Participant, Admin, Question, Quiz. 각 테이블은 관련된 데이터를 저장하며 Quiz 테이블은 Participant와 Question 테이블과의 관계를 나타낸다
```
from flask import (
    jsonify,
    render_template,
    request,
    Blueprint,
    redirect,
    url_for,
    flash,
    session,
)
from werkzeug.security import check_password_hash
from .models import Question, Participant, Quiz, Admin
from .database import db
import plotly.express as px
import pandas as pd
import plotly
import json
from sqlalchemy import func, extract
import plotly.graph_objs as go
from plotly.offline import plot
from datetime import datetime
# 'main'이라는 이름의 Blueprint 객체 생성
main = Blueprint("main", __name__)
admin = Blueprint("admin", __name__, url_prefix="/admin/")


@main.route("/", methods=["GET"])
def home():
    # 참여자 정보 입력 페이지를 렌더링합니다.
    return render_template("index.html")


@main.route("/participants", methods=["POST"])
def add_participant():
    data = request.get_json()
    new_participant = Participant(
        name=data["name"], age=data["age"], gender=data["gender"] , created_at=datetime.utcnow()
    )
    db.session.add(new_participant)
    db.session.commit()

    # 리다이렉션 URL과 참여자 ID를 JSON 응답으로 전송
    return jsonify(
        {"redirect": url_for("main.quiz"), "participant_id": new_participant.id}
    )


@main.route("/quiz")
def quiz():
    # 퀴즈 페이지를 렌더링합니다. 참여자 ID 쿠키가 필요합니다.
    participant_id = request.cookies.get("participant_id")
    if not participant_id:
        # 참여자 ID가 없으면, 홈페이지로 리다이렉션합니다.
        return redirect(url_for("main.home"))

    questions = Question.query.all()
    questions_list = [question.content for question in questions]
    return render_template("quiz.html", questions=questions_list)


@main.route("/submit", methods=["POST"])
def submit():
    # 참여자 ID가 필요합니다.
    participant_id = request.cookies.get("participant_id")
    if not participant_id:
        return jsonify({"error": "Participant ID not found"}), 400

    data = request.json
    quizzes = data.get("quizzes", [])

    for quiz in quizzes:
        question_id = quiz.get("question_id")
        chosen_answer = quiz.get("chosen_answer")

        # 새 Quiz 인스턴스 생성
        new_quiz_entry = Quiz(
            participant_id=participant_id,
            question_id=question_id,
            chosen_answer=chosen_answer,
        )
        # 데이터베이스에 추가
        db.session.add(new_quiz_entry)

    # 변경 사항 커밋
    db.session.commit()
    return jsonify(
        {
            "message": "Quiz answers submitted successfully.",
            "redirect": url_for("main.show_results"),
        }
    )


@main.route("/questions")
def get_questions():
    # is_active가 True인 질문만 선택하고, order_num에 따라 정렬
    questions = (
        Question.query.filter(Question.is_active == True)
        .order_by(Question.order_num)
        .all()
    )
    questions_list = [
        {
            "id": question.id,
            "content": question.content,
            "order_num": question.order_num,
        }
        for question in questions
    ]
    return jsonify(questions=questions_list)


@main.route("/results")
def show_results():
    # 데이터베이스에서 데이터 조회
    participants_query = Participant.query.all()
    quizzes_query = Quiz.query.join(Question).all()

    # pandas DataFrame으로 변환
    participants_data = [
        {"age": participant.age, "gender": participant.gender}
        for participant in participants_query
    ]
    quizzes_data = [
        {
            "question_id": quiz.question_id,
            "chosen_answer": quiz.chosen_answer,
            "participant_age": quiz.participant.age,
        }
        for quiz in quizzes_query
    ]

    participants_df = pd.DataFrame(participants_data)
    quizzes_df = pd.DataFrame(quizzes_data)

    # Plotly 시각화 생성
    # 예시 1: 나이별 분포 (도넛 차트)
    fig_age = px.pie(
        participants_df,
        names="age",
        hole=0.3,
        title="Age Distribution",
        color_discrete_sequence=px.colors.sequential.RdBu,
        labels={"age": "Age Group"},
    )
    fig_age.update_traces(textposition="inside", textinfo="percent+label")

    fig_gender = px.pie(
        participants_df,
        names="gender",
        hole=0.3,
        title="Gender Distribution",
        color_discrete_sequence=px.colors.sequential.Purp,
        labels={"gender": "Gender"},
    )
    fig_gender.update_traces(textposition="inside", textinfo="percent+label")

    quiz_response_figs = {}

    # 각 질문 ID별로 반복하여 그래프 생성
    for question_id in quizzes_df["question_id"].unique():
        filtered_df = quizzes_df[quizzes_df["question_id"] == question_id]
        fig = px.histogram(
            filtered_df,
            x="chosen_answer",
            title=f"Question {question_id} Responses",
            color="chosen_answer",
            barmode="group",
            category_orders={"chosen_answer": ["yes", "no"]},  # 카테고리 순서 지정
            color_discrete_map={"yes": "RebeccaPurple", "no": "LightSeaGreen"},
        )  # 컬러 매핑
        fig.update_layout(
            xaxis_title="Chosen Answer",
            yaxis_title="Count",
            plot_bgcolor="rgba(0,0,0,0)",  # 배경색 투명
            paper_bgcolor="rgba(0,0,0,0)",  # 전체 배경색 투명
            font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
            title_font=dict(
                family="Helvetica, Arial, sans-serif", size=22, color="RebeccaPurple"
            ),
        )
        fig.update_traces(marker_line_width=1.5, opacity=0.6)  # 투명도와 테두리 두께 조정

        # 생성된 그래프를 딕셔너리에 저장
        quiz_response_figs[f"question_{question_id}"] = fig
    age_quiz_response_figs = {}

    # 나이대를 구분하는 함수
    def age_group(age):
        if age == 'teenage':
            return "10s"
        elif age == 'twenty':
            return "20s"
        elif age == 'thirty':
            return "30s"
        elif age == 'forty':
            return "40s"
        elif age == 'fifties':
            return "50s"
        else:
            return "60s+"

    # 나이대 그룹 열 추가
    quizzes_df["age_group"] = quizzes_df["participant_age"].apply(age_group)

    # 각 질문 ID와 나이대별로 대답 분포를 시각화
    for question_id in quizzes_df["question_id"].unique():
        filtered_df = quizzes_df[quizzes_df["question_id"] == question_id]
        fig = px.histogram(
            filtered_df,
            x="age_group",
            color="chosen_answer",
            barmode="group",
            title=f"Question {question_id} Responses by Age Group",
            labels={"age_group": "Age Group", "chosen_answer": "Chosen Answer"},
            category_orders={"age_group": ["10s", "20s", "30s", "40s", "50s+"]},
        )

        # 스타일 조정
        fig.update_layout(
            xaxis_title="Age Group",
            yaxis_title="Count",
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
            title_font=dict(
                family="Helvetica, Arial, sans-serif", size=22, color="RebeccaPurple"
            ),
        )
        fig.update_traces(marker_line_width=1.5, opacity=0.6)
        age_quiz_response_figs[f"question_{question_id}"] = fig
    # 딕셔너리에 저장된 그래프들을 JSON으로 변환
    graphs_json = json.dumps(
        {
            "age_distribution": fig_age,
            "gender_distribution": fig_gender,
            "quiz_responses": quiz_response_figs,
            "age_quiz_response_figs": age_quiz_response_figs,
        },
        cls=plotly.utils.PlotlyJSONEncoder,
    )

    # 데이터를 results.html에 전달
    return render_template("results.html", graphs_json=graphs_json)


@admin.route("", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        admin = Admin.query.filter_by(username=username).first()

        if admin and check_password_hash(admin.password, password):
            session["admin_logged_in"] = True
            return redirect(url_for("admin.dashboard"))
        else:
            flash("Invalid username or password")

    return render_template("admin.html")


@admin.route("/logout")
def logout():
    session.pop("admin_logged_in", None)
    return redirect(url_for("admin.login"))


from functools import wraps
from flask import redirect, url_for, session


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "admin_logged_in" not in session:
            return redirect(url_for("admin.login", next=request.url))
        return f(*args, **kwargs)

    return decorated_function


@admin.route("dashboard")
@login_required
def dashboard():
    # 날짜별 참가자 수를 계산
    participant_counts = (
        db.session.query(
            func.date(Participant.created_at).label("date"),
            func.count(Participant.id).label("count"),
        )
        .group_by("date")
        .all()
    )

    # 날짜와 참가자 수를 분리하여 리스트에 저장
    dates = [result.date for result in participant_counts]
    counts = [result.count for result in participant_counts]

    # Plotly 그래프 생성
    graph = go.Figure(go.Scatter(x=dates, y=counts, mode="lines+markers"))

    graph.update_layout(title="일자별 참가자 수", xaxis_title="날짜", yaxis_title="참가자 수")

    # Plotly 그래프를 HTML로 변환
    graph_div = plot(graph, output_type="div", include_plotlyjs=False,config = {'displayModeBar': False})

    # 생성된 HTML을 템플릿으로 전달
    return render_template("dashboard.html", graph_div=graph_div)


@admin.route("/dashboard/question", methods=["GET", "POST"])
@login_required
def manage_questions():
    if request.method == "POST":
        if "new_question" in request.form:
            # 새 질문 추가
            is_active = (
                "is_active" in request.form and request.form["is_active"] == "on"
            )
            new_question = Question(
                content=request.form["content"],
                order_num=request.form["order_num"],
                is_active=is_active,
            )
            db.session.add(new_question)
            db.session.commit()
        else:
            # 기존 질문 수정
            question_id = request.form["question_id"]
            question = Question.query.get(question_id)
            if question:
                is_active = (
                    "is_active" in request.form and request.form["is_active"] == "on"
                )
                question.content = request.form["content"]
                question.order_num = request.form["order_num"]
                question.is_active = is_active
                db.session.commit()

    questions = Question.query.order_by(Question.order_num).all()
    return render_template("manage_questions.html", questions=questions)


@admin.route("/dashboard/list")
@login_required
def quiz_list():
    quizzes = Quiz.query.all()
    return render_template("quiz_list.html", quizzes=quizzes)
```
### main Blueprint: 참가자 정보 입력, 퀴즈 제출, 결과 조회 등을 담당. admin Blueprint: 관리자 로그인/로그아웃, 질문 관리, 대시보드 등 관리 기능을 담당. 데이터베이스 모델: 참가자(Participant), 질문(Question), 퀴즈(Quiz), 관리자(Admin) 모델을 사용하여 데이터베이스 작업 수행. Plotly: 데이터를 시각화하여 결과 페이지와 관리자 대시보드에 그래프 표시. 이 코드는 웹 애플리케이션의 기본 구조와 기능을 명확하게 나누어 관리하고 있으며, Flask와 SQLAlchemy, Plotly를 활용하여 데이터베이스 연동과 데이터 시각화를 구현하고 있습니다.