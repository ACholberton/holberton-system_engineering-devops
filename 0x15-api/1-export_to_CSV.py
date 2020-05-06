#!/usr/bin/python3
""" Python script to export data in the CSV format."""
import csv
import requests
import sys


if __name__ == "__main__":

    user_input = sys.argv[1]

    response_todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    response_users = requests.get('https://jsonplaceholder.typicode.com/users/'
                                  + '{}'.format(user_input))

    todos = response_todos.json()
    users = response_users.json()
    user = users.get('username')

    tasks = []
    pending_task = []
    task_counter = 0
    counter = 0

    for task in todos:
        if str(task.get('userId')) == user_input:
            counter += 1
            tasks.append(task.get('title'))
            if str(task.get('completed')) == "True":
                task_counter += 1
                tasks.append(task.get('True'))
            else:
                tasks.append(task.get('False'))

    with open('{}.csv'.format(user_input), 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quoting=csv.QUOTE_MINIMAL)
        for pen_tasks in range(0, len(tasks)):
            spamwriter.writerow(user_input, user, pending_task[pen_tasks],
                                tasks[pen_tasks])
