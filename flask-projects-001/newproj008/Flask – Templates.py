from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hello/<int:score>')
def hello(score):
    name = "Aytekin"
    return render_template('index.html', score=score, name=name)


if __name__ == '__main__':
    app.run(debug=True)
