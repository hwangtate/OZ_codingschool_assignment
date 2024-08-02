#!/bin/bash

# 데이터베이스 초기화
flask init-db

# Gunicorn으로 Flask 애플리케이션 실행
exec gunicorn -w 4 -b 0.0.0.0:5000 "app:create_app()"

#Flask 애플리케이션의 데이터베이스를 초기화하고,
#Gunicorn을 사용하여 4개의 워커 프로세스로 Flask 애플리케이션을 실행합니다
#애플리케이션은 모든 네트워크 인터페이스의 5000번 포트에서 수신 대기합니다

