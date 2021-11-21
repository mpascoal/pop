from app import db
from werkzeug.security import generate_password_hash, check_password_hash
import uuid

class User(object):

    username: str
    password: str

    def __init__(self, username, password):
        
        self.username = username
        self.password = generate_password_hash(password)

    def compare_password(self, password):
    
        print(f'{self.password,password}')
        return check_password_hash(self.password, password)
    
    def to_json(self):
        return {
                    "username":self.username,
                    "password":self.password
               }


class Location(object):
    location: str
    id: str

    def __init__(self,id,location):
        self.id = id
        self.location = location  
    def to_json(self):
        return {
                    "id":self.id,
                    "content":self.location
               }

class MotionChange(object):
    id:str
    motionChange:str

    def __init__(self,id,motionChange):
        self.id = id
        self.motionChange = motionChange

    def to_json(self):
        return {
                    "id":self.id,
                    "content":self.motionChange
               }

