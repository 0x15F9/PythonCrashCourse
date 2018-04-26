class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Creates a Restaurant called <restaurant_name> offering <cuisine_type>"""
        self.restaurant_name    = restaurant_name
        self.cuisine_type       = cuisine_type
        self.number_served      = 0

    def describe_restaurant(self):
        """Displays information about the Restaurant"""
        print("The Restaurant is called {} and offers {} cuisine.".format(self.restaurant_name, self.cuisine_type))
        print("It has served {} clients.".format(self.number_served))

    def increment_number_served(self):
        self.number_served += 1
        print(self.number_served)

KiTiCui = Restaurant("KiTiCui", "maurician")
KiTiCui.describe_restaurant()
KiTiCui.increment_number_served()