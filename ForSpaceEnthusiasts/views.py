from django.shortcuts import render
from .apiClient import get_data


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
    #pass results as context as list
    context = {'launches_list' : launches_sorted}
    #ship it off to the template
    return render(request, template_name, context)
        

def Crews(request):
    
    template_name = template_base + "crew.html"
    #get data from the api, pass in the last part of url
    crews = get_data('crew')
    #pass results as context as list
    context = {'crew_list' : crews}
    #ship it off to the template
    return render(request, template_name, context)
    
    
    

def Payloads(request):
    template_name = template_base + "payload.html"
    #get data from the api, pass in the last part of url
    payloads = get_data('payloads')
    #pass results as context as list
    context = {'payload_list' : payloads}
    #ship it off to the template
    return render(request, template_name, context)

    