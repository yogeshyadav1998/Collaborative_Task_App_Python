from flask import Flask, request, session, redirect
from app import db

class User:

  def start_session(self):
    session['logged_in'] = 'true'

  def signup(self):
    userData= request.json
    print(userData)

    # Create the user object
    user = {
      "username": userData['username'],
      "email": userData['email'],
      "password": userData['password']
    }

    # Check for existing email address
    if db.users.find_one({ "email": user['email'] }):
      return { "error": "Email address already in use"}, 400

    if db.users.insert_one(user):
      return user, 200

    return { "error": "Signup failed" }, 400
  
  def signout(self):
    if session['logged_in'] == 'true':
      session['logged_in'] = 'false'
      return { "message": "User logout completed" }, 200
    return { "message": "User already logged out" }, 200
  
  def login(self):
    userData= request.json
    user = db.users.find_one({
      "email": userData['email']
    })

    if user and userData['password'] == user['password']:
      self.start_session()
      return { "message": "User login completed" }, 200
    
    return { "error": "Invalid login credentials" }, 401
  
  def getUsers(self):
    users = db.users.find()
    userList = []
    for user in users:
      userList.append(user)
    return userList