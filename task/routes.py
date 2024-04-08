from flask import Blueprint
from task.model import Task
taskApp = Blueprint('collab_app_task', __name__)

from bson import json_util
import json

@taskApp.route('/tasks')
def getTasks():
  return json.loads(json_util.dumps(Task().getTasks()))

@taskApp.route('/tasks/<task_id>')
def getTask(task_id):
  return json.loads(json_util.dumps(Task().getTask(task_id)))

@taskApp.route('/tasks', methods=['POST'])
def createTasks():
    return Task().createTask()

@taskApp.route('/tasks', methods=['PATCH'])
def filterTasks():
    return Task().filterTask()

@taskApp.route('/tasks/<task_id>', methods=['PUT'])
def updateTask(task_id):
    return Task().updateTask(task_id)

@taskApp.route('/tasks/<task_id>', methods=['DELETE'])
def deleteTask(task_id):
    return Task().deleteTask(task_id)