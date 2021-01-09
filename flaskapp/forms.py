from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
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
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError("That user name is already taken!")

    def validate_email(self,email):
        if email.data != current_user.email:
            email = User.query.filter_by(email=email.data).first()
            if email:
                raise ValidationError("That email is already taken!")

class LoginForm(FlaskForm):
    email = StringField('Email',[DataRequired(), Email() ])
    password = PasswordField('Password',[DataRequired(), Length(min = 6)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign in')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username', [DataRequired(), Length(min = 2, max = 17)])
    email = StringField('Email',[DataRequired(), Email() ])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','png','jpeg'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is already taken!')

    def validate_email(self, email):
            if email.data != current_user.email:
                user = User.query.filter_by(email=email.data).first()
                if user:
                    raise ValidationError('That email is already taken!')