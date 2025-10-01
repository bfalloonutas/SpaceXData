from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .apiClient import get_data
import requests

# Create your views here.

def Home(request):
    name = print("Hello this is the Home Page, Welcome to my project")
    return HttpResponse(name)


def Launches(request):
    template_name = "ForSpaceEnthusiasts/launches.html"
    #get data from the api, pass in the last part of url
    launches = get_data('launches')
    #pass results as context as list
    context = {'launches_list' : launches}
    #ship it off to the template
    return render(request, template_name, context)
        

def Crews(request):
    
    template_name = "ForSpaceEnthusiasts/crew.html"
    #get data from the api, pass in the last part of url
    crews = get_data('crew')
    #pass results as context as list
    context = {'crew_list' : crews}
    #ship it off to the template
    return render(request, template_name, context)
    
    
    

def Payloads(request):
    template_name = "ForSpaceEnthusiasts/payload.html"
    #get data from the api, pass in the last part of url
    payloads = get_data('payloads')
    #pass results as context as list
    context = {'payload_list' : payloads}
    #ship it off to the template
    return render(request, template_name, context)

    