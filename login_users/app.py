from flask import Flask, request, session, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash,check_password_hash
from project import db, app, login_manager
from flask_login import login_user, logout_user, login_required
from project.forms import RegistrationForm, LoginForm
from project.models import User

#home page route
@app.route('/')
def index():
    return render_template('home.html')

#login page route
@app.route('/login',methods=['GET','POST'])
def login_usr():
    form = LoginForm()#login form object
    if form.validate_on_submit():#if form validates on pressing submit
        user_login = User.query.filter_by(username=form.username.data).first() #retrieve the entry for the user from the database
        if user_login is not None and user_login.check_user(form.password.data): #if the entry is not empty and the passwords match
                    login_user(user_login) #login the user
                    session['username'] = user_login.username
                    flash('logged in Successfully')
                    return redirect(url_for('welcome')) #redirect to welcome page
        else: #if the entry is empty or passwords do not match
                flash('Login Failed username and password do not match')
                return redirect(url_for('login_usr')) #redirect to login page
    return render_template('login.html',form=form)

#logout route requires login
@app.route('/logout')
@login_required
def logout():
    logout_user() #logout the user
    return render_template('home.html') #render home page

#route to welcome page
@app.route('/welcome')
@login_required
def welcome():
    return render_template('welcome.html') #render welcome

#route to the registration page
@app.route('/Register',methods=['GET','POST'])
def register():
    form = RegistrationForm() #registration form object
    if form.validate_on_submit(): #if form is valid on submit
        if User.query.filter_by(username=form.username.data).first(): #query the the User table filtered by username if entry exists
            flash('Username already in use') #flash username already in use
            return redirect(url_for('register'))#redirect to registration page
        elif User.query.filter_by(email=form.email.data).first(): #else query the user table filtered by email id if entry exists
            flash("Email already in use")#flash email already in use
            return redirect(url_for('register'))#redirect to registration page
        else: #if the entry doesn't exist
            new_user = User(username=form.username.data, email=form.email.data, password = form.password.data) #create a new entry
            db.session.add(new_user) #add it to the table
            db.session.commit()#commit
            flash("Successfully Registered You may now Login")
            return redirect(url_for('login_usr'))#redirect to the login page
    return render_template('register.html',form=form)

if __name__ == "__main__":
    app.run(debug=True)
