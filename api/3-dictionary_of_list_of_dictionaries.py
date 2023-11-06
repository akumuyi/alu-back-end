#!/usr/bin/python3
"""
Using what you did in the task #0,
extend your Python script to export
data in the JSON format.

Requirements:

Records all tasks from all employees
Format must be: { "USER_ID": [ {"username":
"USERNAME", "task": "TASK_TITLE", "completed":
TASK_COMPLETED_STATUS}, {"username": "USERNAME",
"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
... ], "USER_ID": [ {"username": "USERNAME", "task":
"TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
{"username": "USERNAME", "task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS}, ... ]}

File name must be: todo_all_employees.json
"""
if __name__ == "__main__":
    import json
    import requests
    import sys
    # create your api urls used for making the request
    url1 = f"https://jsonplaceholder.typicode.com/users"
    url2 = f"https://jsonplaceholder.typicode.com/todos"
    request_response1 = requests.get(url1)
    request_response2 = requests.get(url2)
    request_response1 = request_response1.json()
    request_response2 = request_response2.json()
    # get the todo keys for the users
    all_user_keys = request_response2[0].keys()
    # create a dict for storing all users
    # username, title as task, completed
    all_user_json = {}
    user_count = 0
    each_user_todo = 20
    for i in range(0, len(request_response2), each_user_todo):
        new_list = []
        for j in range(i, i+each_user_todo):
            new_dict = {}
            new_dict["username"] = request_response1[user_count]["username"]
            for key in all_user_keys:
                if key != "title" and key != "completed":
                    continue
                if key == "title":
                    new_dict["task"] = request_response2[j][key]
                else:
                    new_dict["completed"] = request_response2[j][key]
            new_list.append(new_dict)
        all_user_json[f'{request_response1[user_count]["id"]}'] = new_list
        user_count += 1
    with open("todo_all_employees.json", 'w', encoding="utf-8") as jsonfile:
        json.dump(all_user_json, jsonfile)
