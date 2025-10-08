import requests


def get_data(page):
    base_url = "https://api.spacexdata.com/v4/"
    #class requests.models.Response
    response = requests.get(base_url + page)

    if response.status_code == 200:
        json_data = response.json()
        return json_data
    else:
        return False


    

