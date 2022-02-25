from flask import render_template
from app import app
from app.forms import LoginForm

user = {'username': 'Benedict'}
posts = [
    {
        'author': {'username': 'John'},
        'body': 'Beautiful day in Portland!'
    },
    {
        'author': {'username': 'Susan'},
        'body': 'The Avengers movie was so cool!'
    }
]

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)