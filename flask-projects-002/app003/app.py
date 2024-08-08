from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    name = "John"
    mylist = ["a", "b", "c", "d"]
    return render_template(template_name_or_list='index.html', name=name, mylist=mylist)


@app.route('/about')
def about():
    return render_template(template_name_or_list='about.html')


@app.route('/contact')
def contact():
    return render_template(template_name_or_list='contact.html')


@app.route('/blog')
def blog():
    return render_template(template_name_or_list='blog.html')


@app.route('/portfolio')
def portfolio():
    return render_template(template_name_or_list='portfolio.html')


@app.route('/services')
def services():
    return render_template(template_name_or_list='services.html')


@app.route('/faq')
def faq():
    warning = "Please use the contact form to get in touch with us. We will get back to you as soon as we can. " \
              "Thank you!"
    return render_template(template_name_or_list='faq.html', warning=warning)


@app.template_filter('reverse_string')
def reverse_string(s):
    return s[::-1]


@app.template_filter('repeat_string')
def repeat_string(s, times=2):
    return s * times


@app.route('/redirect_endpoint')
def redirect_endpoint():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True)
