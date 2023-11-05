#!/usr/bin/python3
"""
Using what you did in the task #0,
extend your Python script to export
data in the CSV format.

Requirements:

Records all tasks that are owned by this employee
Format must be:
"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv
"""

import csv
import json
import requests
import sys


# using this url https://jsonplaceholder.typicode.com/todos/
# add a query string of userId = 2 using the requests module
url1 = "https://jsonplaceholder.typicode.com/todos"
url2 = f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}"
payload = {"userId": sys.argv[1]}


# Make a HTTP request to the remote API to retrieve the employee's tasks.
response = requests.get(url1, params=payload)

# Decode the JSON response into a Python object.
response_data1 = response.json()

# Get the employee's name from the second request.
employee_name = requests.get(url2).json()["username"]

# file name depends on id
filename = f"{sys.argv[1]}.csv"


with open(filename, "w", newline="") as csvfile:
    # create a csv writer object
    data_writer = (
            csv.writer(
                csvfile,
                delimiter=",",
                quotechar='"',
                quoting=csv.QUOTE_ALL,
            )
    )
    # iterate through the first request only and use the value of some key
    # and use the username of the second request for every iteration
    for data in response_data1:
        data_writer.writerow((
            data["userId"],
            employee_name,
            data["completed"],
            data["title"],
        ))
