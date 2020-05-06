#!/usr/bin/python3
""" File exports data to Json format"""

import json
import requests
import sys


if __name__ == "__main__":

    user_input = sys.argv[1]

    response_todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    response_users = requests.get('https://jsonplaceholder.typicode.com/users/'
                                  + '{}'.format(user_input))

    todos = response_todos.json()
    users = response_users.json()
    owed_task = []

    for task in todos:
        owed_task.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": users.get("username")})


    task_dict = {user_input: owed_task}
    jsonfile = "{}.json".format(user_input)
    with open(jsonfile, "w") as json_file:
        """ exports data to json """
        json.dump(user_input, json_file)
