# import necessary libraries
from flask import (
    Flask,
    render_template,
    jsonify,
    request)

import pandas as pd

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sql:///db/db.project_db.sql"

db = SQLAlchemy(app)

class gdpplot(db.Model):
    __tablename__="gdpplot"

    year = db.Column(db.text)
    eugdp = db.Column(db.float)
    eapgdp = db.Column(db.float)
    lacgdp = db.Column(db.float)
    nagdp = db.Columnn(db.float)
    megdp = db.Columnn(db.float)
    ssagdp = db.Column(db.float)
 

    def __repr__(self):
       return '<gdpplot%r>' % (self.name)





@app.route("/")
def index():
    return render_template("index.html")

#This will be our welcome page


@app.route("/line_data_route1")
def line_data_function ():
    results = db.session.query(gdpplot.year,gdpplot.eugdp)


#ONE FOR EACH LINE
#If each one is in a row, then we can to create a list of years and values
#Are years in the SQL?

    trace = {
        "x": year,
        "y": gdp,
        "type": line
    }
    return jsonify(trace)




@app.route("/line_data_route2")
def line_data_function ():
    line_data = db.session.query(gdpplot.year, gdpplot.eapgdp)
    
    trace = {
        "x": year,
        "y": gdp,
        "type": "line"
    }
    return jsonify(trace)   

@app.route("/line_data_route3")
def line_data_function ():
    line_data = db.session.query(gdpplot.year, gdpplot.lacgdp)
    
    trace = {
        "x": year,
        "y": gdp,
        "type": "line"
    }
    return jsonify(trace)   


#@app.route("/scatter_data_route")
#def scatter_data_function ():

    #scatter_data = db.session.query()
    #scatter_data = [{
   #     "x": GDP,
   #     "y": life_expectancy
   #     "type": "scatter"}

#return jsonify(trace)

@app.route("/map_data_route")
def line_data_function ():
    map_data = [{
        "x": [1,2,3,4],
        "y": [2,4,6,8]}]

    return jsonify(map_data)


@app.route("/world_map")
def worldmap():
    return render_template("world_map.html")


@app.route("/line_graphs")
def line_graphs():
    return render_template("line_graphs.html")


@app.route("/scatter_plot")
def scatter_plot():
    return render_template("scatter_plot.html")



if __name__ == "__main__":
    app.run(debug=True)