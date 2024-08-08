from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    name = "John"
    mylist = ["a", "b", "c", "d"]
    return render_template('index.html', name=name, mylist=mylist)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)
