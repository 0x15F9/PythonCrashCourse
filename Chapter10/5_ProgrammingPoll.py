import time

def record_reason(name, reason):
    with open('responses.txt', 'a') as file_object:
        date = time.strftime("%d/%m/%Y %H:%M:%S")
        file_object.write("[{}] {} - {}\n".format(date, name, reason))

while True:
    name = raw_input('Name: ')
    if name == "":
        break
    else:
        reason = raw_input("So, {}, why do you like programming? ".format(name))
        record_reason(name, reason)
        print("Your answer has been saved. Thanks for your time.\n")