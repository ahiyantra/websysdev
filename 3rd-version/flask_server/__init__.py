
from flask import Flask
from config import config
from flask_server.databases.util_db import db_util
from flask_server.routes.person_routes import person_blueprint
import os

def create_app(config_name='default'):
    app = Flask(__name__, static_folder='../react-client/build') # "static folder" changed from "../client/public" after building react app
    app.config.from_object(config[config_name])
    db_util.init_app(app)
    app.register_blueprint(person_blueprint)
    return app
