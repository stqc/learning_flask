#required imports
from flask import Flask, render_template,request
from project.models import data
from project import app,db
import os
from PIL import Image

#route to the main page
@app.route('/',methods=["GET","POST"])
def index():
    img = data.query.all() #fetch all images stored in the database
    if request.method == "POST": #when the upload button on the form is submitted
        file = request.files['pic'] #retrieve the file selected in the file field
        pic =Image.open(file)#open the image with PIL
        pic.thumbnail((200,200))#resize to 200x200
        pic.save(os.path.join(app.config['UPLOAD_FOLDER'],file.filename)) #save the image to the upload folder path
        db.session.add(data(file.filename))#add the image name to the database
        db.session.commit()#commit

    return render_template('home.html',image=img)

if __name__ == '__main__':
    app.run(debug=True)
