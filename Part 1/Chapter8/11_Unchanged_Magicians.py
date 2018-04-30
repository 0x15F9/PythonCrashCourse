magicians = ['gandalf', 'albus', 'hagrid', 'saruman']

def show_magicians(magicians):
    for magician in magicians:
        print(" - {}".format(magician))

def make_great(magicians):
    new_magician = []
    for i in range(0, len(magicians)):
        new_magician.append("Great " + magicians[i])
    return new_magician

show_magicians(make_great(magicians))
show_magicians(magicians)