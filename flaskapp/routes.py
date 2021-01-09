from flask import render_template, url_for, flash, redirect
#Avoding circular import error
from flaskapp import app
from flaskapp.forms import RegistrationForm, LoginForm
from flaskapp.db_models import User,Post

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
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form = form)

@app.route("/signin", methods=['GET', 'POST'])
def signin():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data  == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('login unsuccessful','danger')
    return render_template('login.html', title = 'Login', form = form)