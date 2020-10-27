from flask import Flask, render_template,redirect,session,flash,url_for,session,request
from flask_login import login_user,logout_user,login_required
from project import app, db
from project.forms import login_form,SignupForm,new_post
from project.models import Users,post

@app.route('/')
def home():
    return render_template('home.html',ps=post.query.all())

@app.route('/logout')
@login_required
def logout():
    logout_user()
    session['current_user']=''
    return redirect(url_for('home'))

@app.route('/login',methods=['GET',"POST"])
def login():
    form = login_form()
    if form.validate_on_submit():
        username = form.username.data
        password =form.password.data
        userr = Users.query.filter_by(username=username).first()

        if userr is not None and userr.authorize_pass(password):
            print(userr.username)
            print('success')
            login_user(userr)
            session['current_user']=username
            print(session['current_user'])
            return redirect(url_for("home"))
    return render_template('login.html',form=form)

@app.route('/signup',methods=['GET','POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data

        if Users.query.filter_by(username=username).first():
            flash('Username already taken retry')
            return redirect(url_for("signup"))
        elif Users.query.filter_by(email=email).first():
            flash('Email already in use')
            return redirect(url_for("signup"))
        else:
            user_obj = Users(username=username,password=password,email=email)
            db.session.add(user_obj)
            db.session.commit()
            return redirect(url_for("home"))
    return render_template('signup.html',form=form)

@app.route('/dashboard/<username>',methods=['GET','POST'])
@login_required
def dash(username):
    userr=Users.query.filter_by(username=session['current_user']).first()
    pst =post.query.filter_by(author_name=session['current_user']).all()


    return render_template('user_dash.html',usr = userr,pst=pst,username=userr.username)

@app.route('/new_post',methods=["GET","POST"])
@login_required
def write_post():
    form = new_post()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        if post.query.filter_by(Title = title).first():
            flash('Title already in use please choose a different title')
            return redirect(url_for('write_post'))
        else:
            new_post_entry = post(title=title,author_name=session['current_user'],content=content)
            db.session.add(new_post_entry)
            db.session.commit()
            return redirect(url_for('home'))
    return render_template('new_post.html',form=form)

@app.route('/post/<post_title>')
def read_post(post_title):
    the_post = post.query.filter_by(Title=post_title).first()
    return render_template('blog_view.html',le_post = the_post)

@app.route('/delete_post<post_title>')
@login_required
def delete_post(post_title):
    post_to_del = post.query.filter_by(Title=post_title).first()
    db.session.delete(post_to_del)
    db.session.commit()
    return redirect(url_for('dash',username=session['current_user']))



if __name__ =="__main__":
    app.run(debug=True)
