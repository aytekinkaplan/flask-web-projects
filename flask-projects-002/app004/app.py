from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route(rule='/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)
