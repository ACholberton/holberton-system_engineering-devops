#!/usr/bin/python3
"""python script displays for a given employee ID the returned information
about his/her TODO list progress."""

import requests
import sys
from sys import argv


if __name__ == '__main__':

    user_input = sys.argv[1]

    response_todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    response_users = requests.get('https://jsonplaceholder.typicode.com/users/'
                                  + '{}'.format(user_input))

    todos = response_todos.json()
    users = response_users.json()

    completed_task = []
    for task in completed_task:
        if task['completed'] is True:
            completed_task.get(['title'])

    print("Employee {} is done with tasks({}/{}):".format(users['name'],
                                                          len(todos),
                                                          len(completed_task)))

    for task in completed_task:
        print('\t {}'.format(task))
