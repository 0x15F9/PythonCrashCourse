import unittest
from employee import Employee

class EmployeeTestCase(unittest.TestCase):
    def setUp(self):
        self.first_name = "Isfaaq"
        self.last_name = "Goomany"
        self.annual_salary = 10000
        self.increment = 10000
    def test_give_default_raise(self):
        self.this_employee = Employee(self.first_name, self.last_name, self.annual_salary)
        self.this_employee.give_raise()
        self.assertEqual(self.this_employee.annual_salary, 15000)
    def test_give_custom_raise(self):
        self.this_employee = Employee(self.first_name, self.last_name, self.annual_salary)
        self.this_employee.give_raise(self.increment)
        self.assertEqual(self.this_employee.annual_salary, 20000)

unittest.main()