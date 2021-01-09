from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class  RegistrationForm(FlaskForm):
    username = StringField('Username', [DataRequired(), Length(min = 2, max = 17)])
    email = StringField('Email',[DataRequired(), Email() ])
    password = PasswordField('Password',[DataRequired(), Length(min = 6)])
    confirm_password = PasswordField('Confirm Password',[DataRequired(), Length(min = 6), EqualTo('password')])
    submit = SubmitField('Sign Up')

class  LoginForm(FlaskForm):
    username = StringField('Username', [DataRequired(), Length(min = 2, max = 17)])
    email = StringField('Email',[DataRequired(), Email() ])
    password = PasswordField('Password',[DataRequired(), Length(min = 6)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign in')

