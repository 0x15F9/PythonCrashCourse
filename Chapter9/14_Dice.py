from random import randint

class Die:
    def __init__(self, sides=None):
        if sides is None:
            self.sides = 6
        else:
            self.sides = sides

    def roll_die(self):
        num = randint(1, self.sides)
        print(num)

d = Die(10)
d.roll_die()