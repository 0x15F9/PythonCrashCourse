import pygal
from die import Dice

dice1 = Dice(8)
dice2 = Dice(8)
result1 = dice1.multiroll(100000)
result2 = dice2.multiroll(100000)

freq1 = [result1.count(value) for value in range(1, dice1.sides+1)]
freq2 = [result2.count(value) for value in range(1, dice1.sides+1)]

hist = pygal.Bar()
hist.title = 'Result of rolling two D8'
hist.x_labels = [x for x in range(1, 9)]
hist.x_title = 'Values on Die'
hist.y_title = 'Frequency'

# hist.add('First D8', freq1)
# hist.add('Second D8', freq2)


hist.x_labels = [x for x in range(1, 17)]
sum_result = [result1[x] + result2[x] for x in range(0, len(result1))]
freq_sum = [sum_result.count(x) for x in range(1, 17)]

hist.add('Frequency of Sums', freq_sum)

hist.render_to_file('test.svg')