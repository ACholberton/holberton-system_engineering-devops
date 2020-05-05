#!/usr/bin/python3
"""python script displays for a given employee ID the returned information
about his/her TODO list progress."""

import requests
import sys
from sys import argv


if __name__ == '__main__':

    response_todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    response_users = requests.get('https://jsonplaceholder.typicode.com/users')

    todos = response_todos.json()
    users = response_users.json()

    completed_task = []
    for task in completed_task:
        if task['completed'] is True:
            completed_task.append(task['title'])

    print("Employee {} is done with tasks({}/{}):".format(users, len(todos),
                                                          len(completed_task)))

    for task in completed_task:
        print('\t {}'.format(task))
