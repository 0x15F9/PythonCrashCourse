import pygal
from random_walk import RandomWalk

rw = RandomWalk(50)
res = [(rw.x_arr[a], rw.y_arr[a]) for a in range(0, rw.number + 1)]

xy_chart = pygal.XY(stroke=100)
xy_chart.title = 'Scatter Plot of a random walk with PyGal'

xy_chart.add('Random Walk', res)

xy_chart.render_to_file('test.svg')