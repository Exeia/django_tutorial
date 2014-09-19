# Create your views here.
from django.http import HttpResponse

def index():
    return HttpResponse("Rango says Hello World")

