magicians = ['gandalf', 'albus', 'hagrid', 'saruman']

def show_magicians(magicians):
    for magician in magicians:
        print(" - {}".format(magician))

def make_great(magicians):
    for i in range(0, len(magicians)):
        magicians[i] = "Great " + magicians[i]

make_great(magicians)
show_magicians(magicians)