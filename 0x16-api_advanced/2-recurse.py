#!/usr/bin/python3
"""
This module contains a recursive function that returns the list of all hot
articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    recursive function that returns a list of all hot articles linked to
    a subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"user-agent": "hsld"}
    params = {"after": after, "limit": 100, "count": count}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None

    results = response.json().get("data")
    for child in results.get("children"):
        hot_list.append(child.get("data").get("title"))

    after = results.get("after")
    count += results.get("dist")

    if after:
        recurse(subreddit, hot_list, after, count)
    return hot_list
