from flask import Blueprint
from user.model import User
userApp = Blueprint('collab_app_user', __name__)

from bson import json_util
import json

@userApp.route('/user/signup', methods=['POST'])
def signup():
  print('signup')
  return json.loads(json_util.dumps(User().signup()))

@userApp.route('/user/signout')
def signout():
  return User().signout()

@userApp.route('/user/login', methods=['POST'])
def login():
  return json.loads(json_util.dumps(User().login()))

@userApp.route('/user')
def getUsers():
  return json.loads(json_util.dumps(User().getUsers()))

@userApp.route('/user', methods=['PUT'])
def updateUser():
  return json.loads(json_util.dumps(User().updateUser()))