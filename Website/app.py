# import necessary libraries
from flask import (
    Flask,
    render_template,
    jsonify,
    request)

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/db.sqlite"

db = SQLAlchemy(app)


@app.route("/")
def index():
    return render_template("index.html")

#This will be our welcome page


@app.route("/line_data_route")
def line_data_function ():
    line_data = [{
        "x": [1,2,3,4],
        "y": [2,4,6,8]}]

    return jsonify(line_data)

@app.route("/scatter_data_route")
def line_data_function ():
    scatter_data = [{
        "x": [1,2,3,4],
        "y": [2,4,6,8]}]

    return jsonify(scatter_data)

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