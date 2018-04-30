import unittest
from city_functions import city_country

class TestCase(unittest.TestCase):
	def setUp(self):
		self.city = "paris"
		self.country = "france"
		self.population = 5000000
		self.expected_output = "Paris, France"
		self.expected_output_1 = "Paris, France - population 5000000"

	def test_city_country(self):
		self.obtained_output = city_country(self.city, self.country)
		self.assertEqual(self.obtained_output, self.expected_output)
	
	def test_city_country_population(self):
		self.obtained_output = city_country(self.city, self.country, self.population)
		self.assertEqual(self.obtained_output, self.expected_output_1)

unittest.main()
