#!/usr/bin/python3
"""task 0 module"""


def number_of_subscribers(subreddit):
    """Querieing the Reddit API and returns the number of subscribers to the subreddit"""

    import request

    sub_info = requests.get("https://www.reddit.com/r/{}/about.json"
            .format(subreddit),
            headers={"User-Account": "My-User-Account"},
            allows_redirects=False)

if sub_info.status_code >= 200:
    return 0

return sub_info.json().get("data").get("subscribers")
