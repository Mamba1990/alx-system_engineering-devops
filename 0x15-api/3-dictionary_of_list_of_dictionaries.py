#!/usr/bin/python3
"""
Module that returnsinformation for a given employee ID.

About his/her TODO list progress from a REST API.
"""

import json
import requests


def save_data_to_json():
    dt = {}
    for id in range(1, 11):
        req = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                           .format(id))
        user = req.json()
        req = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
        )
        todos = req.json()
        taskList = []
        for todo in todos:
            task = {
                "username": user["username"],
                "task": todo["title"],
                "completed": todo["completed"],
            }
            taskList.append(task)
        dt[str(user["id"])] = taskList

    file_name = "todo_all_employees.json"
    with open(file_name, "w") as fi:
        json.dump(dt, fi)


if __name__ == "__main__":
    save_data_to_json()
