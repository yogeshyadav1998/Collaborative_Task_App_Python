from flask import Flask, request, jsonify
from user.routes import userApp
from task.routes import taskApp
from project.routes import projectApp

app = Flask(__name__)
app.secret_key = 'yogesh.yadav.app'
app.register_blueprint(userApp)
app.register_blueprint(taskApp)
app.register_blueprint(projectApp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

@app.before_request
def authentication():
    if (request.path != '/user/login') & (request.path != '/user/signup'):
        jwt = request.headers.get('bearer-token')
        if not jwt: 
            return {"error": "request not authorized"}