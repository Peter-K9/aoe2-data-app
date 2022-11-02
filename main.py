from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

#lowercase letters so that the filter can capitalize them
troops = ["Pikeman", "Horse archer", "Crossbowman", "Militia"]


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hobby1", methods=['GET'] )
def hobby1():
    req = requests.get('https://age-of-empires-2-api.herokuapp.com/api/v1/units')
    #error checking stuff should go here
    
    #data = json.loads(req.content)
    data = req.content
    return render_template("hobby1.html", data=data )

@app.route("/hobby2")
def hobby2():
    return render_template("hobby2.html")

@app.route("/hobby3")
def hobby3():
    return render_template("hobby3.html")

@app.route("/troop")
def troop():
    return render_template("troop.html", troopList = troops)




if __name__=='__main__':
    app.run(debug=True)
