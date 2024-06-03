import requests
import json
import pprint


def ts():
    url = "https://f13.planfix.com/rest/task/list"

    payload = json.dumps({
        "offset": 0,
        "pageSize": 100,
        "filterId": 6230198,
        "fields": "id,name"
        })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer 4a0364798374b2d52c84177b32e56077'
        }

    response = requests.request("POST", url, headers=headers, data=payload)
    data = response.text
    ts_list = eval(data)
    ts_list = ts_list['tasks']
    return ts_list