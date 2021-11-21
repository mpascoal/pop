import os
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from pymongo import MongoClient


app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(12)

api = Api(app, prefix="/api/v1")

def get_db():
    client = MongoClient(host="mongodb",
                         port=27017,
                         username="root",
                         password="pass",
                         authSource="admin")
    db = client["playpop"]
    return db

db=get_db()

CORS(app)

from app.resources.auth import LoginRouter, RegisterRouter
api.add_resource(RegisterRouter, "/register")
api.add_resource(LoginRouter, "/login")

from app.resources.location import LocationRouter
api.add_resource(LocationRouter, "/location")

from app.resources.motionChange import MotionChangeRouter
api.add_resource(MotionChangeRouter, "/motionChange")

from app.resources.ping import Ping
api.add_resource(Ping, "/ping")

api.init_app(app)