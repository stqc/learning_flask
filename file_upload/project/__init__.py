from flask import Flask, render_template,request
from flask_sqlalchemy import  SQLAlchemy
from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from wtforms import SubmitField
from flask_migrate import Migrate
import os

app = Flask(__name__)

base = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = base+"/static"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


app.config['SECRET_KEY'] = 'ab'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(base,'databse.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = SQLAlchemy(app)
Migrate(app,db)
