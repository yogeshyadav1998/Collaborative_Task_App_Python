from flask import Flask, request, session, redirect
from app import db

task_schema = {
    'id': str,
    'title': str,
    'description': str,
    'status': str,
    'dueDate': str,
    'assigneeUserName': str
}

class Task:
    def getTasks(self):
        Tasks = db.tasks.find()
        return [{**task, "_id": str(task["_id"])} for task in Tasks], 200

    def createTask(self):
        task_data = request.json
        new_task = {}
        for key in task_schema.keys():
            if key in task_data:
                new_task[key] = task_data[key]
        task = db.tasks.insert_one(new_task)
        return {'message': 'Task created successfully'}, 201
    
    def updateTask(self, taskId):
        task_data = request.json
        updated_task = {}
        for key in task_schema.keys():
            if key in task_data:
                updated_task[key] = task_data[key]
        result = db.tasks.update_one({'id': taskId}, {'$set': updated_task})
        if result.modified_count > 0:
            return {'message': 'Task updated successfully'}, 200
        return {'message': 'Task not found'}, 404
    
    def deleteTask(self, taskId):
        result = db.tasks.delete_one({'id': taskId})
        if result.deleted_count > 0:
            return {'message': 'Task deleted successfully'}, 200
        return {'message': 'Task not found'}, 404