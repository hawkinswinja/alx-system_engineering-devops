#!/usr/bin/python3
"""Query the top hot comments"""

import requests


def top_ten(subreddit):
    """Request top ten hot posts of subreddit from Reddit API"""
    # set custom user-agent
    user_agent = '0x16-api_advanced-hawkinswinja'
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)

    # custom user-agent avoids request limit
    headers = {'User-Agent': user_agent}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print('None')
    else:
        # load response unit from json
        data = response.json()['data']
        # extract list of pages
        posts = data['children']
        for post in posts:
            print(post['data']['title'])
