from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os

load_dotenv()

class Database:
    def __init__(self, app):
        app.config['MONGO_URI'] = os.getenv("DATABASE_URL")
        self.mongo = PyMongo(app)
        

db = Database
