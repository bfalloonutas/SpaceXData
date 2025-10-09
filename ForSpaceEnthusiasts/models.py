from django.db import models
import json

# Create your models here.

class Launch(models.Model):
    id = models.CharField(primary_key=True)
    links = models.JSONField( null=True)
    date_unix = models.DateTimeField()
    window = models.IntegerField(null=True)
    rocket = models.CharField(null=True)
    success = models.BooleanField(null=True)
    failures = models.JSONField(null=True)
    details = models.CharField(max_length=1000, null=True)
    flight_number = models.IntegerField()
    name = models.CharField()
    cores = models.JSONField(null=True)
    crew_members = models.JSONField(null=True)

    def __str__(self):
        return f"{self.name} - {self.id} - {self.date_unix.strftime('%Y-%m-%d %H:%M:%S%z')}"

class Crew(models.Model):
    id = models.CharField(primary_key=True)
    name = models.CharField()
    agency = models.CharField()
    image = models.CharField(null=True)
    wikipedia = models.URLField(null=True)
    status = models.CharField(null=True) 
    flights = models.ManyToManyField(Launch)

    def __str__(self):
        return f"{self.name} - {self.id} - {self.agency}"
    
class Payload(models.Model):
        id = models.CharField(primary_key=True)
        dragon = models.JSONField()
        name = models.CharField()
        type = models.CharField()
        reused = models.BooleanField()
        launch = models.ForeignKey(Launch, on_delete=models.CASCADE, related_name="payload")
        customers = models.JSONField()
        norad_ids = models.JSONField()
        nationalities = models.JSONField()
        manufacturers = models.JSONField()
        mass_kg = models.FloatField(null=True)
        mass_lbs = models.FloatField(null=True)
        orbit = models.CharField(null=True)  
        reference_system = models.CharField(null=True)
        regime  = models.CharField(null=True)
        longitude = models.FloatField(null=True)
        semi_major_axis_km = models.FloatField(null=True)
        eccentricity = models.FloatField(null=True)
        periapsis_km = models.FloatField(null=True)
        apoapsis_km = models.FloatField(null=True)
        inclination_deg = models.FloatField(null=True)
        period_min = models.FloatField(null=True)
        lifespan_years = models.FloatField(null=True)
        epoch = models.DateTimeField(null=True)
        mean_motion = models.FloatField(null=True)
        raan = models.FloatField(null=True)
        arg_of_pericenter = models.FloatField(null=True)
        mean_anomaly = models.IntegerField(null=True)

        def __str__(self):
            return f"{self.name} - {self.id} - {self.type}"
    
    
