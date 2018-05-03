import matplotlib.pyplot as plt

# x_arr = [1, 2, 3, 4, 5]
x_arr = list(range(1, 5000))
y_arr = [x**3 for x in x_arr]

plt.title('Cubes', fontsize=16)
plt.scatter(x_arr, y_arr, edgecolor='none', c=y_arr, cmap=plt.cm.Reds, s=2)
plt.show()