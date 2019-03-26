from flask import Flask
from flask import render_template,request
from flask_bootstrap import Bootstrap
from pymongo import MongoClient
from bson import json_util
from bson.json_util import dumps
from threading import Thread
from flask import Response
import json
import os
app = Flask(__name__)
Bootstrap(app)


MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DBS_NAME = 'first1'
COLLECTION_NAME = 'projects1'
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
'Total Population':True,
'n_male_victim':True,
'n_female_victim':True,
'_id': False}



# ---------zipcode DB init--------------
# MONGODB_HOST = 'localhost'
# MONGODB_PORT = 27018
# DBS_NAME2 = 'first1'
# COLLECTION_NAME2 = 'projects2'
# FIELDS = {'Average Household Income':True,
# 'Average Household Income':True,
# 'Median House Value':True,
# '_id':False}






# ---------------------------------------
static_zip = 90001

@app.route("/")
def home():
    return render_template("home.html")
#
# @app.route("/first2/projects2")
# def second_projects():
#     connection = MongoClient(MONGODB_HOST,MONGODB_PORT)
#     collection = connection[DBS_NAME2][COLLECTION_NAME2]
#     projects = collection.find(projection=FIELDS,limit = 240000)
#     json_projects = []
#     for project in projects:
#         json_projects.append(project)
#     json_projects = json.dumps(json_projects, default=json_util.default)
#     connection.close()
#     return json_projects


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
        print('BEFORE DB!!!!')
        connection = MongoClient(MONGODB_HOST,MONGODB_PORT)
        collection = connection[DBS_NAME][COLLECTION_NAME]
        # projects = collection.aggregate([{'$match':{"zip_code":static_zip}}]);
        projects = collection.find({zip_code:90001});
        print('no!!!!!!!!!!!')
        print(projects)
        json_projects = []
        print('here!!!!!!!')
        for project in projects:
            json_projects.append(project)
        json_projects = json.dumps(json_projects, default=json_util.default)
        with open('static/second/data_new.json', 'w') as outfile:
             json.dump(json_projects, outfile)
        connection.close()
        return json_projects
# test aggragation

@app.route("/about")
def about():
    print("delete begin")
    if os.path.exists("./static/second/data_new.json"):
        os.remove("./static/second/data_new.json")
    print("delete stop")
    return render_template("about.html")


@app.route("/result",methods = ['POST','GET'])
def result():
    if request.method == 'POST':
        result = request.form
        print('test')
    print('test')
    return render_template("result.html",result = result)




if __name__ == "__main__":
    app.run(debug=True)
