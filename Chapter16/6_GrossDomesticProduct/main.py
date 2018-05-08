import pygal
import preprocessing

country_name, country_code, gdp = preprocessing.parse_data('gdp.json', 2010)

worldmap_chart = pygal.maps.world.World()
worldmap_chart.title = 'GDP in 2016'

data = dict((country_code[i], gdp[i]) for i in range(len(country_code)))
worldmap_chart.add('test', data)

worldmap_chart.render_to_file('test.svg')