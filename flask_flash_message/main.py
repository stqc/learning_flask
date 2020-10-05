from flask import Flask, redirect, render_template, url_for, session, flash
from forms import records

app = Flask(__name__)

app.config['SECRET_KEY'] ="supersecretkey"

@app.route('/',methods =["GET","POST"])
def index():
    filled = False
    form = records()
    if form.validate_on_submit():
        filled = True
        session['name'] = form.name.data
        flash("Your response has been recorded")
        return redirect(url_for('index'))
    
    return render_template('index.html',filled=filled,form=form)

if __name__ == "__main__":
    app.run(debug=True)
