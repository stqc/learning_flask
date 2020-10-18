# all the imports
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)

login_manager = LoginManager(app) #creating a LoginManager object for this app

basepath = os.path.abspath(os.path.dirname(__file__)) #getting the base path of __inti__.py

app.config['SECRET_KEY'] ="Verysupersecretkey" #the super secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basepath,'database.sqlite') #configuring the path to the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) #creating an SQLAlchemy object

Migrate(app=app,db=db) #Migrates for easy update to database

login_manager.login_view ='login_usr'
