#!/usr/bin/python3

import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """Tests for the class Employee."""

    def setUp(self):
        """Create an employee for use in all test methods."""
        self.employee = Employee('Adão', 'Sales', 14000)
        self.default_annual_salary = self.employee.annual_salary

    def test_give_default_raise(self):
        """Test default raise of 5000."""
        # annual_salary = self.employee.annual_salary
        self.employee.give_raise()
        self.assertEqual(self.default_annual_salary + 5000,
                         self.employee.annual_salary)

    def test_give_custom_raise(self):
        """Test custom raise."""
        # annual_salary = self.employee.annual_salary
        raise_value = 10000
        self.employee.give_raise(raise_value)
        self.assertEqual(self.default_annual_salary + raise_value,
                         self.employee.annual_salary)


if __name__ == '__main__':
    unittest.main()
