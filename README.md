# SpaceXData
A Django project that displays data from the SpaceX API.


# Project Features
- Database Caching
    - Model for Launch, Crew, and Payload.
    - command get_spaceX_data to fetch data from the SpaceX API and saves it to the local database.
    - Views query the local database.

- base
    - hmtl boilerplate for the rest of templates.
    - contains the navigation bar.
- Home Page
    - summary.
- Launch Page
    - details displayed in a individual "card" element.
    -elements sorted by date in the view.
- Crew Page
    - details displayed in a individual "card" element.
    - elements sorted alphabetically by name in the view.
- Payload
    - details displayed in a individual "card" element.
    - elements sorted alphabetically by name in the view.
    

- Technology Stack
    - Built entirely in Python using Django, for clean, maintianable code.
    - uses requests API GET requests.
    - datetime for formatting dates.
    - os for for template path management.

- AI Usage Log
    Primarly used AI as a search engine (eg. *how* do Django views use models).

    Chatgpt to generate base of HTML and CSS for navbar and containers.

    Chatgpt to assist in generate testing cases eg. (`test_create_payload`, `test_context_launches etc`) to ensure proper coverage.

# Setup and Local Execution:
    
1. Enter project root directory

2. Install dependencies
    
    `pip install --upgrade -r requirements.txt`

3. Set up the datebase

    `python3 manage.py makemigrations`
    `python3 manage.py migrate`

4. Fetch data from API

    `python3 manage.py get_spaceX_data`

5. Run the development server

    `python3 manage.py runserver`

Comments

- In the get_spaceX_data command, payloads without an associated launch object are skipped and not add to the database.
- This was done because it appears that Payload has a one-to-many relationship with Launch. Each payload requires a launch object.
- Payloads with invalid or missing launch ids are ignored to ensure database integrity.
