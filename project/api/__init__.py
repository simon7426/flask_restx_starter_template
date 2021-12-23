from flask_restx import Api

from project.api.alive import alive_namespace

api = Api(version="1.0", title="Budget Tracker Transaction Service API", doc="/docs")

api.add_namespace(alive_namespace, path="/alive")
