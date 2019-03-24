from flask import Flask
from flask import render_template,request
from flask_bootstrap import Bootstrap
from pymongo import MongoClient
import json
from bson import json_util
from bson.json_util import dumps

app = Flask(__name__)
Bootstrap(app)


MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DBS_NAME = 'first1'
COLLECTION_NAME = 'projects'
FIELDS = {'date': True,
'state': True,
'city_or_county': True,
'address': True,
'congressional_district': True,
'latitude': True,
'longitude': True ,
'_id': False}





@app.route("/")
def home():
    return render_template("home.html")



@app.route("/first1/projects")
def firset_projects():
    connection = MongoClient(MONGODB_HOST,MONGODB_PORT)
    collection = connection[DBS_NAME][COLLECTION_NAME]
    projects = collection.find(projection=FIELDS)
    json_projects = []
    for project in projects:
        json_projects.append(project)
    json_projects = json.dumps(json_projects, default=json_util.default)
    connection.close()
    return json_projects

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/result",methods = ['POST','GET'])
def result():
    if request.method == 'POST':
        result = request.form
    return render_template("result.html",result = result)




if __name__ == "__main__":
    app.run(debug=True)
