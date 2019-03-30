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
        print(type('zip_code'))
        # projects = collection.aggregate([{'$match':{"zip_code":static_zip}}]);
        projects = collection.find({'zip_code':dynamic_zip},{_id:str})

        json_projects = []
        print('here!!!!!!!')

        # with open('static/second/data_new.json', 'w') as outfile:
        for project in projects:
            json_projects.append(project)

        logic_steps = [{'incident_id': 190037, 'date': '9/12/14', 'state': 'New York', 'city_or_county': 'New York (Manhattan)', 'address': 'Amsterdam Avenue and 82nd Street', 'n_killed': 0, 'n_injured': 2, 'incident_url': 'http://www.gunviolencearchive.org/incident/190037', 'source_url': 'http://www.nydailynews.com/new-york/drunken-state-narcotics-agent-sued-friend-article-1.2535374', 'congressional_district': 10, 'latitude': 40.7851, 'location_description': '', 'longitude': -73.9769, 'n_guns_involved': 1, 'state_house_district': 67, 'state_senate_district': 31, 'zip_code': 10024, 'n_child': 0, 'n_teen': 0, 'n_adult': 3, 'n_child_victim': 0, 'n_teen_victim': 0, 'n_adult_victim': 2, 'n_male': 2, 'n_female': 1, 'n_male_victim': 1, 'n_female_victim': 1, 'suicide': 0, 'suicide - attempt': 0, 'mistaken identity': 0, 'armed robbery': 0, 'school incident': 0, 'accidental shooting': 1, 'hunting accident': 0, 'thought gun was unloaded': 0, 'playing with gun': 0, 'child involvement': 0, 'defensive use': 0, 'officer involved incident': 0, 'spree shooting': 0, 'mass shooting': 0, 'gang involvement': 0, 'drug involvement': 0, 'political violence': 0, 'terrorism involvement': 0, 'hate crime': 0, 'bar club incident': 0, 'drive by': 0, 'home invasion': 0, 'domestic violence': 0, 'sex crime': 0, 'kidnapping': 0, 'under the influence of alcohol/drugs': 1, 'assualt weapon': 0, 'car jacking': 0, 'non aggresive incident': 0, 'road rage': 0, 'unlawful purchase/sale': 0, 'shootout': 0, 'state_ab': 'NY'}, {'incident_id': 205130, 'date': '9/28/14', 'state': 'New York', 'city_or_county': 'Manhattan', 'address': '426 Amsterdam Ave.', 'n_killed': 0, 'n_injured': 0, 'incident_url': 'http://www.gunviolencearchive.org/incident/205130', 'source_url': 'http://newyork.cbslocal.com/2014/10/09/police-search-for-suspect-who-robbed-4-stores-around-manhattan/', 'congressional_district': 10, 'latitude': 40.7842, 'location_description': '', 'longitude': -73.9779, 'n_guns_involved': '', 'state_house_district': 67, 'state_senate_district': 29, 'zip_code': 10024, 'n_child': 0, 'n_teen': 0, 'n_adult': 1, 'n_child_victim': 0, 'n_teen_victim': 0, 'n_adult_victim': 1, 'n_male': 1, 'n_female': 0, 'n_male_victim': 1, 'n_female_victim': 0, 'suicide': 0, 'suicide - attempt': 0, 'mistaken identity': 0, 'armed robbery': 1, 'school incident': 0, 'accidental shooting': 0, 'hunting accident': 0, 'thought gun was unloaded': 0, 'playing with gun': 0, 'child involvement': 0, 'defensive use': 0, 'officer involved incident': 0, 'spree shooting': 0, 'mass shooting': 0, 'gang involvement': 0, 'drug involvement': 0, 'political violence': 0, 'terrorism involvement': 0, 'hate crime': 0, 'bar club incident': 0, 'drive by': 0, 'home invasion': 0, 'domestic violence': 0, 'sex crime': 0, 'kidnapping': 0, 'under the influence of alcohol/drugs': 0, 'assualt weapon': 0, 'car jacking': 0, 'non aggresive incident': 0, 'road rage': 0, 'unlawful purchase/sale': 0, 'shootout': 0, 'state_ab': 'NY'}, {'incident_id': 375086, 'date': '7/16/15', 'state': 'New York', 'city_or_county': 'New York (Manhattan)', 'address': '2441 Broadway', 'n_killed': 0, 'n_injured': 1, 'incident_url': 'http://www.gunviolencearchive.org/incident/375086', 'source_url': 'https://www.dnainfo.com/new-york/20160408/upper-west-side/man-charged-with-attempted-murder-upper-west-side-diner-shooting', 'congressional_district': 10, 'latitude': 40.7912, 'location_description': 'City Diner', 'longitude': -73.9744, 'n_guns_involved': '', 'state_house_district': 67, 'state_senate_district': 31, 'zip_code': 10024, 'n_child': 0, 'n_teen': 0, 'n_adult': 2, 'n_child_victim': 0, 'n_teen_victim': 0, 'n_adult_victim': 1, 'n_male': 2, 'n_female': 0, 'n_male_victim': 1, 'n_female_victim': 0, 'suicide': 0, 'suicide - attempt': 0, 'mistaken identity': 0, 'armed robbery': 0, 'school incident': 0, 'accidental shooting': 0, 'hunting accident': 0, 'thought gun was unloaded': 0, 'playing with gun': 0, 'child involvement': 0, 'defensive use': 0, 'officer involved incident': 0, 'spree shooting': 0, 'mass shooting': 0, 'gang involvement': 0, 'drug involvement': 0, 'political violence': 0, 'terrorism involvement': 0, 'hate crime': 0, 'bar club incident': 0, 'drive by': 0, 'home invasion': 0, 'domestic violence': 0, 'sex crime': 0, 'kidnapping': 0, 'under the influence of alcohol/drugs': 0, 'assualt weapon': 0, 'car jacking': 0, 'non aggresive incident': 0, 'road rage': 0, 'unlawful purchase/sale': 0, 'shootout': 0, 'state_ab': 'NY'}, {'incident_id': 547481, 'date': '4/24/16', 'state': 'New York', 'city_or_county': 'New York (Manhattan)', 'address': 'West 81st Street', 'n_killed': 0, 'n_injured': 0, 'incident_url': 'http://www.gunviolencearchive.org/incident/547481', 'source_url': 'http://abc7ny.com/news/detectives-suspects-follow-man-into-upper-west-side-apartment-rob-him/1307231/', 'congressional_district': 10, 'latitude': 40.7845, 'location_description': '', 'longitude': -73.9774, 'n_guns_involved': '', 'state_house_district': 67, 'state_senate_district': 29, 'zip_code': 10024, 'n_child': 0, 'n_teen': 0, 'n_adult': 3, 'n_child_victim': 0, 'n_teen_victim': 0, 'n_adult_victim': 1, 'n_male': 3, 'n_female': 0, 'n_male_victim': 1, 'n_female_victim': 0, 'suicide': 0, 'suicide - attempt': 0, 'mistaken identity': 0, 'armed robbery': 0, 'school incident': 0, 'accidental shooting': 0, 'hunting accident': 0, 'thought gun was unloaded': 0, 'playing with gun': 0, 'child involvement': 0, 'defensive use': 0, 'officer involved incident': 0, 'spree shooting': 0, 'mass shooting': 0, 'gang involvement': 0, 'drug involvement': 0, 'political violence': 0, 'terrorism involvement': 0, 'hate crime': 0, 'bar club incident': 0, 'drive by': 0, 'home invasion': 1, 'domestic violence': 0, 'sex crime': 0, 'kidnapping': 0, 'under the influence of alcohol/drugs': 0, 'assualt weapon': 0, 'car jacking': 0, 'non aggresive incident': 0, 'road rage': 0, 'unlawful purchase/sale': 0, 'shootout': 0, 'state_ab': 'NY'}, {'incident_id': 580482, 'date': '6/14/16', 'state': 'New York', 'city_or_county': 'New York (Manhattan)', 'address': '2245 Broadway', 'n_killed': 0, 'n_injured': 1, 'incident_url': 'http://www.gunviolencearchive.org/incident/580482', 'source_url': 'http://www.nydailynews.com/new-york/nyc-crime/cops-charge-man-accidentally-shot-leg-zabar-article-1.2674867', 'congressional_district': 10, 'latitude': 40.7851, 'location_description': "Zabar's", 'longitude': -73.9795, 'n_guns_involved': 1, 'state_house_district': 67, 'state_senate_district': 29, 'zip_code': 10024, 'n_child': 0, 'n_teen': 0, 'n_adult': 1, 'n_child_victim': 0, 'n_teen_victim': 0, 'n_adult_victim': 1, 'n_male': 1, 'n_female': 0, 'n_male_victim': 1, 'n_female_victim': 0, 'suicide': 0, 'suicide - attempt': 0, 'mistaken identity': 0, 'armed robbery': 0, 'school incident': 0, 'accidental shooting': 1, 'hunting accident': 0, 'thought gun was unloaded': 0, 'playing with gun': 0, 'child involvement': 0, 'defensive use': 0, 'officer involved incident': 0, 'spree shooting': 0, 'mass shooting': 0, 'gang involvement': 0, 'drug involvement': 0, 'political violence': 0, 'terrorism involvement': 0, 'hate crime': 0, 'bar club incident': 0, 'drive by': 0, 'home invasion': 0, 'domestic violence': 0, 'sex crime': 0, 'kidnapping': 0, 'under the influence of alcohol/drugs': 0, 'assualt weapon': 0, 'car jacking': 0, 'non aggresive incident': 0, 'road rage': 0, 'unlawful purchase/sale': 0, 'shootout': 0, 'state_ab': 'NY'}]
        print(logic_steps)
        print(json_projects)
        # print(json_projects[0])
        # print(json_projects[1])
        # print(json_projects[2])
        # print(json_projects[3])
        # print((len(json_projects))

        print(type(json_projects))
        print('test!!!!!!')
        # output_file = open("./static/second/data_new.json", 'w', encoding='utf-8')
        # with open('outfile.json', 'wb') as fp:
        #     for dict in list:
        #         fp.write(json_projects)


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
