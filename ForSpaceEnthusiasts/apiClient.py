import requests


def get_data(page):
    base_url = "https://api.spacexdata.com/v4/"
    #class requests.models.Response
    response = requests.get(base_url + page)

    #list: response.json()
    print(type(response))

    if response.status_code == 200:
        json_data = response.json()
        print(type(json_data))
        return json_data
    else:
        error_msg = "Could not fetch data on" + page
        return error_msg


launches = get_data('launches')

#Sort Launches by date.
launches_sorted = sorted(launches, key=lambda launch: launch["date_unix"], reverse=True)

    







