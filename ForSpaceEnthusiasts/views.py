from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
import requests

# Create your views here.

def Home(request):
    name = print("Hello this is the Home Page, Welcome to my project")
    return HttpResponse(name)


class Launches(generic.ListView):
    template_name = "ForSpaceEnthusiasts/launches.html"
    #Get Json data to override model default
    def get_queryset(self):
        response = requests.get('https://api.spacexdata.com/v5/launches/latest')
        return response.json

class Crews(generic.ListView):
    template_name = "ForSpaceEnthusiasts/crew.html"
    #Get Json data to override model default
    def get_queryset(self):
        response = requests.get('https://api.spacexdata.com/v5/launches/latest')
        return response.json

class Payloads(generic.ListView):
    template_name = "ForSpaceEnthusiasts/payload.html"
        #Get Json data to override model default
    def get_queryset(self):
        response = requests.get('https://api.spacexdata.com/v5/launches/latest')
        return response.json