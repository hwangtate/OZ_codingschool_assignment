from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World! This is main page"

@app.route("/about")
def about():
    return "Hello World! This is about page"

@app.route("/user/<int:username>")
def user_profile(username):
    return f"Hello NUM : {username}"

@app.route("/test")
def test():
    response = requests.post("http://127.0.0.1:5000/submit", 'test data')
    return response.text

@app.route("/submit", methods=["POST", "GET", "PUT", "DELETE"])
def submit():
    print(request.method)

    if request.method == "GET":
        print("GET method")

    elif request.method == "POST":
        print("POST method", request.data)

    return ''

if __name__ == '__main__':
    app.run()