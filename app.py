from flask import Flask
from flask import render_template,request
from flask_bootstrap import Bootstrap
from pymongo import MongoClient
import json
from bson import json_util
from bson.json_util import dumps
from threading import Thread
from flask import Response

app = Flask(__name__)
Bootstrap(app)


MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DBS_NAME = 'first1'
COLLECTION_NAME = 'projects'
FIELDS = {'date': True,
'state_ab': True,
'city_or_county': True,
'address': True,
'n_killed': True,
'n_injured': True,
'congressional_district': True ,
'latitude': True ,
'longitude': True ,
'n_guns_involved': True ,
'state_house_district': True ,
'state_senate_district': True ,
'zip_code': True ,
'n_child': True ,
'n_teen': True ,
'n_adult': True ,
'n_child_victim': True ,
'n_teen_victim': True ,
'n_adult_victim': True ,
'n_male': True ,
'n_female': True ,
'n_male_victim': True ,
'n_female_victim': True ,
'_id': False}




static_zip = 90001

@app.route("/")
def home():
    return render_template("home.html")



@app.route("/first1/projects")
def firset_projects():
    connection = MongoClient(MONGODB_HOST,MONGODB_PORT)
    collection = connection[DBS_NAME][COLLECTION_NAME]
    projects = collection.find(projection=FIELDS,limit = 240000)
    json_projects = []
    for project in projects:
        json_projects.append(project)
    json_projects = json.dumps(json_projects, default=json_util.default)
    connection.close()
    return json_projects

# test aggragation
@app.route("/first1/zipfilter",methods = ['POST','GET'])
def zipfilter():
        result = request.form
        static_zip = result['Area']
        static_zip=int(static_zip)
        print(" i am in json")
        print(static_zip)
        connection = MongoClient(MONGODB_HOST,MONGODB_PORT)
        collection = connection[DBS_NAME][COLLECTION_NAME]
        projects = collection.aggregate([{'$match':{"zip_code":static_zip}}]);
        json_projects = []
        for project in projects:
            json_projects.append(project)
        json_projects = json.dumps(json_projects, default=json_util.default)
        connection.close()
        return json_projects
# test aggragation

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/result",methods = ['POST','GET'])
def result():
    if request.method == 'POST':
        result = request.form
        print('test')
    return render_template("result.html",result = result)




if __name__ == "__main__":
    app.run(debug=True)
