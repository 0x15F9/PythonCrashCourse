class Employee():
    def __init__(self, first_name, last_name, annual_salary):
        """Class modelling an employee"""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
    def give_raise(self, amount=None):
        """Increase the annual salary of an employee. default = 5000"""
        if amount==None:
            self.annual_salary += 5000
        else:
            self.annual_salary += amount
        