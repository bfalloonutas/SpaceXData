from django.shortcuts import render
from .apiClient import get_data
from datetime import datetime

# Create your views here.

template_base = "ForSpaceEnthusiasts/"

def Home(request):
    template_name = template_base + "home.html"
    context = {"home" : "This is the home page"}
    return render(request, template_name, context)


def Launches(request):
    template_name = template_base + "launches.html"
    #get data from the api, pass in the last part of url
    launches = get_data('launches')

    #Sort Launches by date.
    launches_sorted = sorted(launches, key=lambda launch: launch["date_unix"], reverse=True)
    
    #Format dates for publishing
    for launch in launches_sorted:
        get_date = datetime.fromtimestamp(launch["date_unix"])
        format_date = get_date.strftime("%H:%M:%S %d %B %Y ")
        launch["date_unix"] = format_date

        
    #pass results as context as list
    context = {'launches_list' : launches_sorted}
    #ship it off to the template
    return render(request, template_name, context)
        

def Crews(request):
    
    template_name = template_base + "crew.html"
    #get data from the api, pass in the last part of url
    crews = get_data('crew')
    #Sort crew by name,
    crews_sorted = sorted(crews, key=lambda crew: crew["name"])
    #pass results as context as list
    context = {'crew_list' : crews_sorted}
    #ship it off to the template
    return render(request, template_name, context)
    
    
    

def Payloads(request):
    template_name = template_base + "payload.html"
    #get data from the api, pass in the last part of url
    payloads = get_data('payloads')
    #Sort payloads by name
    payloads_sorted = sorted(payloads, key=lambda payload: payload["name"])
    #pass results as context as list
    context = {'payload_list' : payloads_sorted}
    #ship it off to the template
    return render(request, template_name, context)

    