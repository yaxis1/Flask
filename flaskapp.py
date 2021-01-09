from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLALchemy
from forms import RegistrationForm, LoginForm
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '839c91f955762c458c526e67f90a0a68'
app.config['SQLALCHEMY_DB_URL'] = 'sqlite:///site.db'
db=SQLALchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(17), unique = True, nullable = False)
    email = db.Column(db.String(100), unique = True, nullable = False)
    image_file = db.Column(db.String(20), nullable = False, default = 'default.jpg')
    password = db.Column(db.String(60), nullable = False)
    posts = db.relationship('Post', backref='author', lazy = True)

    def __repr__(self):
        return f"User('{self.username}, {self.email},{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)  
    title = db.Column(db.String(100), nullable = False)
    date_posted = db.Column(db.DateTime(), nullable = False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"







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

if __name__ == '__main__':
    app.run(debug=True)


