#!/usr/bin/python3
"""script to get api data"""

if __name__ == '__main__':
    import requests
    import sys
    url = 'https://jsonplaceholder.typicode.com/users/' + sys.argv[1]
    response = requests.get(url + '/todos')
    r = requests.get(url)
    usertasks = response.json()
    userdata = r.json()
    complete = len(list(filter(lambda x: (x.get('completed')), usertasks)))
    print('Employee {} is done with tasks({}/{}):'
          .format(userdata.get('name'), complete, len(usertasks)))
    for x in usertasks:
        print('	 {}'.format(x.get('title')))
