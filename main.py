#Project for ria resource. Which will be triger individuals data

import requests
import json
import config


req = requests.get("https://developers.ria.com/auto/categories/" , params={'api_key' : config.api})
req = req.json()
for item in req:
    print(item)
