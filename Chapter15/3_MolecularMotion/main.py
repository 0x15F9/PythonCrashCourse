import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk(1000)

plt.title("Molecular Motion", fontsize=16)
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
# plt.scatter(rw.x_arr, rw.y_arr, c=[x for x in list(range(0, len(rw.x_arr)))], cmap=plt.cm.Reds, s=10)
plt.plot(rw.x_arr, rw.y_arr, linewidth=0.5)
plt.scatter(rw.x_arr[0], rw.y_arr[0])
plt.annotate(xy=[rw.x_arr[0], rw.y_arr[0]], s="Start")
plt.scatter(rw.x_arr[-1], rw.y_arr[-1])
plt.annotate(xy=[rw.x_arr[-1], rw.y_arr[-1]], s="End")

plt.show()