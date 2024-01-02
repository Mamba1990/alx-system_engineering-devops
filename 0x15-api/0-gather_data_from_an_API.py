#!/usr/bin/python3
"""
Module returning information for a given employee ID.

About his/her TODO list progress from a REST API.
"""

import requests
from sys import argv


def fetch_data(id):
    req = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                       .format(id))
    user = req.json()
    inf = "Employee {} is done with tasks".format(user["name"])

    req = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos"
                       .format(id))
    todos = req.json()
    inf += "({}/{}):".format(
                        sum(1 for todo in todos if todo["completed"]),
                        len(todos))
    for todo in todos:
        if todo["completed"]:
            inf += "\n\t {}".format(todo["title"])
    print(inf)


if __name__ == "__main__":
    fetch_data(argv[1])
