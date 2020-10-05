from form import SignUpForm
from flask import Flask, render_template, url_for, redirect, session, flash

app = Flask(__name__)

app.config['SECRET_KEY'] ="mysecretkey"

@app.route('/',methods=['GET','POST'])
def index():
    form = SignUpForm()

    if form.validate_on_submit():
        session['name'] = form.name.data
        session['password'] = form.password.data
        session['gender'] = form.gender.data
        session['pets'] = form.pets.data
        flash('You have signed up for this awesome website my dude!')
        return redirect(url_for('thanks'))

    return render_template('main.html',form=form)

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

if __name__ == "__main__":
    app.run(debug=True)
