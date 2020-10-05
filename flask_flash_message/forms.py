from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, RadioField, SubmitField
from wtforms.validators import DataRequired

class records(FlaskForm):
    name = StringField(label="Name: ", validators=[DataRequired()])
    species = RadioField(label='Species: ', validators=[DataRequired()], choices=[('Human','Human'),('Cat','Cat'),('Dog','Dog')])
    about = TextAreaField(label ='About yourself: ', validators=[DataRequired()])
    submit = SubmitField(label='Submit')
