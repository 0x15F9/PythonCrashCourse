from matplotlib import pyplot as plt
from datetime import datetime
import csv

def read_csv_to_dict(filename):
    with open(filename) as f:
        result = {}
        reader = csv.reader(f)
        header_row = next(reader)
        for row in reader:
            month = []
            for index, col in enumerate(row):
                if index == 0:
                    year = col
                else:
                    month.append(col)
            result[year] = month
        return result

def dict_to_xy(dictionary):
    month = []
    temperature = []
    for k, v in dictionary.items():
        year = k
        for index, temp in enumerate(v):
            if index < 12:
                if index < 9:
                    m = '0{}'.format(index+1)
                else :
                    m = str(index+1)
                month.append(datetime.strptime('{}-{}'.format(year, m), '%Y-%m') )
                temperature.append(temp)
    return month, temperature