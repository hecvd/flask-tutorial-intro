from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, EqualTo, Length
from wtforms.fields.html5 import EmailField

class LoginForm(Form):
    email = EmailField('email', validators=[InputRequired(), Email()])
    password = PasswordField('password', [InputRequired(), Length(min=6, max=25)])
    remember_me = BooleanField('remember_me', default=False)

class SignInForm(Form):
    email = EmailField('email', validators=[InputRequired(), Email()])
    password = PasswordField('New Password', [
        InputRequired(),
        EqualTo('confirm', message='Passwords must match'),
        Length(min=6, max=25)
    ])
    confirm = PasswordField('password', validators=[InputRequired()])

class NameForm(Form):
    name = StringField('What is your name?', validators=[InputRequired()])
    submit = SubmitField('Submit')