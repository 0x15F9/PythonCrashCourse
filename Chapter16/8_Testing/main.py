import pygal
from preprocessing import get_data, sortListToDicts

year = 2014
filename = 'YouthLiteracyRate.csv'
wm = pygal.maps.world.World()
wm.title = 'Literacy rate, youth total (% of people ages 15-24)'
country_name, country_code, data = get_data(filename, year)
no_data, less_than_50, less_than_75, more_than_75 = sortListToDicts(country_code, data)

wm.add("No data", no_data)
wm.add("< 50%", less_than_50)
wm.add("< 75%", less_than_75)
wm.add("> 75 %", more_than_75)

wm.render_to_file('test.svg')