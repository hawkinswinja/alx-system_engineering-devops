#!/usr/bin/python3
"""script to get api data"""

if __name__ == '__main__':
    import requests
    import sys
    import json
    filename = sys.argv[1] + '.json'
    url = 'https://jsonplaceholder.typicode.com/users/' + sys.argv[1]
    response = requests.get(url + '/todos')
    r = requests.get(url)
    usertasks = response.json()
    username = r.json().get('name')
    userlist = []
    for x in usertasks:
        task_dict = {"task": x.get('title')}
        task_dict["username"] = str(username)
        task_dict["completed"] = x['completed']
        userlist.append(task_dict)
    with open(filename, 'w', encoding='UTF8', newline='') as f:
        user = {sys.argv[1]: userlist}
        json.dump(user, f)
