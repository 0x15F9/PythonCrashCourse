from matplotlib import pyplot as plt
from preprocess import *

max_air_temp = read_csv_to_dict('mru_max_air_temp.csv')
max_air_temp_x, max_air_temp_y = dict_to_xy(max_air_temp)
min_air_temp = read_csv_to_dict('mru_min_air_temp.csv')
min_air_temp_x, min_air_temp_y = dict_to_xy(min_air_temp)

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.title('Air Temp Comparison for Mauritius from 1983 to 2005')
plt.xlabel('Year')
plt.ylabel("Temperature (C)")
plt.legend(loc='upper left')
fig.autofmt_xdate()

plt.plot(max_air_temp_x, max_air_temp_y, linewidth=0.5, c='red', label='Max')
plt.plot(min_air_temp_x, min_air_temp_y, linewidth=0.5, c='blue', label='Min')

plt.show()