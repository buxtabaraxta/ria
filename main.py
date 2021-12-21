# Project for ria resource. Which will be triger individuals data
import sys
import requests
import json
import api

auto_ria_domain = "https://auto.ria.com"
domain_auto = "https://developers.ria.com/auto/search"
category_id = "category_id/1"
category_auto = "categories/1"

request = requests.get("https://developers.ria.com/auto/search",
                       params={'api_key': api.key, 'category_id': 1,
                               "marka_id[0]": 9,
                               "model_id[0]": 33436,
                               "s_yers[0]": 2002,
                               "po_yers[0]": 2002,
                               # "marka_id[1]": 9,
                               # "model_id[1]": 18490,
                               # "s_yers[1]": 2002,
                               # "po_yers[1]": 2005,
                               "abroad": 0,
                               "custom": 0,
                               "auto_repairs": 0,
                               "damage": 0,
                               "countpage": 100, "page": 0})

# Stop if got connect limit
# if request.json().get('additional_params').get('page'):
#     print('catch')
# sys.exit(0)

# print(type(request.json()))
# sys.exit(0)
try:
    if request.json().get('error').get('code'):
        print(request.json().get('error').get('message'))
        sys.exit(0)
except AttributeError:
    print("No connection limit")


def get_url(mark, model):
    return requests.get(f"{domain_auto}/{category_id}/marka_id/{mark}/", params={'api_key': api.key})


def create_json(endpoint, name):
    with open(name + '.json', 'w', encoding='utf-8') as f:
        # f.write(str(endpoint.json())) - working
        f.write(json.dumps(endpoint.json()))


# Runners
file_name = "cars_found/all_bmw_7_2002_2005"
create_json(request, file_name)

# Get ad's ids
ids = []
with open(file_name + ".json", 'r', encoding='utf8') as bmws:
    file_data = json.load(bmws)
    ids = [line for line in file_data['result']['search_result']['ids']]
    # ids = [line for line in file_data['result']['search_result']['ids']]


def find_urgent(ids_list):
    # id19050985 = "https://developers.ria.com/auto/info?api_key=YOUR_API_KEY&auto_id=19050985" -- Example
    for _id in ids_list:
        page = requests.get("https://developers.ria.com/auto/info", params={"api_key": api.key, "auto_id": _id}).json()
        if ('срочно' or 'очень') in str(page['autoData']['description']).lower():
            print(f"{page.get('marka_id')}")
            print(f"{auto_ria_domain}{page.get('linkToView')}")
            print('{:.150}'.format(str(page['autoData']['description'])))


find_urgent(ids)
