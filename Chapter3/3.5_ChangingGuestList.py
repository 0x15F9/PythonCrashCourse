guests = ["Dada", "Dadi", "Mama", "Papa", "Zal", "Chacha Yaseen"]
message = "Hey {}!\nI hope that you are doing fine. I would like to invite you over at my place for dinner on Sunday the 22nd of April at 7:30"

for guest in guests:
    print(message.format(guest))

print ("\nChacha Yaseen cannot make it\n")
guests.pop()
guests.append("Nee")

for guest in guests:
    print(message.format(guest))