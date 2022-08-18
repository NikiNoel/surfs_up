# To import the Flask dependency:
from flask import Flask

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
