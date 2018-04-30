#!/bin/python3
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Creates a Restaurant called <restaurant_name> offering <cuisine_type>"""
        self.restaurant_name    = restaurant_name
        self.cuisine_type       = cuisine_type

    def describe_restaurant(self):
        """Displays information about the Restaurant"""
        print("The Restaurant is called {} and offers {} cuisine.".format(self.restaurant_name, self.cuisine_type))


class IceCreamstand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors            = flavors
    
    def display_flavors(self):
        for flavor in self.flavors:
            print('- {}'.format(flavor))

VonaCorona = IceCreamstand('Vona Corona', 'Mauritian',  ['vanilla', 'chocolate', 'caramel', 'sparkle', 'bubbly'])
VonaCorona.display_flavors()