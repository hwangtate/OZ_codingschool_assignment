from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    data = {
        'title' : 'Flask Jinja Template',
        'user' : 'taeyeong',
        'is_admin' : True,
        'item_list' : ["itme1", "item2", "item3"]
    }

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)