class Employee:
    """Collect data of an employee."""

    def __init__(self, first_name, last_name, annual_salary):
        """Store the basic information about employee."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = float(annual_salary)

    def give_raise(self, extramoney=5000):
        """Add money to annual salary."""
        self.annual_salary += extramoney
