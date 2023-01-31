#!/usr/bin/python3
"""query the total subcribers of a valid subreddit"""
import requests


def number_of_subscribers(subreddit):
    """returns the total subcribers of a subreddit"""
    url = 'https://www.reddit.com/r/{}.json'.format(subreddit)
    user = '0x16-api_advanced_hawkinswinja)'
    headers = {'User_Agent': user}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    data = response.json()['data']
    pages = data.get('children')
    page_data = pages[0]['data']
    return page_data.get('subscribers')
