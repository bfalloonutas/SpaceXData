from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home, name='Home'),
    path('Launches/', views.Launches.as_view(), name="Launches"),
    path('Crews/', views.Crews.as_view(), name="Crews"),
    path('Payloads/', views.Payloads.as_view(), name="Payloads")
]
