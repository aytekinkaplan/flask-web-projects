from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'This is the index page.'


app.add_url_rule('/hello', 'hello', view_func=hello_world)


if __name__ == '__main__':
    app.run(debug=True)
