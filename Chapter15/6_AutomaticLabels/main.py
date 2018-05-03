import pygal
from die import Dice

dice = Dice(6)
result = dice.multiroll(100000)
frequencies = [result.count(value) for value in range(1, 7)]

hist = pygal.Bar()
hist.title = 'Result of rolling a D6'
hist.x_labels = [x for x in range(1, 7)]
hist.x_title = 'Values on Die'
hist.y_title = 'Frequency' 
hist.add('D6', frequencies)

hist.render_to_file('test.svg')