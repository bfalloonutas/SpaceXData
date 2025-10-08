from django.shortcuts import render
from .apiClient import get_data
from .models import Launch, Crew, Payload
from datetime import datetime
# Create your views here.

template_base = "ForSpaceEnthusiasts/"

def Home(request):
    template_name = template_base + "home.html"
    context = {"home" : "This is the home page"}
    return render(request, template_name, context)


def Launches(request):
    template_name = template_base + "launches.html"
    #get data from the model ordered by date
    launches = Launch.objects.order_by("-date_unix")
    #pass results as context 
    context = {'launches_list' : launches}
    #ship it off to the template
    return render(request, template_name, context)
        
def Crews(request):
    template_name = template_base + "crew.html"
    #get data from the model
    crews = Crew.objects.order_by("name")
    #pass results as context as list
    for crew in crews:
        print(crew.flights)
    context = {'crew_list' : crews}
    #ship it off to the template
    return render(request, template_name, context)   

def Payloads(request):
    template_name = template_base + "payload.html"
    #Get data from the model
    payloads = Payload.objects.order_by("name")
    #pass results as context as list
    context = {'payload_list' : payloads}
    #ship it off to the template
    return render(request, template_name, context)

    