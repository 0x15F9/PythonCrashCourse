import requests
import json

def get_repos(url, num_of_repos):
    r = requests.get(url)
    status_code = r.status_code

    if status_code == 200:
        data_dict = r.json()
        repo_dict = data_dict['items']
    
    return repo_dict

def print_results(result):
    for index in range(len(result)):
        print('Name:', result[index]['name'])
        print('Description:', result[index]['description'])
        print('Owner:', result[index]['owner']['login'])
        print('Stars:', result[index]['stargazers_count'])
        print('Repository:', result[index]['html_url'])
        print('')


def result_into_dict(result):
    values, names = [], []
    for index in range(len(result)):
        values.append({
            'value': int(result[index]['stargazers_count']),
            'label': result[index]['description'],
            'xlink': result[index]['html_url']
            })
        names.append(result[index]['name'])
    return values, names