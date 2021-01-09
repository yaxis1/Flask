from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '839c91f955762c458c526e67f90a0a68'
app.config['SQLALCHEMY_DB_URL'] = 'sqlite:///site.db'
#Creating instance of database
db=SQLAlchemy(app)

#Circular import
from flaskapp import routes