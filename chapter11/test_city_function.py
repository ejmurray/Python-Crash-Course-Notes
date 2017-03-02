import unittest
from chapter11.city_functions import city_functions


class TestCityString(unittest.TestCase):
    """Tests city_function"""

    def test_city_function(self):
        """Test that the function returns the formatted city, country"""
        formatted_city = city_functions('santiago', 'chile')
        self.assertEqual(formatted_city, 'Santiago, Chile.')

    def test_with_population(self):
        """Test the function with a population 0f 5000000"""
        formatted_city = city_functions('santiago', 'chile', 5000000)
        self.assertEqual(formatted_city, 'Santiago, Chile - Population 5000000')

if __name__ == '__main__':
    unittest.main()
