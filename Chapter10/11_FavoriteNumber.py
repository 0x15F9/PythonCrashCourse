import json

def save(filename, content):
    with open(filename, 'w') as json_file:
        json.dump(content, json_file)

fav_num = int(raw_input("Favorite number: "))
save('favorite_number.json', fav_num)