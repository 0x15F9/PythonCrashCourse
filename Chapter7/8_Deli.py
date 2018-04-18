sandwich_orders     = ["Tuna", "Chicken", "Vegan", "Salami", "Burger"]
finished_sanwich    = []

for sandwich in sandwich_orders:
    print("I made you {} sandwich.".format(sandwich.lower()))
    finished_sanwich.append(sandwich)

print("All sandwiches have been made!")

for sandwich in finished_sanwich:
    print(sandwich)