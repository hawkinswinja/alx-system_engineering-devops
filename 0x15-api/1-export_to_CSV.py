#!/usr/bin/python3
"""script to get api data"""

if __name__ == '__main__':
    import requests
    import json
    import sys
    import csv
    filename = sys.argv[1] + '.csv'
    url = 'https://jsonplaceholder.typicode.com/users/' + sys.argv[1]
    response = requests.get(url + '/todos')
    r = requests.get(url)
    usertasks = response.json()
    username = r.json().get('name')
    data = []
    for x in usertasks:
        mytasks = json.dumps("{},{},{},{}".format(sys.argv[1], username,
                             str(x.get('completed')), str(x.get('title'))))
        data.append(mytasks)
    with open(filename, 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
