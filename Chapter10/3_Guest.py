def write_name(name):
    with open('guests.txt', 'a') as file_object:
        file_object.write(name+"\n")

name = raw_input('Hello! What is your name? ')
write_name(name)