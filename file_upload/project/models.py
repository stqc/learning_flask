from flask import Flask, render_template,request
from flask_sqlalchemy import  SQLAlchemy
from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from wtforms import SubmitField
from flask_migrate import Migrate
from project import db
class data(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    photo = db.Column(db.String)

    def __init__(self,photo):
        self.photo = photo
