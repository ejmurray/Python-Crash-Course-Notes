import unittest

from chapter11.employee import Employee


class TestEmployee(unittest.TestCase):
    """A class to test that the employee class is working"""

    def setUp(self):
        """Make an employee to use in the main program"""
        self.ernest = Employee('Ernest', 'Murray', 60000)

    def test_give_default_raise(self):
        """Test that the default raise works"""
        self.ernest.give_raise()
        self.assertEqual(self.ernest.salary, 65000)

    def test_custom_raise(self):
        """Test that a raise other than 5000 can be used"""
        self.ernest.give_raise(10000)
        self.assertEqual(self.ernest.salary, 70000)

if __name__ == '__main__':
    unittest.main()
