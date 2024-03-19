from flask import Flask, request, jsonify

import dns.resolver
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8']

import pymongo

from bson.json_util import dumps
import json
f = open('config.json')
envVariables = json.load(f)

client = pymongo.MongoClient(envVariables["MONGODB_URL"])

app = Flask(__name__)
app.secret_key = 'yogesh.yadav.app'
# database for hands-on
db = pymongo.database.Database(client, 'test')

from user.model import User
from task.model import Task

@app.route('/user/signup', methods=['POST'])
def signup():
  print('signup')
  return dumps(User().signup())

@app.route('/user/signout')
def signout():
  return User().signout()

@app.route('/user/login', methods=['POST'])
def login():
  return User().login()

@app.route('/users')
def getUsers():
  return dumps(User().getUsers())

@app.route('/tasks')
def getTasks():
  return dumps(Task().getTasks())

@app.route('/tasks', methods=['POST'])
def createTasks():
    return dumps(Task().createTask())

@app.route('/tasks/<task_id>', methods=['PUT'])
def updateTask(task_id):
    return dumps(Task().updateTask(task_id))

@app.route('/tasks/<task_id>', methods=['DELETE'])
def deleteTask(task_id):
    return dumps(Task().deleteTask(task_id))
