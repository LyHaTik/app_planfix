import requests
import json


def refer():
    url = "https://f13.planfix.com/rest/contact/list"

    payload = json.dumps({
    "offset": 0,
    "pageSize": 100,
    "fields": "id,name,lastname",
    "filters": [
        {
        "type": 4008,
        "operator": "equal",
        "value": 11856
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
    refer_list = data['contacts']
    return refer_list