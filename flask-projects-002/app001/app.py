from flask import Flask, render_template, request, make_response

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/hello')
def hello():
    response = make_response()
    response.status_code = 202
    response.headers['Content-Type'] = 'text/plain'
    response.set_cookie('key', 'value')
    return response

@app.route('/helloworld', methods=['GET', 'POST'])
def helloworld():
    if request.method == 'GET':
        return "You made a GET request\n"
    elif request.method == 'POST':
        return "You made a POST request\n"
    else:
        return 'You made an unknown request\n'


@app.route('/greet/<name>')
def greet(name):
    return f'Hello {name}'


@app.route('/handle_url_params')
def handle_params():
    if 'greeting' in request.args and 'name' in request.args:
        greeting = request.args['greeting']
        name = request.args.get('name')
        return f'{greeting}, {name}'
    else:
        return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)
