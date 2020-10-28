#!/usr/bin/python3

import unittest
from city_functions import city


class CitiesTestCase(unittest.TestCase):
    """Test for 'city_function.py'."""

    def test_city_country(self):
        """Do cities like 'São Paulo, Brasil' work?"""
        output = city('são paulo', 'brasil')
        self.assertEqual(output, 'São Paulo, Brasil')

    def test_city_country_population(self):
        """Do cities like 'Maringa, Brasil - population = 342310' work?"""
        output = city('maringa', 'brasil', 342310)
        self.assertEqual(output, 'Maringa, Brasil - population = 342310')

if __name__ == '__main__':
    unittest.main()
