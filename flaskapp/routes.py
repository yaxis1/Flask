from flask import render_template, url_for, flash, redirect
#Avoding circular import error
from flaskapp import app, db, bcrypt
from flaskapp.forms import RegistrationForm, LoginForm
from flaskapp.db_models import User,Post
from flask_login import login_user

posts = [
    {
        'author': 'Saif',
        'title': 'Vixen',
        'content': 'Stacy Cruz',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Bala',
        'title': 'Blacked',
        'content': 'Tori Black',
        'date_posted': 'April 21, 2018'
    }
]
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/signup", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
       # db.create_all()
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,email = form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created, you can now login!', 'success')
        return redirect(url_for('signin'))
    return render_template('register.html', title = 'Register', form = form)

@app.route("/signin", methods=['GET', 'POST'])
def signin():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user,remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('login unsuccessful :) ','danger')

    return render_template('login.html', title = 'Login', form = form)