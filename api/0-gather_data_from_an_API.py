#!/usr/bin/python3

"""
This script fetches and analyzes completed tasks for a given
employee from a remote API

It takes an employee's ID as a command-line argument, retrieves
the tasks associated with that employee,
and displays the number of completed tasks, total tasks, and the
titles of completed tasks.

Usage:
    $ python script_name.py employee_id

Args:
    employee_id (int): The ID of the employee for whom you want
    to analyze completed tasks.

Example:
    $ python script_name.py 1
"""

if __name__ == "__main__":
    import json
    import sys
    import urllib.request
    # Get the employee's ID from the sys module and format it into the URL
    # https://jsonplaceholder.typicode.com/users/{employees_id}
    employee_id = sys.argv[1]
    url1 = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    url2 = f"https://jsonplaceholder.typicode.com/users/{employee_id}/"
    # Create the request objects.
    request_object1 = urllib.request.Request(url1)
    request_object2 = urllib.request.Request(url2)
    # Get data from the server.
    with urllib.request.urlopen(request_object1) as get_data1:
        response_data1 = json.load(get_data1)
    with urllib.request.urlopen(request_object2) as get_data2:
        response_data2 = json.load(get_data2)
    # Use a list comprehension to filter completed tasks
    completed_tasks = [task for task in response_data1 if task['completed']]
    # Get the number of completed tasks and total tasks
    no_of_comptasks = len(completed_tasks)
    totalno_of_task = len(response_data1)
    # Get Employee Name
    employee_name = response_data2["name"]
    # Print output in the requested format;
    # Employee EMPLOYEE_NAME is done with
    # tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):'
    print(f"Employee {employee_name} is done with \
            tasks({no_of_comptasks}/{totalno_of_task}):")
    # Second and N following lines display the title of
    # completed tasks: TASK_TITLE (with 1 tabulation and 1
    # space before the TASK_TITLE)
    # Print the completed tasks
    for task in completed_tasks:
        print("\t" + " " + task["title"])
