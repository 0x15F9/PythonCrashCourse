from random import randint

class Dice():
    """Class definition for creating a die"""
    def __init__(self, sides=6):
        """ Initialize class
        sides -- number of sides in the die
        """
        self.sides = sides

    def roll(self):
        """ Rolls the dice once """
        return randint(1, self.sides)

    def multiroll(self, number):
        """ Rolls the dice repeatedly
        number -- number of times to roll
        """
        result = []
        for num in range(1, number):
            result.append(self.roll())
        return result