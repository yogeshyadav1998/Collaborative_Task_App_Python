from flask import Flask, request, session, redirect
from mongodb import db

task_schema = {
    'name': str,
    'description': str,
    'manager': str,
    'channel_id': str,
    'developer': str,
    "qa": str
}

class Project:
    def getProjects(self):
        project_filter = request.json
        Tasks = db.projects.find(project_filter)
        return Tasks, 200

    def createProject(self):
        project_data = request.json
        new_project = {}
        for key in task_schema.keys():
            if key in project_data:
                new_project[key] = project_data[key]
        db.projects.insert_one(new_project)
        return {"message": "project created success"}, 201
    
    def updateProject(self):
        project_data = request.json
        db.projects.update_one({"channel_id" : project_data["channel_id"]}, {"$set": project_data})
        return {"message": "project created success"}, 201
