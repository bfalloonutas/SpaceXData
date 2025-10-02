from django.urls import path
from . import views



urlpatterns = [
    path('', views.Home, name='Home'),
    path('launches/', views.Launches, name="Launches"),
    path('crews/', views.Crews, name="Crews"),
    path('payloads/', views.Payloads, name="Payloads")
]
