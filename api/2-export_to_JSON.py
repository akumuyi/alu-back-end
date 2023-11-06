#!/usr/bin/python3
"""
This script fetches and analyzes completed tasks for a given
employee from a remote API and exports the data in JSON format.

Usage:
    $ python script_name.py employee_id

Args:
    employee_id (int): The ID of the employee for whom you want
    to analyze completed tasks and export the data in JSON format.

"""


import json
import sys
import urllib.request


def export_to_json(employee_id):
    """Exports the employee's task data to JSON format.

    Args:
        employee_id (int): The ID of the employee for whom you want
        to export the task data.

    Returns:
        str: A JSON string containing the employee's task data.
    """

    # Define the URLs for employee tasks and user information
    tasks_url = (
        "https://jsonplaceholder.typicode.com/todos?"
        "userId={employee_id}"
    )
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    # Create the request objects for tasks and user information
    tasks_request = urllib.request.Request(tasks_url)
    user_request = urllib.request.Request(user_url)

    try:
        # Get data from the server for tasks and user information
        with urllib.request.urlopen(tasks_request) as tasks_response, \
             urllib.request.urlopen(user_request) as user_response:
            tasks_data = json.load(tasks_response)
            user_data = json.load(user_response)
    except urllib.error.URLError as e:
        print(f"Failed to fetch data: {e}")
        sys.exit(1)

    # Extract the username
    username = user_data.get("username", "")

    # Prepare the data in the specified JSON format
    task_list = [
        {
            "task": task["title"],
            "completed": task["completed"],
            "username": username,
        }
        for task in tasks_data
    ]

    # Create a list of dictionaries where each dictionary represents a task
    data_to_export = task_list

    # Return the JSON string containing the task data
    return json.dumps(data_to_export, indent=4)\



if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python script_name.py employee_id")
        sys.exit(1)

    # Get the employee's ID from the command line argument
    employee_id = sys.argv[1]

    # Export the employee's task data to JSON format
    json_data = export_to_json(employee_id)

    # Write the JSON data to a file
    json_filename = f"{employee_id}.json"
    with open(json_filename, "w") as json_file:
        json_file.write(json_data)

    # Print the name of the JSON file to which the data was exported
    print(f"Data exported to {json_filename}")
