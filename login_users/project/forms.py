#form class
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,EqualTo,Email
from wtforms import ValidationError
from werkzeug.security import check_password_hash,generate_password_hash
from project.models import User

#registration form
class RegistrationForm(FlaskForm):
    email = StringField(label='Email: ',validators =[DataRequired(),Email()])
    username = StringField(label='Username: ',validators=[DataRequired()])
    password = PasswordField(label='Password: ',validators=[DataRequired(),EqualTo(fieldname='confirm_pass',message='Passwords should match')])
    confirm_pass= PasswordField(label="Confirm password: ",validators=[DataRequired()])
    submit = SubmitField(label='Register')

    def check_email(self):
        if User.query.filter_by(email = self.email.data).first():
            raise ValidationError(message='This Email is already in use')
    def check_username(self):
        if User.query.filter_by(username = self.username.data).first():
            raise ValidationError(message='This Username is already in use')
#login form
class LoginForm(FlaskForm):
    username = StringField(label='Username: ',validators=[DataRequired()])
    password = PasswordField(label='Password: ',validators=[DataRequired()])
    submit= SubmitField(label='Login!')
