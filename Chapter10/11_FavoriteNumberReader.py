import json

def fetch(filename):
    with open(filename, 'r') as json_file:
        return(json.load(json_file))

fav_num = fetch('favorite_number.json')
print("I know that your favorite number is {}.".format(fav_num))