from ninja import Schema
from django.contrib.auth.backends import ModelBackend, UserModel
from django.db.models import Q

import datetime
from django.conf import settings
from ninja_extra import NinjaExtraAPI
import jwt
from ninja.security import HttpBearer


api = NinjaExtraAPI()


def authenticate_user_django(request, phone=None, password=None, **kwargs):
    try:
        user = UserModel.objects.get(Q(phone__iexact=phone))

    except UserModel.DoesNotExist:
        UserModel().set_password(password)
    except UserModel.MultipleObjectsReturned:

        return UserModel.objects.filter(phone=phone).order_by("id").first()
    else:
        if user.check_password(password):
            return user


class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        try:
            JWT_SIGNING_KEY = getattr(settings, "SECRET_KEY", None)
            return jwt.decode(token, JWT_SIGNING_KEY, algorithms="HS256")

        except jwt.PyJWTError as e:
            return None


def authenticate(request, phone, password):
    try:
        user = authenticate_user_django(
            request=request, phone=phone, password=password
        )
        data = {
            "data": {
                "id": user.id.hex,
                "email": user.email,
                "is_superuser": user.is_superuser,
                "role": user.user_type
            },
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=10),
        }

        JWT_SIGNING_KEY = getattr(settings, "SECRET_KEY", None)
        return jwt.encode(data, JWT_SIGNING_KEY, algorithm="HS256")

    except jwt.PyJWTError as e:
        return None


class AuthSchema(Schema):
    phone: str
    password: str
