person = {
    "firstName" : "Muhammad Isfaaq",
    "lastName"  : "Goomany",
    "age"       : 18,
    "dob"       : "24/06/1999",
}

person1 = {
    "firstName" : "Muhammad Umar Farook",
    "lastName"  : "Auhammud",
    "age"       : 18,
    "dob"       : "26/06/1999",
}

person2 = {
    "firstName" : "Muhammad Izhaar Shafee",
    "lastName"  : "Goomany",
    "age"       : 13,
    "dob"       : "04/11/2004",
}

persons = [person, person1, person2]

for human in persons:
    for k,v in sorted(human.items(), reverse=True):
        print("The {} of the person is {}".format(k,v))
    print("")