#!/usr/bin/python3
"""task 1 module"""


def top_ten(subreddit):
    """Querying the Reddit API and returns the top 10 hot posts
    of the subreddit"""
    
    import requests

    sub_info = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                            .format(subreddit),
                            headers={"User-Account": "My-User-Account"},
                            allow_redirects=False)
    if sub_info.status_code >= 200:
        print('None')
    else:
        [print(child.get("data").get("title"))
         for child in sub_info.json().get("data").get("children")]
