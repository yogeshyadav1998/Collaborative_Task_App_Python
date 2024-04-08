from flask import request, Response, jsonify, json
from mongodb import db
import jwt
import datetime

f = open('config.json')
envVariables = json.load(f)

def generate_token(userData):
    # Example payload data to be included in the JWT token
    payload = {
        'username': userData['username'],
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)  # Token expiration time
    }

    # Generate JWT token
    token = jwt.encode(payload, envVariables['SECRET_KEY'], algorithm='HS256')

    # Return the token as response
    return token

class User:

  def signup(self):
    userData= request.json
    print(userData)

    token = generate_token(userData)

    # Create the user object
    user = {
      "username": userData['username'],
      "password": userData['password'],
      "salt": token
    }

    # Check for existing email address
    if db.users.find_one({ "username": user['username'] }):
      return { "error": "User id already in use"}, 400
    
    if db.users.insert_one(user):
      return user, 200

    return { "error": "Signup failed" }, 400
  
  def signout(self):
    if 'AUTO-AUTH-TASK-APP' in request.cookies:
      res = Response()
      res.delete_cookie('AUTO-AUTH-TASK-APP')
      res.set_data("User logged out")
      return res, 200
    return { "message": "User already logged out" }, 200
  
  def login(self):
    userData= request.json
    user = db.users.find_one({
      "username": userData['username']
    })

    if user and userData['password'] == user['password']:
      # res = Response()
      # res.set_cookie('AUTO-AUTH-TASK-APP', user['salt'])
      # res.set_data("User logged in")
      return user
    
    return { "error": "Invalid login credentials" }
  
  def getUsers(self):
    users = db.users.find()
    return users, 200