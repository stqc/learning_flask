from flask import Flask
from project import app,db,login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)

class Users(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),unique=True)
    password = db.Column(db.String(128))
    email = db.Column(db.String,unique=True)
    posts = db.relationship('post',backref ='author',uselist=True)
    profile_pic = db.Column(db.String,default = "default.png")

    def __init__(self,username,password,email):
        self.username = username
        self.password = generate_password_hash(password)
        self.email = email

    def authorize_pass(self,passw):
        return check_password_hash(self.password,passw)

class post(db.Model):
    __tablename__='post_uploaded'
    id = db.Column(db.Integer,primary_key=True)
    Title = db.Column(db.String(64),unique=True)
    author_name = db.Column(db.String,db.ForeignKey('users.username'))
    content = db.Column(db.String)
    date = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)

    def __init__(self,title,author_name,content):
        self.Title = title
        self.author_name = author_name
        self.content = content
