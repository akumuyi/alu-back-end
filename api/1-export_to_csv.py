#!/usr/bin/python3
import csv  # Import the CSV module

"""
This script fetches and analyzes completed tasks for a
given employee from a remote API and exports the data in CSV format.
It takes an employee's ID as a command-line argument, retrieves the
tasks associated with that employee, displays the number of completed
tasks, and exports the data to a CSV file in the requested format.
Usage:
    $ python script_name.py employee_id
Args:
    employee_id (int): The ID of the employee for whom you want to
    analyze completed tasks and export to CSV.
"""

if __name__ == "__main__":
    import json
    import sys
    import urllib.request
    # Get the employee's ID from the sys module and format it into the URL
    # https://jsonplaceholder.typicode.com/users/{employee_id}
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
    # Get Employee Name
    employee_name = response_data2["name"]
    # Print output in the requested format; 'Employee EMPLOYEE_NAME is
    # done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):'
    print(f"Employee {employee_name} is done with
          tasks({len(completed_tasks)}/{len(response_data1)}): ")
    # Create a CSV file and write the data to it
    with open(f"{employee_id}.csv", 'w', newline='') as csvfile:
        fieldnames = ["USER_ID", "USERNAME",
                      "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()  # Write the header row
        # Write data for each completed task
        for task in completed_tasks:
            writer.writerow({
                "USER_ID": employee_id,
                "USERNAME": employee_name,
                "TASK_COMPLETED_STATUS": task['completed'],
                "TASK_TITLE": task['title']
            })
