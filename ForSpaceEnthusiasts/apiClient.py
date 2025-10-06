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


payloads = get_data("payloads")

for payload_manufacturers in payloads:
    print(type(payload_manufacturers["manufacturers"]))
    print(payload_manufacturers["manufacturers"])

    







