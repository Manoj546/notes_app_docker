from flask import Flask
import os
import importlib

from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os

load_dotenv()

class Database:
    def __init__(self, app):
        app.config['MONGO_URI'] = os.getenv("DATABASE_URL")
        self.mongo = PyMongo(app)
        

db = Database

def create_app():
    app = Flask(__name__)
    db.init_app(app)
    app.config['SECRET_KEY'] = 'your_secret_key'
    return app
