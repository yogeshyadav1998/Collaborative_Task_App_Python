from flask import Flask, request, session, redirect, Response, jsonify
from mongodb import db
import secrets

class User:

  def signup(self):
    userData= request.json
    print(userData)

    # Create the user object
    user = {
      "username": userData['username'],
      "email": userData['email'],
      "password": userData['password'],
      "salt": ''
    }

    # Check for existing email address
    if db.users.find_one({ "email": user['email'] }):
      return { "error": "Email address already in use"}, 400
    
    salt = secrets.token_hex(8)
    user["salt"] = salt
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
      "email": userData['email']
    })

    if user and userData['password'] == user['password']:
      res = Response()
      res.set_cookie('AUTO-AUTH-TASK-APP', user['salt'])
      res.set_data("User logged in")
      return res
    
    return { "error": "Invalid login credentials" }, 401
  
  def getUsers(self):
    users = db.users.find()
    return users, 200