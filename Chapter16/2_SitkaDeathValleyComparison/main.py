from matplotlib import pyplot as plt
from datetime import datetime
import csv

def f_to_c(f):
    return int((int(f)-32)/1.8)

def convert_date(date):
    year = date.split('-')[0]
    month = date.split('-')[1]
    if len(month) == 1:
        month = '0{}'.format(month)
    d = date.split('-')[2]
    if len(d) == 1:
        d = '0{}'.format(d)
    date = '{}-{}-{}'.format(year, month, d)
    return datetime.strptime(date, "%Y-%m-%d")

dv_mean, st_mean ,yr = [], [], []

with open('sitka_weather_2014.csv') as file_object:
    reader = csv.reader(file_object)
    header = next(reader)
    for rows in range(300):
        line = next(reader)
        st_mean.append(f_to_c(line[2]))
        yr.append(convert_date(line[0]))

with open('death_valley_2014.csv') as file_object:
    reader = csv.reader(file_object)
    header = next(reader)
    for rows in range(300):
        line = next(reader)
        dv_mean.append(f_to_c(line[2]))

fig = plt.figure(dpi=128, figsize=(10, 8))
plt.title("Comparison of Mean temperatures")
plt.xlabel("Date")
plt.ylabel('Temperature')

plt.plot(yr, st_mean, linewidth=0.2, color='red')
plt.plot(yr, dv_mean, linewidth=0.2, color='blue')
plt.fill_between(yr, st_mean, dv_mean, facecolor='green', alpha=0.2)

fig.autofmt_xdate()
plt.show()