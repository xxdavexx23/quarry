from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
from dotenv import load_dotenv
# set the bind address to 0.0.0.0
# this will allow the container to be accessed from the host machine

load_dotenv()


app = Flask(__name__ )
CORS(app)


# Configuration for MariaDB``
# Format: mysql+pymysql://<username>:<password>@<host>/<dbname>
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI');
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define your models here
class dc_universe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Hero = db.Column(db.String(255))

    def to_dict(self):
        return {
            'id': self.id,
            'hero': self.Hero
        }

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/data')
def get_data():
    all_data = dc_universe.query.all()
    return jsonify([data.to_dict() for data in all_data])

if __name__ == '__main__':
    app.run(debug=True, host='192.168.1.6', port=5000)
