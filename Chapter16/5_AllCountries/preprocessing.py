import json
from pygal.maps.world import COUNTRIES

not_found = set()

def country_name_to_code(name):
    try:
        for k, v in COUNTRIES.items():
            if name == v:
                return k
            elif name == 'Iran, Islamic Rep.':
                return 'ir'
            else:
                not_found.add(name)
    except:
        return None

def parse_data(filename, year):
    country_name, country_code, population = [], [], []
    with open(filename) as f:
        data_file =json.load(f)
        for country_data in data_file:
            if country_data["Year"] == str(year):
                country_name.append(country_data["Country Name"])
                country_code.append(country_name_to_code(country_name[-1]))
                population.append(float(country_data["Value"]))
    print(sorted(not_found))
    return(country_name, country_code, population)