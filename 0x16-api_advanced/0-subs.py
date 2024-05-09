#!/usr/bin/python3
"""
This module contains a function used to obtain the number of subscribers 
in a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Return the total number of subscribers on a given subreddit
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    response = requests.get(url=url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    json = response.json()
    return (json.get("data").get("subscribers"))
