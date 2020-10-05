from flask_wtf import FlaskForm
from wtforms import StringField,RadioField,SelectMultipleField,PasswordField,SubmitField
from wtforms.validators import DataRequired

class SignUpForm(FlaskForm):
    name = StringField(label='Username', validators=[DataRequired()])
    password = PasswordField(label='Password', validators = [DataRequired()])
    gender = RadioField(label='Gender',choices =[('Male','Male'),("Female","Female"),
                                                ('Others','Others')])
    pets = SelectMultipleField(label ='Select pets if any',choices=[('None','None'),('Cat','Cat'),
                                                                ('Dog','Dog'),('Others','Others')])
    submit = SubmitField(label='Sign Up!')
