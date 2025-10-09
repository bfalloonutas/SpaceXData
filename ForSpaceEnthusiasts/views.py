from django.shortcuts import render
from .models import Launch, Crew, Payload

# Create your views here.

template_base = "ForSpaceEnthusiasts/"

def Home(request):
    template_name = template_base + "home.html"
    context = {"home" : "home page"}
    return render(request, template_name, context)


def Launches(request):
    template_name = template_base + "launches.html"
    #get data from the model ordered by date
    launches = Launch.objects.order_by("-date_unix")
    #pass result to context 
    context = {'launches_list' : launches}
    #ship it off to the template
    return render(request, template_name, context)
        
def Crews(request):
    template_name = template_base + "crew.html"
    #get data from the model
    crews = Crew.objects.order_by("name")
    #pass results to context 
    context = {'crew_list' : crews}
    #ship it off to the template
    return render(request, template_name, context)   

def Payloads(request):
    template_name = template_base + "payload.html"
    #Get data from the model
    payloads = Payload.objects.order_by("name")
    #pass results to context 
    context = {'payload_list' : payloads}
    #ship it off to the template
    return render(request, template_name, context)

    