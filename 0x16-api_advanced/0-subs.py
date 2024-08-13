#!/usr/bin/python3
"""function that queries the Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """funtion to write the following code"""
    url = f"https://api.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    ok = requests.get(url, headers=headers, allow_redirects=False)
    if ok.status_code == 200:
        rabi = ok.json()
        return rabi['data']['subscribers']
    else:
        return 0
