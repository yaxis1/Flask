from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flaskapp.config import Config

#Creating instance of database
db=SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.signin'
login_manager.login_message_category = 'info'


#Function to create this app
def create_app(config_class = Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    #Circular import
    from flaskapp.users.routes import users
    app.register_blueprint(users)

    from flaskapp.posts.routes import posts
    app.register_blueprint(posts)

    from flaskapp.main.routes import main
    app.register_blueprint(main)

    return app