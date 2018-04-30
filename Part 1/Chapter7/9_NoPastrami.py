sandwich_orders     = ["Tuna", "Pastrami", "Chicken", "Pastrami", "Vegan", "Salami", "Pastrami", "Burger"]
finished_sanwich    = []

print("The Deli has run out of pastrami.")

for sandwich in sandwich_orders:
    if sandwich == "Pastrami":
        print("No pastrami dude!")
    else:
        print("I made you {} sandwich.".format(sandwich.lower()))
        finished_sanwich.append(sandwich)

print("All sandwiches have been made!")

for sandwich in finished_sanwich:
    print(sandwich)