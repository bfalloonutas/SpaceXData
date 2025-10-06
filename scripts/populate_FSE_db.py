import requests
import os
import django
from ForSpaceEnthusiasts.apiClient import get_data
from ForSpaceEnthusiasts.models import Launch
from datetime import datetime


def run():
    launches = get_data("launches")

    launch_objects = []
    """ Drop database before loading new date """
    if(Launch.objects.exists()):
        launches = Launch.objects.all()
        launches.delete()
        print("Deleted previous items")

    """ Load data from the api into the database """
    for launch in launches:
        launch_objects.append(Launch(
            id = launch["id"],
            links = launch["links"],
            date_unix = datetime.fromtimestamp(launch["date_unix"]),
            window = launch["window"],
            rocket = launch["rocket"],
            success = launch["success"],
            failures = launch["failures"],
            details = launch["details"],
            flight_number = launch["flight_number"],
            name = launch["name"],
            cores = launch["cores"],)
        )

    Launch.objects.bulk_create(launch_objects)
    print("1")
    