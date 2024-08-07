from flask import render_template
from app import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/services')
def services():
    return render_template('services.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')


@app.route('/team')
def team():
    return render_template('team.html')


@app.route('/faq')
def faq():
    return render_template('faq.html')
