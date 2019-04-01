from flask import Flask
from flask import render_template,request,jsonify
from flask_bootstrap import Bootstrap
from pymongo import MongoClient
from bson import json_util
from bson.json_util import dumps
from threading import Thread
from flask import Response
import json
import os
import csv
import os.path
import time

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
'n_male_victim':True,
'n_female_victim':True,
'state_ab': True,
'_id': False}



# # ---------zipcode DB init--------------
#
MONGODB_HOST2 = 'localhost'
DBS_NAME2 = 'second'
MONGODB_PORT2 = 27018
COLLECTION_NAME2 = 'projects2'
FIELDS2 = {'Average Household Income':True,
'Average Household Income':True,
'Median House Value':True,
'_id':False}
#
#
#
#
#
#
# # ---------------------------------------
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


@app.route("/test2")
def second_projects():
    connection = MongoClient(MONGODB_HOST2,MONGODB_PORT2)
    collection = connection[DBS_NAME2][COLLECTION_NAME2]
    projects = collection.find(projection=FIELDS2,limit = 240000)
    json_projects = []
    for project in projects:
        json_projects.append(project)
    json_projects = json.dumps(json_projects, default=json_util.default)
    connection.close()
    return json_projects



@app.route("/test")
def test():
    connection = MongoClient(MONGODB_HOST,MONGODB_PORT)
    collection = connection[DBS_NAME][COLLECTION_NAME]
    projects = collection.find({'zip_code':10024})
    json_projects = []
    for project in projects:
        json_projects.append(project)
    json_projects = json.dumps(json_projects, default=json_util.default)
    connection.close()
    return json_projects

# test aggragation
@app.route("/first1/zipfilter",methods = ['POST'])
def zipfilter():
        print('you are in filter!!!!!!')
        result = request.form
        dynamic_zip = result['Area']
        dynamic_zip=int(dynamic_zip)
        connection = MongoClient(MONGODB_HOST,MONGODB_PORT)
        collection = connection[DBS_NAME][COLLECTION_NAME]
        str = 0
        _id = '_id'
        # projects = collection.aggregate([{'$match':{"zip_code":static_zip}}]);
        projects = collection.find({'zip_code':dynamic_zip},{_id:str})      #must mask _id
                                                                            #if not, cannot save to json file, dont know the reason, but this worked

        json_projects = []
        for project in projects:
            json_projects.append(project)

        with open('./static/second/data_new.json', 'w') as fout:
             json.dump(json_projects, fout)

        print('test')
        print('what is the type???',type(json_projects))
        print('what is the type???',json_projects[0])

        connection.close()
        # return json_projects

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
    while not os.path.exists("./static/second/data_new.json"):
        time.sleep(1)
    if os.path.isfile("./static/second/data_new.json"):
        if request.method == 'POST':
            result = request.form
            print('test')

        print('test')
        return render_template("result.html",result = result)


if __name__ == "__main__":
    app.run(debug=True)
