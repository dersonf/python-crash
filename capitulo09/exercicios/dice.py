#!/usr/bin/python3
from random import randint


class Dice:
    """Choice a number as a dice."""

    def __init__(self, sides=6):
        """Initialize the dice attribute."""
        self.sides = sides

    def roll_dice(self):
        """Choice a number in dice."""
        number = randint(1, self.sides)
        print(number)


if __name__ == '__main__':
    print("A dice with 6 sides.")
    for count in range(1, 11):
        numero = Dice()
        numero.roll_dice()

    print("A dice with 10 sides.")
    for count in range(1, 11):
        numero = Dice(10)
        numero.roll_dice()

    print("A dice with 20 sides.")
    for count in range(1, 11):
        numero = Dice(20)
        numero.roll_dice()
