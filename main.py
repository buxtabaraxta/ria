# Project for ria resource. Which will be triger individuals data
import sys
import requests
import json
import api

"""
#EXAMPLES
# Example search api request
example_api_search = "https://developers.ria.com/auto/search?api_key=YOUR_API&" \
                       "category_id=1&bodystyle=3&bodystyle=2&marka_id=79&model_id=0&" \
                       "s_yers=2010&po_yers=2010"
                       
# Example search by id
id19050985 = "https://developers.ria.com/auto/info?api_key=YOUR_API_KEY&auto_id=19050985" 

# Work search example
# result = requests.get("https://developers.ria.com/auto/search",
#                       params={'api_key': config.api, 'category_id': 1, "bodystyle": 3, "marka_id": 79,
#                               "model_id": 0, "s_yers": 2010, "po_years": 2010})

"""

domain_auto = "https://developers.ria.com/auto/search"
category_id = "category_id/1"
category_auto = "categories/1"

# mark = "marks"
# model = "models"
# auto = requests.get("https://developers.ria.com/auto/categories/1/marks", params={'api_key': config.api})
# options = requests.get("https://developers.ria.com/auto/categories/1/options", params={'api_key': config.api})
# drives_type = requests.get("https://developers.ria.com/auto/categories/1/drivesType", params={'api_key': config.api})
# bodystyles = requests.get("http://api.auto.ria.com/categories/1/bodystyles", params={'api_key': config.api})
# id31396593 = requests.get(f"{bmw.url}/33436", params={'api_key': config.api})
# audi2000 = requests.get("https://developers.ria.com/auto/categories/1/marks/6/", params={'api_key': config.api})


all_bmw_745_2002 = requests.get("https://developers.ria.com/auto/search",
                                params={'api_key': api.key, 'category_id': 1, "marka_id": 9,
                                        "model_id": 33436, "s_yers": 2002, "po_years": 2002, "abroad": 0, "custom": 1,
                                        "countpage": 30})

bmw_31396593 = f"https://developers.ria.com/auto/info?api_key={api.key}&auto_id=31396593"


def get_url(mark, model):
    return requests.get(f"{domain_auto}/{category_id}/marka_id/{mark}/", params={'api_key': api.key})


# Function generates json file. Takes two parameters (endpoint, str(name of file))
def create_configurator_car_json(endpoint, name):
    with open(name + '.json', 'w', encoding='utf-8') as f:
        # print(endpoint.json()w
        human_redable = dict()
        for rows in endpoint.json():
            human_redable[rows['name']] = rows['value']
        f.write(str(human_redable))


bmw_31396593 = requests.get(bmw_31396593)


def create_json(endpoint, name):
    with open(name + '.json', 'w', encoding='utf-8') as f:
        f.write(str(endpoint.json()))


# Create json with spake two txt files
"""
keys = []
values = []
with open("search_parameters", encoding='utf-8') as file, open("search_parameters_1") as file_1:
    for line in file:
        keys.append(line.rstrip())
    for line in file_1:
        values.append(line.rstrip())

parameters = dict(zip(keys, values))
with open("configurator_car/search_parameters.json", "w", encoding='utf-8') as file_params:
    file_params.write(json.dumps(parameters, ensure_ascii=False))
"""

# create_configurator_car_json(None, None)
create_json(bmw_31396593, "cars_found/bmw_31396593")
