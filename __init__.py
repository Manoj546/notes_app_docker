from flask import Flask
import os
from flask_pymongo import PyMongo
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self, app):
        app.config['MONGO_URI'] = os.getenv("DATABASE_URL")
        self.mongo = PyMongo(app)

# Create an instance of the Database class
db = Database()

def create_app():
    app = Flask(__name__)
    # Initialize the app with the Database instance
    db.init_app(app)
    app.config['SECRET_KEY'] = 'your_secret_key'
    return app
