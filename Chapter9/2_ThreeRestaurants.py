class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Creates a Restaurant called <restaurant_name> offering <cuisine_type>"""
        self.restaurant_name    = restaurant_name
        self.cuisine_type       = cuisine_type

    def describe_restaurant(self):
        """Displays information about the Restaurant"""
        print("The Restaurant is called {} and offers {} cuisine.".format(self.restaurant_name, self.cuisine_type))

Dhiraj = Restaurant('Dhiraj', 'Mixed')
Dhiraj.describe_restaurant()

Instanbul = Restaurant('Instanbul', 'Turkish')
Instanbul.describe_restaurant()

FlameAndGrill = Restaurant('Flame & Grill', 'Indian')
FlameAndGrill.describe_restaurant()