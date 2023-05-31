# To import the Flask dependency:
from flask import Flask

# import is datetime, NumPy, and Pandas
import datetime as dt
import numpy as np
import pandas as pd

# the dependencies we need for SQLAlchemy, which will help us access our data in the SQLite database
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#  add the code to import the dependencies that we need for Flask. You'll import these right after your SQLAlchemy dependencies
from flask import Flask, jsonify

# Create a new Flask app instance. 
# "Instance" is a general term in programming to refer to a singular version of something.
app = Flask(__name__)

# Create Flask Routes
# First, we need to define the starting point, also known as the root. To do this, we'll use the function @app.route('/').
@app.route('/')

# The forward slash inside of the app.route denotes that we want to put our data at the root of our routes. The forward slash is commonly known as the highest level of hierarchy in any computer system.

# reate a function called hello_world(). Whenever you make a route in Flask, you put the code you want in that specific route below @app.route().
@app.route('/')
def hello_world():
    return 'Hello world'

# Run a Flask App
# To run the app, we're first going to need to use the command line to navigate to the folder where we've saved our code. To run the app, we're first going to need to use the command line to navigate to the folder where we've saved our code
set FLASK_APP=app.py
flask run

# Set Up the Flask Weather App
# Add dependencies to the top

# Set up Database
engine = create_engine("sqlite:///hawaii.sqlite")

# The create_engine() function allows us to access and query our SQLite database file. Now let's reflect the database into our classes.
Base = automap_base()

# Add the following code to reflect the database:
Base.prepare(engine, reflect=True)

# With the database reflected, we can save our references to each table. Again, they'll be the same references as the ones we wrote earlier in this module. We'll create a variable for each of the classes so that we can reference them later, as shown below.
Measurement = Base.classes.measurement
Station = Base.classes.station

# create a session link from Python to our database with the following code:
session = Session(engine)


# Set up Flask
app = Flask(__name__)


# Create the welcome route
# define the welcome route:
@app.route("/")

# create a function welcome() with a return statement
def welcome():
    return

# add the precipitation, stations, tobs, and temp routes that we'll need for this module into our return statement. We'll use f-strings to display them for our investors:
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

flask run

# Precipitation Route
@app.route("/api/v1.0/precipitation")

# Next, we will create the precipitation() function.
def precipitation():
    # add the line of code that calculates the date one year ago from the most recent date in the database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # write a query to get the date and precipitation for the previous year
    precipitation = session.query(Measurement.date, Measurement.prcp).\
       filter(Measurement.date >= prev_year).all()
    # create a dictionary with the date as the key and the precipitation as the value. To do this, we will "jsonify" our dictionary. Jsonify() is a function that converts the dictionary to a JSON file
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

# Stations Route
# return a list of all the stations
# Begin by defining the route and route name
@app.route("/api/v1.0/stations")

# With the route defined, create a new function called stations()
def stations():
    # create a query that will allow us to get all of the stations in our database
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)
    
# Monthly Temperature Route
# the goal is to return the temperature observations for the previous year
@app.route("/api/v1.0/tobs")

# Create a function called temp_monthly() 
def temp_monthly():
    # calculate the date one year ago from the last date in the database.
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # query the primary station for all the temperature observations from the previous year.
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# Statistics Route
# Investors will need to see the minimum, maximum, and average temperatures.
# route will be to report on the minimum, average, and maximum temperatures
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# Create a function called stats() to put our code in.
# Add parameters to our stats()function: a start parameter and an end parameter. 
def stats(start=None, end=None):
    #  create a query to select the minimum, average, and maximum temperatures from our SQLite database. We'll start by just creating a list called sel
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps=temps)
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)

flask run