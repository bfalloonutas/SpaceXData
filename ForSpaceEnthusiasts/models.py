from django.db import models
import json

# Create your models here.

class Launch(models.Model):
    id = models.CharField(primary_key=True)
    links = models.JSONField( null=True)
    date_unix = models.DateTimeField(null=True)
    window = models.IntegerField(null=True, blank=True)
    rocket = models.CharField(null=True)
    success = models.BooleanField(null=True)
    failures = models.JSONField(null=True)
    details = models.CharField(max_length=1000, null=True)
    flight_number = models.IntegerField(default=0)
    name = models.CharField()
    cores = models.JSONField(null=True)


""" class Crews(models.Model):
    flight id FK
    crew id FK


 """

""" class Payload(models.Model)
    launch id FK
 """