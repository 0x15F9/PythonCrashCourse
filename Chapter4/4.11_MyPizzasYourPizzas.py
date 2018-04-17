pizzas = ["pepperoni", "mexican", "hawaiian"]

friendsPizzas = pizzas[:]
friendsPizzas.append("brazilian")

print("My favorite pizzas are: {}".format(pizzas))

print("My friend's favorite pizzas are:")
for pizza in friendsPizzas:
    print("{} pizza.".format(pizza))