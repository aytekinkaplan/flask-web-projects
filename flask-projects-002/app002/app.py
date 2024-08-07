from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index(name):
    myvalue = 'Hello World'
    myresult = 23 * 19
    return render_template('index.html', name='World', myvalue=myvalue, myresult=myresult)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)