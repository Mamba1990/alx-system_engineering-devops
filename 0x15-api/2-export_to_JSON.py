#!/usr/bin/python3
"""
Module returns information for a given employee ID.

About his/her TODO list progress from a REST API.
"""

import json
from sys import argv
import requests


def fetch_data(id):
    req = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                       .format(id))
    user = req.json()

    req = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos"
                       .format(id))
    todos = req.json()
    taskList = []
    for todo in todos:
        task = {
            "task": todo["title"],
            "completed": todo["completed"],
            "username": user["username"],
        }
        taskList.append(task)

    data = {str(user["id"]): taskList}
    file_name = "{}.json".format(user["id"])
    with open(file_name, "w") as fi:
        json.dump(data, fi)


if __name__ == "__main__":
    fetch_data(argv[1])
