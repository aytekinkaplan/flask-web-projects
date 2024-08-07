from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'This is the index page.'


@app.route('/about')
def about():
    return 'This is the about page.'


@app.route('/contact')
def contact():
    return 'This is the contact page.'


@app.route('/hello/<name>')
def hello(name):
    return 'Hello {}'.format(name)


@app.route('/user/<int:id>')
def user(id):
    return 'User {}'.format(id)


if __name__ == '__main__':
    app.run(debug=True)
