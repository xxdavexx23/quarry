from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
from dotenv import load_dotenv
# set the bind address to 0.0.0.0
# this will allow the container to be accessed from the host machine

"""
This module sets up a Flask application with SQLAlchemy for ORM, CORS for handling cross-origin requests,
and uses environment variables for configuration. It includes a simple model representing DC Universe heroes
and routes to return greetings and data from the database as JSON responses.

Imports:
    Flask: For creating the Flask application instance.
    jsonify: For formatting responses as JSON.
    SQLAlchemy: For ORM (Object-Relational Mapping) to interact with the database.
    CORS: For handling Cross-Origin Resource Sharing, allowing the API to be accessed from different domains.
    os: For interacting with the operating system, particularly for accessing environment variables.
    load_dotenv: For loading environment variables from a .env file into the application's environment.

Environment Variables:
    FLASK_SECRET_KEY: Used as the secret key in the Flask application configuration.
    DATABASE_URI: Connection string for the database, used in the Flask application configuration.

Models:
    DCUniverse: Represents a table in the database with `id` and `Hero` columns.

Routes:
    '/': Returns a simple greeting.
    '/data': Returns all DC Universe heroes in the database as JSON.

Main:
    The application runs with debugging enabled on a specified host and port.
"""

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

# Initialize Flask application and enable CORS
app = Flask(__name__)
CORS(app)

# Application configuration using environment variables
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with Flask app for ORM
db = SQLAlchemy(app)

class heroes(db.Model):
    """
    A model representing a DC Universe hero.

    Attributes:
        id (int): Unique identifier for each hero, serves as the primary key.
        Hero (str): Name of the hero.

    Methods:
        to_dict: Returns a dictionary representation of the instance, suitable for JSON conversion.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    def to_dict(self):
        """Converts the DCUniverse instance into a dictionary."""
        return {
            'id': self.id,
            'name': self.name
        }

@app.route('/')
def hello_world():
    """Returns a simple greeting."""
    return 'Welcome, World! You have reached the DC Universe API.'

@app.route('/data')
def get_data():
    """Queries all DC Universe heroes from the database and returns them as JSON."""
    all_data = heroes.query.all()
    return jsonify([data.to_dict() for data in all_data])

if __name__ == '__main__':
    # Run the Flask app with debugging enabled, accessible externally
    app.run(debug=True, host='0.0.0.0', port=5000)
