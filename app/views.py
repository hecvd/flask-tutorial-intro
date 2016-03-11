from app import app
from flask import render_template, url_for

@app.route('/')
@app.route('/index')
def index():
  user = {'nickname': 'hector'}  # fake user
  posts = [  # fake array of posts
      { 
          'author': {'nickname': 'Coba'}, 
          'body': 'Bajenle 2 rayitas' 
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
