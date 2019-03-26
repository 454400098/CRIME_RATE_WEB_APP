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
'officer involved incident':True ,
'_id': False}

MONGODB_HOST2 = 'localhost'
MONGODB_PORT2 = 27017
DBS_NAME2 = 'second1'
COLLECTION_NAME2 = 'projects2'
FIELDS2 = {' GEOID '  : True,
' Total Population '  : True,
' Total Male Population '  : True,
' Total Female Population	White - Total Population '  : True,
' White - Total Male Population '  : True,
' White - Total Female Population '  : True,
' African American - Total Population '  : True,
' African American - Total Male Population '  : True,
' African American - Total Female Population '  : True,
' American Indian - Total Population '  : True,
' American Indian - Total Male Population '  : True,
' American Indian - Total Female Population '  : True,
' Asian - Total Population '  : True,
' Asian - Total Male Population '  : True,
' Asian - Total Female Population '  : True,
' Native Hawaiian - Total Population '  : True,
' Native Hawaiian - Total Male Population '  : True,
' Native Hawaiian - Total Female Population '  : True,
' Other Races - Total Population '  : True,
' Other Races - Total Male Population '  : True,
' Other Races - Total Female Population '  : True,
' Two or More Races - Total Population '  : True,
' Two or More Races - Total Male Population '  : True,
' Two or More Races - Total Female Population '  : True,
' Hispanic or Latino - Total Population '  : True,
' Hispanic or Latino - Total Male Population '  : True,
' Hispanic or Latino - Total Female Population '  : True,
' Median Age '  : True,
' Male - Median Age '  : True,
' Female - Median Age '  : True,
' U.S. citizen, born in the United States '  : True,
' U.S. citizen, born in Puerto Rico or U.S. Island Areas '  : True,
' U.S. citizen, born abroad of American parent(s) '  : True,
' U.S. citizen by naturalization '  : True,
' Not a U.S. citizen '  : True,
' Not a citizen - European '  : True,
' Not a citizen - Asian '  : True,
' Not a citizen - African '  : True,
' Not a citizen - Oceania '  : True,
' Not a citizen - Latin America '  : True,
' Not a citizen - North America '  : True,
' No Income '  : True,
' Total Housing Units '  : True,
' Housing Units - Owner occupied '  : True,
' Housing Units - Renter occupied '  : True,
' Median House Value '  : True,
' Lower Quartile House Value '  : True,
' Upper Quartile House Value '  : True,
' Median Household Income '  : True,
' Average Household Income '  : True,
' Total num of families '  : True,
' RATIO OF INCOME TO POVERTY Under .50 '  : True,
' RATIO OF INCOME TO POVERTY 0.50-0.74 '  : True,
' RATIO OF INCOME TO POVERTY 0.75-0.99 '  : True,
' RATIO OF INCOME TO POVERTY 1.0-1.24 '  : True,
' RATIO OF INCOME TO POVERTY 1.24 - 1.49 '  : True,
' RATIO OF INCOME TO POVERTY 1.50 - 1.74 '  : True,
' RATIO OF INCOME TO POVERTY 1.75 - 1.84 '  : True,
' RATIO OF INCOME TO POVERTY 1.85 - 1.99 '  : True,
' RATIO OF INCOME TO POVERTY 2.0 - 2.99 '  : True,
' RATIO OF INCOME TO POVERTY 3.0 - 3.99 '  : True,
' RATIO OF INCOME TO POVERTY 4.0 - 4.99 '  : True,
' RATIO OF INCOME TO POVERTY 5.0 and over '  : True,}



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
	
@app.route("/second1/projects2")
def secset_projects():
    connection = MongoClient(MONGODB_HOST2,MONGODB_PORT2)
    collection = connection[DBS_NAME2][COLLECTION_NAME2]
    projects = collection.find(projection=FIELDS2)
    json_projects = []
    for project in projects:
        json_projects.append(project)
    json_projects = json.dumps(json_projects, default=json_util.default)
    connection.close()
    return json_projects


# test aggragation
@app.route("/first1/zipfilter")
def zipfilter():
    connection = MongoClient(MONGODB_HOST,MONGODB_PORT)
    collection = connection[DBS_NAME][COLLECTION_NAME]
    projects = collection.aggregate([{'$match':{"zip_code":10026}}]);
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

    return render_template("result.html",result = result)




if __name__ == "__main__":
    app.run(debug=True)
