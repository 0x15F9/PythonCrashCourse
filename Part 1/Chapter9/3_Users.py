class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name  = last_name
        self.age        = age

    def describe_user(self):
        print("{} {} is {} years old.".format(self.first_name, self.last_name, self.age))

    def greet_user(self):
        print("Hello {}".format(self.first_name))

me = User("Isfaaq", 'Goomany',18)
me.describe_user()
me.greet_user()