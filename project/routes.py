from flask import Blueprint
from project.model import Project
projectApp = Blueprint('collab_app_project', __name__)

from bson import json_util
import json

@projectApp.route('/projects')
def getProjects():
    return json.loads(json_util.dumps(Project().getProjects()))

@projectApp.route('/projects', methods=['POST'])
def createProjects():
    return json.loads(json_util.dumps(Project().createProject()))

@projectApp.route('/projects', methods=['PUT'])
def updateProject():
    return json.loads(json_util.dumps(Project().updateProject()))
