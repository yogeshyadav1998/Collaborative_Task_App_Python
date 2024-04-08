from flask import Flask, request, jsonify
from user.routes import userApp
from task.routes import taskApp

app = Flask(__name__)
app.secret_key = 'yogesh.yadav.app'
app.register_blueprint(userApp)
app.register_blueprint(taskApp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# @app.before_request
# def authentication():
#     if (request.path != '/user/login') & (request.path != '/user/signup'):
#       if not 'AUTO-AUTH-TASK-APP' in request.cookies:
#           return {"message": "not authenticated"}, 400