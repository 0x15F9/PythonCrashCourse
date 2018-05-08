import csv
from pygal.maps.world import COUNTRIES

not_found = set()

def country_name_to_code(name):
    try:
        for k, v in COUNTRIES.items():
            if name == v:
                return k
            elif name == 'Iran, Islamic Rep.':
                return 'ir'
            elif name == 'Libya':
                return 'ly'
            elif name == 'Egypt, Arab Rep.':
                return 'eg'
                
    except:
        return None

def get_data(filename, year):
    country_name, country_code, data = [], [], []
    with open(filename) as f:
        year_col = None
        raw_data = csv.reader(f)
        header_row = next(raw_data)
        for ix, code in enumerate(header_row):
            if str(code) == str(year):
                year_col = ix
                break
        for row in raw_data:
            country_name.append(row[0])
            country_code.append(country_name_to_code(country_name[-1]))
            if row[year_col] != '':
                data.append(row[year_col])
            else:
                this_year_col = year_col
                while row[this_year_col] == '' and this_year_col >= 5:
                    this_year_col -= 1
                if this_year_col ==  4 and row[this_year_col] == '':
                    data.append(0)
                else:
                    data.append(row[this_year_col])
    return country_name, country_code, data

def sortListToDicts(country_code, data):
    no_data, less_than_50, less_than_75, more_than_75 = {}, {}, {}, {}
    for ix, country in enumerate(country_code):
        if country != None:
            this_data = float(data[ix])
            if this_data == 0.0:
                no_data.update({country : this_data})
            elif this_data < 50 and this_data > 0:
                less_than_50.update({country : this_data})
            elif this_data < 75 and this_data >= 50:
                less_than_75.update({country : this_data})
            elif this_data >= 75 and this_data < 100:
                more_than_75.update({country : this_data})
    return no_data, less_than_50, less_than_75, more_than_75


# country_name, country_code, data = get_data('YouthLiteracyRate.csv', 2016)
# no_data, less_than_50, less_than_75, more_than_75 = sortListToDicts(country_code, data)
# print(no_data)