import os
from flask import Flask, render_template,request,url_for,redirect,session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import upload_form

app = Flask(__name__)
app.config['SECRET_KEY'] ="supersecret"

base = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///'+os.path.join(base,'data.sqlite')


db = SQLAlchemy(app)
Migrate(app,db)

class car(db.Model):
    __tablename__ ='car'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    owner = db.Column(db.Text)
    booked = db.Column(db.Boolean)
    ride = db.relationship('Ride',backref ='cars',uselist=False)


    def __init__(self,id,name,owner,booked):
        self.id = id
        self.name = name
        self.owner = owner
        self.booked = booked

    def __repr__(self):
        if self.ride:
            return f'{self.name} is booked for {self.ride.destination}'
        else:
            return f'{self.name} is avaialable'
    

class Ride(db.Model):
    __tablename__ ='rides'
    id = db.Column(db.Integer,primary_key=True)
    destination = db.Column(db.Text)
    source = db.Column(db.Text)
    car = db.Column(db.Integer,db.ForeignKey('car.id'))

    def __init__(self,destination,source,car):
        self.destination = destination
        self.source = source
        self.car = car

@app.route('/')
def index():
    cars_available = car.query.all()
    return render_template('home.html',cars_available= cars_available)

@app.route('/post_car',methods=['GET','POST'])
def post_car():
    form = upload_form()
    if form.validate_on_submit():
        car1 = car(id=form.car_num.data,owner=form.name.data,name =form.car_model.data,booked=False)
        db.session.add(car1)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('cars.html',form=form)

@app.route('/rent',methods=['GET','POST'])
def rentcar():
    if request.method =='POST':
        r = request.form['car']
        dest = request.form['destination']
        source = request.form['source']
        journey = Ride(destination=dest,source=source,car=r)
        selected_Car = car.query.filter_by(id=r).first()
        selected_Car.booked = True
        db.session.add_all([journey,selected_Car])
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('rent.html',cars_available=car.query.filter_by(booked=False).all())

@app.route('/endride',methods=['GET','POST'])
def ride_end():
    if request.method =='POST':
        try:
            r = request.form['car']
            journey=Ride.query.filter_by(car=r).first()
            session['d']= journey.destination
            session['s'] =journey.source
            db.session.delete(journey)
            c= car.query.filter_by(id=r).first()
            c.booked=False
            db.session.commit()
            return render_template('delete.html')
        except:
            pass

    return render_template('endride.html')


if __name__ == "__main__":
    app.run(debug=True)
