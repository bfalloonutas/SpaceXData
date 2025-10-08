from django.test import TestCase, Client
from django.urls import reverse
from datetime import datetime
from .apiClient import get_data
from .models import Launch, Payload, Crew

# Create your tests here.

def create_launch(id):
    return Launch.objects.create(
            name="Flight Name",
            id = id,
            success = True,
            date_unix = datetime.fromtimestamp(1143239400)
        )
def create_crew(id):
    return Crew.objects.create(
            name="Bugs Bunny",
            id =id,
            agency = "Looney Tunes",
            launches = []
        )
def create_payload(id):
    return Payload.objects.create(
            id = id,
            dragon = [],
            name="BugsBunny-01",
            type = "cartoon",
            reused = True,
            launch ="1",
            customers = ["children"],
            norad_ids = [30000],
            nationalities=["United States"],
            manufacturers = [],
        )

class LaunchModelTests(TestCase):
    #Test that Launch can create an object with valid variables

        
    def test_create_launch(self):
        launch = create_launch("1")
        self.assertEqual(launch.name, "Flight Name")
        self.assertTrue(launch.success)
        self.assertEqual(launch.id, "1")
        self.assertEqual(launch.date_unix, datetime(2006, 3, 24, 22, 30))

    #test that __str__ returns expected results
    def test_str_method_launch(self):
        launch = create_launch("1")
        expected_string = "Flight Name - 1 - 2006-03-24 22:30:00"

        self.assertEqual(str(launch), expected_string)



class CrewModelTests(TestCase):
    #Test that Crew can create an object with valid variables

    def test_create_crew(self): 
        crew = create_crew("1")
        self.assertEqual(crew.name, "Bugs Bunny")
        self.assertTrue(crew.agency)
    
    #test that __str__ returns expected results
    def test_str_method_crew(self):
        crew = create_crew("1")
        excepted_string = "Bugs Bunny - 1 - Looney Tunes"

        self.assertEqual(str(crew), excepted_string)
        

     
class PayloadModelTests(TestCase):
    #Test that Crew can create an object with valid variables        
    def test_create_payload(self):
        payload = create_payload("1")
        self.assertEqual(payload.name, "BugsBunny-01")
        self.assertEqual(payload.id, "1")
        self.assertTrue(payload.reused, True)
        self.assertEqual(payload.launch, "1")
        self.assertEqual(payload.customers, ["children"])
        self.assertEqual(payload.norad_ids, [30000])
        self.assertEqual(payload.nationalities, ["United States"])
        self.assertEqual(payload.manufacturers, [])
    #test that __str__ returns expected results
    def test_str_method_payload(self):
        payload = create_payload("1")
        excepted_string = "BugsBunny-01 - 1 - cartoon"
        self.assertEqual(str(payload), excepted_string)


    
class APITests(TestCase):
    #Test that we get data back from the api when we have a valid search
    def test_get_data_launch(self):
        json_data = get_data("launches")
        self.assertIsNotNone(json_data)

    def test_get_data_crew(self):
        json_data= get_data("crew")
        self.assertIsNotNone(json_data)

    def test_get_data_payload(self):
        json_data= get_data("payloads")
        self.assertIsNotNone(json_data)

    #Check we get expected output when call to api fails
    #I would expect the same result if the api is unreachable with
    #a valid search query
    def test_data_invalid(self):
        json_data = get_data("launch")
        self.assertEqual(json_data, "Could not fetch data on launch")


class TestLoadData(TestCase):
    #Check that duplicate data is not loaded into the database
    #Set up so that it copies the behaviour of populate_FSE_db script
    def test_dup_data_payload(self):
        payload_object = []
        payload_object.append(Payload(
            id = "1",
            dragon = [],
            name="BugsBunny-01",
            type = "cartoon",
            reused = True,
            launch ="1",
            customers = ["children"],
            norad_ids = [30000],
            nationalities=["United States"],
            manufacturers = []))
        payload_object.append(Payload(
            id = "1",
            dragon = [],
            name="BugsBunny-02",
            type = "cartoon2",
            reused = True,
            launch ="1",
            customers = ["childrens"],
            norad_ids = [40000],
            nationalities=["America"],
            manufacturers = []))
        
        Payload.objects.bulk_create(payload_object, ignore_conflicts=True)

        self.assertEqual(Payload.objects.count(), 1)

    def test_dup_data_launch(self):
        launch_object = []
        launch_object.append(Launch(
            name="Flight Name",
            id = "1",
            success = True,
            date_unix = datetime.fromtimestamp(1143239400)
        ))
        launch_object.append(Launch(
            name="Flight Name",
            id = "1",
            success = True,
            date_unix = datetime.fromtimestamp(1143239400)
        ))

        Launch.objects.bulk_create(launch_object, ignore_conflicts=True)
        self.assertEqual(Launch.objects.count(), 1)

    def test_dup_data_crew(self):
        crew_object = []
        crew_object.append(Crew(
            name="Bugs Bunny",
            id = "1",
            agency = "Looney Tunes",
            launches = []
        ))
        crew_object.append(Crew(
            name="Bugs Bunny",
            id = "1",
            agency = "Looney Tunes",
            launches = []
        ))
        Crew.objects.bulk_create(crew_object, ignore_conflicts=True)
        self.assertEqual(Crew.objects.count(), 1)

class LaunchViewTests(TestCase):
    def setUp(self):
        self.client= Client()

    def test_view_status_launch(self):
        response = self.client.get(reverse('Launches'))        
        self.assertEqual(response.status_code, 200)


    def test_context_no_launches(self):
        response = self.client.get(reverse('Launches'))        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No Launches Found, please try reloading")
    
    def test_context_launches(self):
        launch = create_launch("1")
        response = self.client.get(reverse('Launches'))  
        self.assertQuerySetEqual(
            response.context["launches_list"],
            [launch],
        )      
       

        
"""    
    
    def test_template_launches(self):"""
    
class CrewViewTests(TestCase):
    def test_view_status_crew(self):
        response = self.client.get(reverse('Crews'))       
        self.assertEqual(response.status_code, 200)

    def test_context_no_crew(self):
        response = self.client.get(reverse('Crews')) 
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No Crew Found, please try reloading")      
     
    def text_context_crew(self):
        crew = create_crew("1")
        response = self.client.get(reverse('Crews'))  
        self.assertQuerySetEqual(
            response.context["crew_list"],
            [crew],
        )
    """
    def test_template_crew(self):"""
    
class PayloadViewTests(TestCase):
    def test_view_status_payload(self):
        response = self.client.get(reverse('Payloads'))       
        self.assertEqual(response.status_code, 200)
        crew = create_crew("1")

    def test_context_no_payload(self):
        response = self.client.get(reverse('Payloads')) 
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No payload Found, please try reloading")      
     
    def text_context_payload(self):
        payload = create_payload("1")
        response = self.client.get(reverse('Payloads'))  
        self.assertQuerySetEqual(
            response.context["payload_list"],
            [payload],
        )


