import unittest
from chapter11.name_function import get_formatted_name


class TestGet_formatted_name(unittest.TestCase):

    def test_get_formatted_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')


if __name__ == '__main__':
    unittest.main()
