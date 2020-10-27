from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate

app = Flask(__name__)
login_manager =LoginManager(app=app)

basepath = os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY'] ='key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basepath,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app=app )


Migrate(app=app,db=db)

login_manager.login_view ='login'
