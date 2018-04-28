import time

def record_user(name):
    with open('guest_book.txt', 'a') as file_object:
        date = time.strftime("%d/%m/%Y %H:%M:%S")
        file_object.write("[{}] {}\n".format(date, name))

while True:
    name = raw_input('Name: ')
    if name == "":
        break
    else:
        record_user(name)
        print('Hello {}! I hope that you are doing well :)'.format(name))