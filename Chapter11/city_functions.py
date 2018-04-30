def city_country(city, country, population=None ):
	"""Functions which takes a city name, a country name and its population and returns City, Country - Population"""
	if population==None:
		return "{}, {}".format(city.title(), country.title())
	else:
		return "{}, {} - population {}".format(city.title(), country.title(),population)
