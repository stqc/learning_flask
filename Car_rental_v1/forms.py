from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,RadioField
from wtforms.validators import DataRequired
#from car_rental import db,car


class upload_form(FlaskForm):
    name = StringField(label='Owner Name',validators=[DataRequired()])
    car_num = StringField(label='Registration Number', validators=[DataRequired()])
    car_model = StringField(label='Model', validators=[DataRequired()])
    submit = SubmitField(label='Post Car!', validators=[DataRequired()])
