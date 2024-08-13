#!/usr/bin/python3
"""recursive with api function God help me """
import requests


def recurse(subreddit, hot_list=[]):
    """doing recursive work"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 100, "after": after}
    res = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if res.status_code != 200:
        return None
    data = res.json().get("data", {})
    posts = data.get("children", [])
    after = data.get("after", None)
    hot_list.extend([post["data"]["title"] for post in posts])
    if after is not None:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list if hot_list else None
