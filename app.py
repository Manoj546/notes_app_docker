from flask import Flask, render_template, request, redirect
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os
load_dotenv()

class Database:
    def __init__(self, app):
        app.config['MONGO_URI'] = os.getenv("DATABASE_URL")
        self.mongo = PyMongo(app)
        self.app = app  # Store the Flask app as an attribute

# Create an instance of the Database class
db = Database(Flask(__name__))
from Model.todoModel import TodoModel

# Create an instance of the TodoModel class
todo_model = TodoModel(db)
app = db.app  # Access the Flask app from the Database instance


@app.route('/tasks', methods=['POST'])
def create_task():
    description = request.form['description']
    category = request.form['category']
    due_date = request.form['date']

    todo_model.create_task(description, category, due_date)
    return redirect('/')

@app.route('/')
def index():
    try:
        # Fetch tasks from the database
        tasks = todo_model.get_tasks()

        # Define category colors
        categoryColors = {
            'Personal': 'rgb(179, 59, 209)',
            'Work': 'rgb(23, 162, 184)',
            'School': 'rgb(255, 193, 7)',
            'College': 'rgb(108, 117, 125)',
            'Office': 'rgb(40, 167, 69)',
        }

        # Render the template with tasks and categoryColors
        return render_template('index.html', tasks=tasks, categoryColors=categoryColors)
    except Exception as e:
        # Handle exceptions appropriately
        print(str(e))
        return render_template('index.html', tasks=[], categoryColors={})

# web.py
def delete_tasks():
    try:
        task_ids = request.form.getlist('taskIds')

        for task_id in task_ids:
            todo_model.delete_by_id(task_id)
            
        return redirect('/')
    except Exception as e:
        print(f"Error deleting tasks: {str(e)}")
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
