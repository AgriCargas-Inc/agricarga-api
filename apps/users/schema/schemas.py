from datetime import datetime
from ninja import Schema

class UserSchemaInp(Schema):
    name: str
    email: str
    phone: str
    user_type: str
    password: str
    
class UserSchemaOut(Schema):
    id: str
    email: str
    phone: str
    name: str

class Message(Schema):
    message: str