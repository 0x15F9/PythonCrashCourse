import json

filename = 'username.json'

def get_stored_username():
    """Get stored username if available"""
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except IOError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username"""
    username = raw_input('What is your name? ')
    try:
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
    except IOError:
        print("Unable to save.")
    else:
        return username

def greet_user():
    """Greet the user by name"""
    username = get_stored_username()
    if username:
        sameUser = raw_input("Is this {}? (y/n)".format(username))
        if sameUser == 'y':
            print("Welcome back {}.".format(username))
        else:
            username = get_new_username()
            print("We'll remember you when you come back {}.".format(username))   
    else:
        username = get_new_username()
        print("We'll remember you when you come back {}.".format(username))

greet_user()