# todoModel.py
from flask_pymongo import pymongo
from bson import ObjectId

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
        return list(self.tasks.find({}, {'_id': True, 'description': True, 'category': True, 'dueDate': True}))

    def delete_tasks(self, task_ids):
        self.tasks.delete_many({'_id': {'$in': task_ids}})
        

    def delete_by_id(self, task_id):
        print(f"Deleting task: {task_id}")
        self.tasks.delete_one({'_id': ObjectId(task_id)})

    def update_task(self, task_id, description, category, due_date):
        query = {'_id': ObjectId(task_id)}
        update_data = {'$set': {'description': description, 'category': category, 'dueDate': due_date}}
        self.tasks.update_one(query, update_data)