from random import choice

class RandomWalk():
    """Class definition for creating a random walk"""
    def __init__(self, number=5000):
        self.number = number
        self.x_arr = [0]
        self.y_arr = [0]
        self.fill_walk()

    def fill_walk(self):
        while len(self.x_arr) <= self.number:
            direction_x = choice([-1, 1])
            magnitude_x = choice([0, 1, 2, 3, 4, 5])
            x           = direction_x * magnitude_x

            direction_y = choice([-1, 1])
            magnitude_y = choice([0, 1, 2, 3, 4, 5])
            y           = direction_y * magnitude_y

            if x == y == 0:
                continue

            self.x_arr.append(self.x_arr[-1] + x)
            self.y_arr.append(self.y_arr[-1] + y)

    def return_tuple(self):
        return [(self.x_arr(a), self.y_arr(a)) for a in range(0,5)]
            
        
