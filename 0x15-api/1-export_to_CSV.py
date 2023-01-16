#!/usr/bin/python3
"""script to get api data"""

if __name__ == '__main__':
    import requests
    import sys
    import csv
    filename = sys.argv[1] + '.csv'
    url = 'https://jsonplaceholder.typicode.com/users/' + sys.argv[1]
    response = requests.get(url + '/todos')
    r = requests.get(url)
    usertasks = response.json()
    username = r.json().get('name')
    with open(filename, 'w', newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [sys.argv[1], username, t.get("completed"), t.get("title")]
         ) for t in usertasks]
