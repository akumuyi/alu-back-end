#!/usr/bin/python3
"""
This script fetches and analyzes completed tasks for a given
employee from a remote API and exports the data in JSON format.

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

def export_to_json(employee_id, tasks):
    """Exports the task data to JSON format.

    Args:
        employee_id (int): The ID of the employee for whom the tasks are owned by.
        tasks (list): A list of tasks.

    Returns:
        str: A JSON string containing the task data.
    """

    json_data = {
        "USER_ID": employee_id,
        "tasks": [
            {
                "task": task["title"],
                "completed": task["completed"],
                # Check if the `username` key exists in the `task` dictionary.
                # If it does, add the `username` key to the JSON data.
                "username": task["username"] if "username" in task else None,
            }
            for task in tasks
        ],
    }

    return json.dumps(json_data, indent=4)


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

    # Use a list comprehension to filter completed tasks.
    completed_tasks = [
        task for task in response_data1 if task["completed"]
    ]

    # Get Employee Name
    employee_name = response_data2["name"]

    # Export the task data to JSON format.
    json_data = export_to_json(employee_id, completed_tasks)

    # Write the JSON data to a file.
    with open(f"{employee_id}.json", "w") as outfile:
        outfile.write(json_data)
