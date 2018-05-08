import unittest
from preprocessing import country_name_to_code

class CountryTestCase(unittest.TestCase):
    def setUp(self):
        self.country1 = 'Mauritius'
        self.expectedCode1 = 'mu'
        self.country2 = 'Libya'
        self.expectedCode2 = 'ly'
    
    def testMauritius(self):
        obtainedCode = country_name_to_code(self.country1)
        self.assertEqual(obtainedCode, self.expectedCode1)
    def testLibya(self):
        obtainedCode = country_name_to_code(self.country2)
        self.assertEqual(obtainedCode, self.expectedCode2)

unittest.main()