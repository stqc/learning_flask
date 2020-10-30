import os
from PIL import Image
from flask import url_for,current_app

def add_profile(pic,username):
    filename = pic.filename
    ext = filename.split('.')[-1]
    username = str(username)+'.'+ext

    filepath = os.path.join(current_app.root_path,'static',username) #root of the current app

    output_size =(200,200)

    pic = Image.open(pic)
    pic.thumbnail(filepath)

    return username
