from flask import Flask
import os
import importlib

module_path = os.environ.get("DATABASE_MODULE_PATH", "Database.db")
database_module = importlib.import_module(module_path)
db = database_module.db

def create_app():
    app = Flask(__name__)
    db.init_app(app)
    app.config['SECRET_KEY'] = 'your_secret_key'
    return app
