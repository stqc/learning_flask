from flask import Flask
from werkzeug.security import generate_password_hash,check_password_hash
from project import db,login_manager
from flask_login import UserMixin

#method for LoginManager to retrieve currently logged in user_id
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin): #user table
    id = db.Column(db.Integer,primary_key=True) #primary key id
    email = db.Column(db.String(64),unique=True) # unique email
    username = db.Column(db.String(64),unique=True) # unique username
    password = db.Column(db.String) #password field

    def __init__(self,email,username,password): # email,username and password to be given while creating a new entry
        self.email = email
        self.password = generate_password_hash(password) #password is hashed and stored
        self.username = username

    def check_user(self,passw): #method to check if the entered password is correct (while loging in)
        return check_password_hash(self.password,passw)
