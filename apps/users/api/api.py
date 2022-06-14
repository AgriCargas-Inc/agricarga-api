from ninja import NinjaAPI
from ninja.responses import codes_4xx


api = NinjaAPI()


@api.get("/")
def home(request):
    return "welcome"