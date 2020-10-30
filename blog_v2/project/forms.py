from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,TextAreaField
from wtforms.validators import DataRequired,Email

class login_form(FlaskForm):
    username = StringField(label='Username',validators=[DataRequired()])
    password = PasswordField(label ='Password',validators=[DataRequired()])
    submit = SubmitField(label='Login')

class SignupForm(FlaskForm):
    username = StringField(label ='Username',validators=[DataRequired()])
    password = PasswordField(label='Password',validators =[DataRequired()])
    email = StringField(label ='Email',validators=[DataRequired(),Email()])
    submit = SubmitField(label='Sign up')

class new_post(FlaskForm):
    content = TextAreaField(label="Post content", validators=[DataRequired()])
    title = StringField(label='Title',validators=[DataRequired()])
    submit = SubmitField(label="Post")
