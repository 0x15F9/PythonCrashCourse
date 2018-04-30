guests = ["Dada", "Dadi", "Mama", "Papa", "Zal", "Chacha Yaseen"]
message = "Hey {}!\nI hope that you are doing fine. I would like to invite you over at my place for dinner on Sunday the 22nd of April at 7:30"

for guest in guests:
    print(message.format(guest))

print ("\nI just found a bigger dinner table.\n")
guests.insert(0, "Nee")
guests.insert(len(guests) // 2, "Karan")
guests.append("Zia")

for guest in guests:
    print(message.format(guest))