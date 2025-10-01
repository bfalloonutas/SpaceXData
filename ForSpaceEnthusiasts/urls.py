from django.urls import path
from . import views



urlpatterns = [
    path('', views.Home, name='Home'),
    path('Launches/', views.Launches, name="Launches"),
    path('Crews/', views.Crews, name="Crews"),
    path('Payloads/', views.Payloads, name="Payloads")
]
