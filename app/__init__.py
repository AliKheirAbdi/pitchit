from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)




bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

from app.users.routes import users
from app.pitches.routes import pitches
from app.main.routes import main
app.register_blueprint(users)
app.register_blueprint(pitches)
app.register_blueprint(main)

mail = Mail()

def create_app(config_name):
    app = Flask(__name__)
    #........
    mail.init_app(app)