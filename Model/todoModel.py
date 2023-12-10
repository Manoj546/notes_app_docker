# todoModel.py
from flask_pymongo import pymongo

class TodoModel:
    def __init__(self, db):
        self.tasks = db.mongo.db.task

    def create_task(self, description, category, due_date):
        task = {
            'description': description,
            'category': category,
            'dueDate': due_date
        }
        self.tasks.insert_one(task)

    def get_tasks(self):
        return list(self.tasks.find({}, {'_id': False}))

    def delete_tasks(self, task_ids):
        print(f"Deleting tasks: {task_ids}")
        self.tasks.delete_many({'_id': {'$in': task_ids}})
        
    def delete_by_id(self, task_id):
        print(f"Deleting task: {task_id}")
        self.tasks.delete_one({'_id': task_id})
