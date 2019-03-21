from flask import Flask
from flask import render_template,request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/result",methods = ['POST','GET'])
def result():
    if request.method == 'POST':
        result = request.form
    return render_template("result.html")

if __name__ == "__main__":
    app.run(debug=True)
