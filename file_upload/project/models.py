#import the db object from __init__
from project import db

class data(db.Model):#table named data
    id = db.Column(db.Integer,primary_key=True)#id is the primary key
    photo = db.Column(db.String)#photo column to store names of the photos

    def __init__(self,photo):
        self.photo = photo
