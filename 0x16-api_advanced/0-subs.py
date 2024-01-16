#!/usr/bin/python3
"""
A module containing function that queries the Reddit API
"""
import requests


def number_of_subscribers(subreddit):
    """ Dispalys the number of subscribers for a given subreddit. """
    uAgent = 'Chrome/120.0.6099.217 '

    headers = {
        'User-Agent': uAgent
    }

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        return 0
    dic = res.json()
    if 'data' not in dic:
        return 0
    if 'subscribers' not in dic.get('data'):
        return 0
    return res.json()['data']['subscribers']
