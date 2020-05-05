#!/usr/bin/python3
"""python script displays for a given employee ID the returned information
about his/her TODO list progress."""

import requests
import sys


if __name__ == '__main__':

    user_input = sys.argv[1]

    response_todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    response_users = requests.get('https://jsonplaceholder.typicode.com/users/'
                                  + '{}'.format(user_input))

    todos = response_todos.json()
    users = response_users.json()

    completed_task = []
    task_counter = 0
    counter = 0

    for task in todos:
        if str(task.get('userId')) == user_input:
            counter += 1
            if str(task.get('completed')) == "True":
                task_counter += 1
                completed_task.append(task.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(users['name'],
                                                          task_counter,
                                                          counter))

    for tasks in completed_task:
        print('\t {}'.format(tasks))
