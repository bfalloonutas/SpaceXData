from ForSpaceEnthusiasts.apiClient import get_data
from ForSpaceEnthusiasts.models import Launch, Crew, Payload
from datetime import datetime

def add_crew_members():
    launches = Launch.objects.all()

    #iterate through the list of all launches
    for launch in launches:
        #Check if list of crew contains crew member
        if(launch.crew_members):
            #interate through the list of crew
            for crew in launch.crew_members:
                #get each crew member object from Crew
                #print(crew)
                crew_member = Crew.objects.get(id=crew)
                
                #add this launch object to crew list of flights
                #To get flight out of crew_member.flights use
                #crew_member.flights.all() || crew_member.flights.get(id=launch-id)
                crew_member.flights.add(launch) 
                           
                
                
        


def run():
    #see if there is a way to get all the data with one api call
    launches = get_data("launches")
    crews = get_data("crew")
    payloads = get_data("payloads")


    launch_objects = []
    crew_objects = []
    payload_objects = []      

    """ Load data from the api into the database """
    #Check if we got data from payload
    if (launches):
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
                cores = launch["cores"],
                crew_members = launch["crew"])
            )
        Launch.objects.bulk_create(launch_objects, ignore_conflicts=True)
        print("Add launch items")
    
    #Check if we got data from payload
    if (crews):
        for crew in crews:
            crew_objects.append(Crew(
                id = crew["id"],
                name = crew["name"],
                agency = crew["agency"],
                image = crew["image"],
                wikipedia = crew["wikipedia"],
                status = crew["status"],
            ))
        Crew.objects.bulk_create(crew_objects, ignore_conflicts=True)
        print("Add crew items")
    #Check if we got data from payload
    if (payloads):
        for payload in payloads:
            payload_objects.append(Payload(
                id = payload["id"],
                dragon = payload["dragon"],
                name = payload["name"],
                type = payload["type"],
                reused = payload["reused"],
                launch = payload["launch"],
                customers = payload["customers"],
                norad_ids = payload["norad_ids"],
                nationalities = payload["nationalities"],
                manufacturers = payload["manufacturers"],
                mass_kg = payload["mass_kg"],
                mass_lbs = payload["mass_lbs"],
                orbit = payload["orbit"],
                reference_system = payload["reference_system"],
                regime  = payload["regime"],
                longitude = payload["longitude"],
                semi_major_axis_km = payload["semi_major_axis_km"],
                eccentricity = payload["eccentricity"],
                periapsis_km = payload["periapsis_km"],
                apoapsis_km = payload["apoapsis_km"],
                inclination_deg = payload["inclination_deg"],
                period_min = payload["period_min"],
                lifespan_years = payload["lifespan_years"],
                epoch = payload["epoch"],
                mean_motion = payload["mean_motion"],
                raan = payload["raan"],
                arg_of_pericenter = payload["arg_of_pericenter"],
                mean_anomaly = payload["mean_anomaly"],
            ))
        Payload.objects.bulk_create(payload_objects, ignore_conflicts=True)
        print("Add payload items")

    
    add_crew_members()



print("Finished script to load data into db")

    
    
    