class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name  = last_name
        self.age        = age

    def describe_user(self):
        print("{} {} is {} years old.".format(self.first_name, self.last_name, self.age))

    def greet_user(self):
        print("Hello {}".format(self.first_name))

class Admin(User):
    def __init__(self, first_name, last_name, age, privileges):
        # Inheritance
        super().__init__(first_name, last_name, age)

        self.privileges = ["can add post", "can delete post", "can ban user"]
        self.privileges.extend(privileges)

    def show_privileges(self):
        for privilege in self.privileges:
            print(" - {}".format(privilege))