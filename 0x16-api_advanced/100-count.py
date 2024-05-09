#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit."""
import requests


def count_words(subreddit, word_list, instances={}, after="", count=0):
    """Prints counts of given words found in hot posts of a given subreddit.

    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        instances (obj): Key/value pairs of words/counts.
        after (str): The parameter for the next page of the API results.
        count (int): The parameter of results matched thus far.
    """
    word_list = set([word.lower() for word in word_list])
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"user-agent": "shdh"}
    params = {"after": after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 20:
        return None

    data = response.json().get("data")
    for child in data.get("children"):
        title_words = child.get("data").get("title").lower().split()
        for word in word_list:
            dic[word] = dic.get(word, 0) + title_words.count(word)
    after = data.get("after")

    if after:
        count_words(subreddit, word_list, after, dic)
    else:
        word_list.sort(key=lambda x: dic.get(x), reverse=True)
        for word in word_list:
            if dic.get(word):
                print("{}: {}".format(word, dic.get(word)))
