#!/usr/bin/python3
"""Write a function that queries the Reddit"""
import requests


def top_ten(subreddit):
    """a function that print out """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        abga = res.json()
        posts = abga['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        print('None')
        return
