#!/usr/bin/python3
"""this module queries the reddit api,
    parses the title of all hot articles,
    and prints a sorted count of given keywords"""

from collections import Counter
import requests


def count_words(subreddit, word_list, after=None, word_counts=None):
    headers = {"User-Agent": "100_count/1.0"}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    params = {'limit': 100, 'after': after}

    if word_counts is None:
        word_counts = Counter()

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()

        if 'error' in data:
            return

        for post in data['data']['children']:
            title = post['data']['title'].lower()
            for word in word_list:
                if f" {word.lower()} " in f" {title} ":
                    word_counts[word.lower()] += 1

        if data['data']['after']:
            count_words(subreddit, word_list,
                        after=data['data']['after'], word_counts=word_counts)
        else:
            sorted_list = [x for x in sorted(word_counts.keys())]
            for word in sorted_list:
                print(f"{word}: {word_counts[word]}")
    else:
        print(f"Request failed with status code {response.status_code}")
