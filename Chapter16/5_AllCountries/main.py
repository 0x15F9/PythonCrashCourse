import pygal
import preprocessing

country_name, country_code, population = preprocessing.parse_data('population_data.json', 2010)

worldmap_chart = pygal.maps.world.World()
worldmap_chart.title = 'Population Count'

data = dict((country_code[i], population[i]) for i in range(len(country_code)))
worldmap_chart.add('test', data)

worldmap_chart.render_to_file('test.svg')