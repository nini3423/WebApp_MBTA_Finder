from flask import Flask, redirect, request, render_template

from mbta_finder import find_stop_near

app = Flask(__name__)

@app.route("/")
def landingPage():
    return render_template("index.html")

@app.route("/find", methods=['GET', 'POST'])
def getPlaces():
    # modify this function so it renders different templates for POST and GET method.
    # aka. it displays the form when the method is 'GET'; it displays the results when
    # the method is 'POST' and the data is correctly processed.
    if request.method == 'POST':
        place = request.form["place"]
        route_type = request.form["route_type"]
        station_name, wheelchair_boarding = find_stop_near(place, route_type)
        if station_name:
            return render_template(
                "result.html", place=place, route_type=route_type, station_name=station_name, wheelchair_boarding=wheelchair_boarding
                )
        else:
            return render_template("input_form.html", error=True)
    return render_template("input_form.html", error=None)
            
@app.errorhandler(404)
def pageNotFound(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

