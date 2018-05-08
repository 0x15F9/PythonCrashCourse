import json
from pygal.maps.world import COUNTRIES

filename = 'gdp.json'
year = '2010'

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
    country_name, country_code, gdp = [], [], []
    with open(filename) as f:
        raw_data = json.load(f)
        for country_data in raw_data:
            if str(country_data['Year']) == str(year):
                country_name.append(country_data['Country Name'])
                country_code.append(country_name_to_code(country_data['Country Name']))
                gdp.append(country_data['Value'])
    return country_name, country_code, gdp
