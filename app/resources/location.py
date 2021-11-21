from flask_restful import Resource
from app.models import Location

from app import request, db
from app.decorator import jwt_required
from flask_restful import Resource, reqparse

class LocationRouter(Resource):
    #@jwt_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str)
        parser.add_argument('content', type=str)
        args = parser.parse_args()
        print(f'{args["id"]},{args["content"]}')
        location = Location(id = args["id"], location = args["content"])
        loc = db['location']
        loc.insert_one(location.to_json())
        try:
            return {"success":location.to_json()}, 200
        except:
            
            return {"error": "Houve um erro ao tentar processar o seu pedido"}, 500
    
    