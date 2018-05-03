import pygal
from die import Dice

sides = 6
rolls = 100000

dice1 = Dice(sides=sides)
dice2 = Dice(sides=sides)
dice3 = Dice(sides=sides)
result1 = dice1.multiroll(rolls)
result2 = dice2.multiroll(rolls)
result3 = dice3.multiroll(rolls)

sum_result = [result1[x] + result2[x] + result3[x] for x in range(0, rolls-1)]
freq_sum = [sum_result.count(value) for value in range(3, 19)]

hist = pygal.Bar()
hist.title = 'Result of rolling 3 D6s'
hist.x_labels = [x for x in range(3, 19)]
hist.x_title = 'Sum of Throw'
hist.y_title = 'Frequency'

hist.add('Frequenct', freq_sum)

hist.render_to_file('test.svg')