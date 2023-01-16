#!/usr/bin/python3
"""script to get api data"""

if __name__ == '__main__':
    import requests
    import json
    filename = 'todo_all_employees.json'
    url = 'https://jsonplaceholder.typicode.com'
    response = requests.get(url + '/users')
    allusers = response.json()
    alltasks = {}
    for user in allusers:
        fetch = requests.get(url + '/users/' + str(user.get('id')) + '/todos')
        mytasks = fetch.json()
        tasks_list = []
        for task in mytasks:
            task_dict = {"username": user.get('name')}
            task_dict["task"] = task.get('title')
            task_dict["completed"] = task.get('completed')
            tasks_list.append(task_dict)
        alltasks[user.get('id')] = tasks_list
    with open(filename, 'w', encoding='UTF8', newline='') as f:
        json.dump(alltasks, f)
