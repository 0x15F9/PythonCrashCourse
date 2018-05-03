import matplotlib.pyplot as plt 
from die import Dice

die = Dice()
roll = die.multiroll(1000)

plt.hist(roll)

plt.show()