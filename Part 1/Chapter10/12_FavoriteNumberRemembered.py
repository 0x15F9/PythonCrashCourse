import json

file = 'fav_num.json'

def save(filename, content):
    try:
        with open(filename, 'w') as json_file:
            json.dump(content, json_file)
    except IOError:
        pass

def fetch(filename):
    try:
        with open(filename, 'r') as json_file:
            return(json.load(json_file))
    except IOError:
        return ''
        pass

content = fetch(file)

if content == '':
    fav_num = int(raw_input("Favorite number: "))
    save(file, fav_num)
else:
    print("I know that your favorite number is {}.".format(content))
