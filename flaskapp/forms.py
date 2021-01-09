from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskapp.db_models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', [DataRequired(), Length(min = 2, max = 17)])
    email = StringField('Email',[DataRequired(), Email() ])
    password = PasswordField('Password',[DataRequired(), Length(min = 6)])
    confirm_password = PasswordField('Confirm Password',[DataRequired(), Length(min = 6), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("That user name is already taken!")

    def validate_email(self,email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError("That email is already taken!")


class LoginForm(FlaskForm):
    username = StringField('Username', [DataRequired(), Length(min = 2, max = 17)])
    email = StringField('Email',[DataRequired(), Email() ])
    password = PasswordField('Password',[DataRequired(), Length(min = 6)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign in')
