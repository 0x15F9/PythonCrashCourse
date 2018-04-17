guests = ["Dada", "Dadi", "Mama", "Papa", "Zal", "Chacha Yaseen"]
message = "Hey {}!\nI hope that you are doing fine. I would like to invite you over at my place for dinner on Sunday the 22nd of April at 7:30"

for guest in guests:
    print(message.format(guest))

print("I can only invite 2 persons over for dinner")

while len(guests) > 2:
    print("Sorry {}, I cannot invite you over".format(guests[-1]))
    guests.pop()

for guest in guests:
    print("Hey {}! You are still invited! Make sure you come.".format(guest))

del guests
print(len(guests))