from flask_restful import Resource, marshal
from app.models import MotionChange
from app import request, db
from app.decorator import jwt_required
from flask_restful import Resource, reqparse
from werkzeug.exceptions import HTTPException


class MotionChangeRouter(Resource):
    
    #@jwt_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str)
        parser.add_argument('content', type=str)
        args = parser.parse_args()
        print(f'{args["id"]},{args["content"]}')
        motionChange = MotionChange(id = args["id"], motionChange = args["content"])
        print(motionChange.to_json())
        loc = db['playpop']['motionChange']
        loc.insert_one(motionChange.to_json())
        try:
            return {"success":motionChange.to_json()},200
        except HTTPException:
            print(HTTPException.description)
            return {"error": "Houve um erro ao tentar processar o seu pedido"}, 500
    
    