from flask import Flask
from Database.db import db

def create_app():
    app = Flask(__name__)
    db.init_app(app)
    app.config['SECRET_KEY'] = 'your_secret_key'
    return app