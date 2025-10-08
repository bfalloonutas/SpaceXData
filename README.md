# SpaceXData
Display data from the SpaceX Api

Technologies

request package for api GET requests in python

django-extensions package to allow for scripts to run on the django enviroment

imported datetime to format dates

Imported os for os.path.join(BASE_DIR, 'templates'), to allow navigation of templates in the html for the navbar


Used chatgpt to generate the base of the html and css code for the navbar and containers.

Used chatgpt to generate testing conditions eg. (test_create_payload, test_context_launches etc) for tests.py to help ensure that areas of testing are not missed

Run application 

#1 Enter virtual enviroment or install pip packages from requirements.txt


#2 Check for changes to the models.py, in the project root folder where manage.py is located run the following commands
    python3 manage.py makemigrations
    IF changes detected migrate
    python3 manage.py migrate

#3 Get data from the api
    python3 manage.py runscript populate_FSE_db

#4 Run the server
    python3 manage.py runserver

