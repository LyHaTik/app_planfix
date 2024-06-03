import requests
import json


def renter():
    url = "https://f13.planfix.ru/rest/contact/list"

    payload = json.dumps({
        "offset": 0,
        "pageSize": 100,
        "fields": "id,name",
        "filters": [
            {
                "type": 4008,
                "operator": "equal",
                "value": 11852
            }
            ]
        })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer 4a0364798374b2d52c84177b32e56077'
        }

    response = requests.request("POST", url, headers=headers, data=payload)

    data = eval(response.text)
    renter_list = data['contacts']
    return renter_list