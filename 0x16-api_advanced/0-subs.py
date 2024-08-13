#!/usr/bin/python3
"""function that queries the Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """funtion to write the following code"""
    url = f"https://api.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0', 'Accept': 'application/.json'}
    ok = requests.get(url, headers=headers, allow_redirects=False)
    subs = 0
    if ok.status_code == 200:
        try:
            rabi = ok.json()
            data = rabi.get('data')
            subs = data.get('subscribers')
        except Exception:
            pass
        finally:
            return subs
    return subs
