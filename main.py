from flask import Flask, render_template

app = Flask(__name__)

#lowercase letters so that the filter can capitalize them
troops = ["Pikeman", "Horse archer", "Crossbowman", "Militia"]


@app.route("/app/views/templates/")
def index():
    return render_template("index.html")

@app.route("/app/views/templates/hobby1")
def hobby1():
    return render_template("hobby1.html")

@app.route("/app/views/templates/hobby2")
def hobby2():
    return render_template("hobby2.html")

@app.route("/app/views/templates/hobby3")
def hobby3():
    return render_template("hobby3.html")

@app.route("/app/views/templates/troop")
def troop():
    return render_template("troop.html", troopList = troops)




if __name__=='__main__':
    app.run(debug=True)
