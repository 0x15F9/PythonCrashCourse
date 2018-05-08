import requests
import json
import pygal
from pygal.style import LightSolarizedStyle as LSL, LightenStyle as LS

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 25

my_style = LS("#240699", base_style = LSL)

url = "https://api.github.com/search/repositories?q=language:bash&sort=stars"
number_of_repos = 10
r = requests.get(url)
status_code = r.status_code

values, names = [], []

if status_code == 200:
    data_dict = r.json()
    repo_dict = data_dict['items']

    # print('Status Code:', status_code)
    # print('results:', data_dict['total_count'])
    # print('')
    # print('Information about the first {} repositories:'.format(number_of_repos))

    for index in range(number_of_repos):
        # print('Name:', repo_dict[index]['name'])
        # print('Description:', repo_dict[index]['description'])
        # print('Owner:', repo_dict[index]['owner']['login'])
        # print('Stars:', repo_dict[index]['stargazers_count'])
        # print('Repository:', repo_dict[index]['html_url'])
        # print('')
        values.append({
            'value': repo_dict[index]['stargazers_count'],
            'label': repo_dict[index]['description'],
            'xlink': repo_dict[index]['html_url']
            })
        names.append(repo_dict[index]['name'])


line_chart = pygal.Bar(my_config, style=my_style)
line_chart.title = 'Top {} most starred python repos'.format(number_of_repos)
# line_chart.add('', stars)
line_chart.add('', values)
line_chart.x_labels = names

line_chart.render_to_file('stars.svg')
