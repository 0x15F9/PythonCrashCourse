milou = {
    "kind" : "dog",
    "owner" : "tintin"
}

piku = {
    "kind" : "bird",
    "owner" : "zaf"
}

popo = {
    "kind" : "dog",
    "owner" : "unkar"
}

robo = {
    "kind" : "bird",
    "owner" : "zal"
}

pets = [milou, piku, popo, robo]

for pet in pets:
    for k, v in pet.items():
        print("{} : {}".format(k, v))