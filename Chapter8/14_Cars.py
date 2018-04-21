def make_car(manufacturer, model, **attr):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model

    for k, v in attr.items():
        car[k] = v

    return car

# user_profile = make_car('muhammad isfaaq', 'goomany', age=18)

# print(user_profile)