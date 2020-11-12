from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

pet_names =[]

class pet_na(Resource):
    def get(self, name):
        for i in pet_names:
            if i['name']==name:
                return i
        return {'name':None},404

    def post(self,name):
        pet_names.append({'name':name})
        return pet_names

    def delete(self, name):
        for i, nme in enumerate(pet_names):
            if nme['name']==name:
                pet_names.pop(i)
                return {i:nme['name']}

class allnames(Resource):
    def get(self):
        return {'all names':pet_names}

api.add_resource(pet_na,'/<string:name>')
api.add_resource(allnames,'/all/show')
if __name__ == '__main__':
    app.run(debug=True)
