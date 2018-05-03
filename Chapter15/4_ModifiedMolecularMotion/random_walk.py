from random import choice

class RandomWalk():
    """Class definition for creating a random walk"""
    def __init__(self, number=5000):
        self.number = number

        self.x_dir = [-1 , 1]
        self.x_mag = [0, 1, 2, 3, 4, 5]

        self.y_dir = [-1 , 1]
        self.y_mag = [0, 1, 2, 3, 4, 5]


        self.x_arr = [0]
        self.y_arr = [0]

    def fill_walk(self):
        while len(self.x_arr) <= self.number:

            direction_x = choice(self.x_dir)
            magnitude_x = choice(self.x_mag)

            direction_y = choice(self.y_dir)
            magnitude_y = choice(self.y_mag)

            x = direction_x * magnitude_x
            y = direction_y * magnitude_y

            if x == y == 0:
                continue

            self.x_arr.append(self.x_arr[-1] + x)
            self.y_arr.append(self.y_arr[-1] + y)
        
