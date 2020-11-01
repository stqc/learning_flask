from flask import Flask, render_template,request
from project.models import data
from project import app,db
import os
from PIL import Image


@app.route('/',methods=["GET","POST"])
def index():
    img = data.query.all()
    if request.method == "POST":
        file = request.files['pic']
        pic =Image.open(file)
        pic.thumbnail((200,200))
        pic.save(os.path.join(app.config['UPLOAD_FOLDER'],file.filename))
        db.session.add(data(file.filename))
        db.session.commit()


    return render_template('home.html',image=img)

if __name__ == '__main__':
    app.run(debug=True)
