#Flask imports
from flask import Flask
from flask_sqlalchemy import  SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)

base = os.path.abspath(os.path.dirname(__file__)) #getting the base path
UPLOAD_FOLDER = base+"/static" #path for upload folder

app.config['SECRET_KEY'] = 'ab' #secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(base,'databse.sqlite') #database uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False 
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER #setting the upload folder for the app

db = SQLAlchemy(app)#sqlalcemy object
Migrate(app,db)
