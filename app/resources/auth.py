import datetime
from os import error

import jwt 
from flask_restful import Resource, reqparse ,marshal

from app import db, request, app
from app.models import User
#from app.schemas import users_fields


class LoginRouter(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str)
        parser.add_argument('password', type=str)
        args = parser.parse_args()

        users = db['user']
        db_user = users.find_one({"username":args['username']})
        print(f"{db_user['username']},{args['password']}")

        user = User(db_user['username'],args['password'])
        if not user or not user.compare_password(args["password"]):
            return {"error": "Credenciais inválida."}, 400

        payload = {
            "id": db_user['username'],
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
        }

        try:
            token = jwt.encode(payload, app.config["SECRET_KEY"])
            return {"token": token}
        except error:
            print(error)
            return {"error": "Houve um erro ao tentar processar o seu pedido"}, 500


class RegisterRouter(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str)
        parser.add_argument('password', type=str)
        args = parser.parse_args()

        username = str(args['username'])
        password = str(args['password'])
        user = User(str(username),str(password))
        try:
            users = db['user']
            users.insert_one(user.to_json())
            return user.to_json() ,200
        except:
            return {"error": "Houve um erro ao tentar processar o seu pedido"}, 500
