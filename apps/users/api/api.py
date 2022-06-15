from ninja import NinjaAPI
from typing import List
from ninja.responses import codes_4xx
from apps.users.models import User
from apps.users.schema import schemas as custom_schemas

api = NinjaAPI()


@api.get("/")
def home(request):
    return "welcome"

@api.get("/user", response=List[custom_schemas.UserSchemaInp])
def list_user(request):
    qs = User.objects.all()
    return qs

@api.post("/user", auth=None, response={201: custom_schemas.UserSchemaInp,codes_4xx: custom_schemas.Message})
def create_user(request, payload: custom_schemas.UserSchemaInp):
    result = User.objects.create(**payload.dict())
    print(result)
    print(result.id)
    return 201, {
                 "name": result.name,
                 "email": result.email,
                 "phone": result.phone,
                 "user_type": result.user_type,
                 "password": result.password
                }