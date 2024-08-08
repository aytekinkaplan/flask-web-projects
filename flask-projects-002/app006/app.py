from flask import Flask, render_template, session, make_response

app = Flask(__name__, template_folder='templates')
app.secret_key = 'SOME_SECRET_KEY'


@app.route('/')
def index():
    return render_template('index.html', message='Index')


@app.route('/set_data')
def set_data():
    session['name'] = 'Aytekin'
    session['other'] = 'Hello World'
    return render_template('index.html', message='Session data set')


@app.route('/get_data')
def get_data():
    if 'name' in session.keys() and 'other' in session.keys():
        name = session['name']
        other = session['other']
        return render_template('index.html', message=f'Name: {name}, Other: {other}')
    else:
        return render_template('index.html', message='No session data')


@app.route('/clear_session')
def clear_session():
    session.clear()
    return render_template('index.html', message='Session cleared')


@app.route('/set_cookie')
def set_cookie():
    response = make_response(render_template('index.html', message='Cookie set'))
    response.set_cookie('cookie_value', 'cookie_value')
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)
