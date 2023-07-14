from flask import Blueprint

# Create a Blueprint object for the routes
api = Blueprint('api', __name__)

# Import the routes to register them
from routes.routes import *
