from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '839c91f955762c458c526e67f90a0a68'

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


