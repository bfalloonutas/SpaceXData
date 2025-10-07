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

class Crew(models.Model):
    id = models.CharField(primary_key=True)
    name = models.CharField()
    agency = models.CharField()
    image = models.CharField(null=True, blank=True)
    wikipedia = models.URLField(null=True, blank=True)
    launches = models.JSONField()
    status = models.CharField() 
    
class Payload(models.Model):
        id = models.CharField(primary_key=True)
        dragon = models.JSONField()
        name = models.CharField()
        type = models.CharField()
        reused = models.BooleanField()
        launch = models.CharField()
        customers = models.JSONField()
        norad_ids = models.JSONField()
        nationalities = models.JSONField()
        manufacturers = models.JSONField()
        mass_kg = models.FloatField(null=True, blank=True)
        mass_lbs = models.FloatField(null=True, blank=True)
        orbit = models.CharField(null=True, blank=True)  
        reference_system = models.CharField(null=True, blank=True)
        regime  = models.CharField(null=True, blank=True)
        longitude = models.FloatField(null=True, blank=True)
        semi_major_axis_km = models.FloatField(null=True, blank=True)
        eccentricity = models.FloatField(null=True, blank=True)
        periapsis_km = models.FloatField(null=True, blank=True)
        apoapsis_km = models.FloatField(null=True, blank=True)
        inclination_deg = models.FloatField(null=True, blank=True)
        period_min = models.FloatField(null=True, blank=True)
        lifespan_years = models.FloatField(null=True, blank=True)
        epoch = models.DateTimeField(null=True, blank=True)
        mean_motion = models.FloatField(null=True, blank=True)
        raan = models.FloatField(null=True, blank=True)
        arg_of_pericenter = models.FloatField(null=True, blank=True)
        mean_anomaly = models.IntegerField(null=True, blank=True)
        
""" s Crew_Launch(models.Model):
    flight id FK
    crew id FK """





""" class Payload(models.Model)
    launch id FK
 """