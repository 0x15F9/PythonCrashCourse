plants = ["Cherry", "Strawberry", "Litchi", "Mango"]
statement = "I would like to own a {} tree"

# I guess i'm too lazy for the manual looping
for plant in plants:
    print(statement.format(plant))