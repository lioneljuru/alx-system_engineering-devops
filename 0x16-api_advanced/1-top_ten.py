#!/usr/bin/python3
"""
This module contains a function used to obtain the top ten hot posts
in a subreddit
"""
import requests


def top_ten(subreddit):
    """
    Print the 10 hottest posts on a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_"}
    params = {"limit": 10}
    response = requests.get(url=url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        print("None")
        return 0
    data = response.json().get("data").get("children")
    for datum in data:
        print(datum.get("data").get("title"))
