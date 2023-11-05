#!/usr/bin/python3


def export_to_json(employee_id, tasks):
    """Exports the task data to JSON format.

    Args:
        employee_id (int): The ID of the employee
        for whom the tasks are owned by.
        tasks (list): A list of tasks.

    Returns:
        str: A JSON string containing the task data.
    """

    json_data = {
        employee_id: [
            {
                "task": task["title"],
                "completed": task["completed"],
                "username": task.get("username", None),
            }
            for task in tasks
        ]
    }

    return json.dumps(json_data, indent=4)


if __name__ == "__main__":
    import csv
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
    employee_name = response_data2["username"]

    # Export the task data to JSON format.
    json_data = export_to_json(employee_id, completed_tasks)

    # Write the JSON data to a file.
    with open(f"{employee_id}.json", "w") as outfile:
        outfile.write(json_data)
