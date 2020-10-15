#!/usr/bin/python3


class Car:
    """Asimple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attibutes to describe a car."""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Retrn a neatly formatted descripitive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
