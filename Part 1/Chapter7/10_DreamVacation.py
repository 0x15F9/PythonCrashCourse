poll = {}

place = ""
polling = True

while polling:
    place = raw_input("If you could visit one place in the world, where would you go?\n")
    if place != "":
        if poll.has_key(place):
            poll[place] += 1
        else:
            poll[place] = 1
    else:
        polling = False
        break

for k,v in poll.items():
    print("{} : {}".format(k,v))