# -*- coding: utf-8 -*-
from app import app
from flask import render_template, url_for, flash, redirect
from forms import LoginForm, SignInForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'hector'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'Roy'}, 
            'body': u'Lol hoy me enteré que existe cancún'
        },
        { 
            'author': {'nickname': 'Fru'}, 
            'body': 'Hice CaFru!' 
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for email="%s", password=%s' %
              (form.email.data, str(form.password.data)))
        return redirect('/index')
    return render_template('login.html', title='Log In', form=form)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SignInForm()
    return render_template('signin.html', title='Sign In', form=form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
