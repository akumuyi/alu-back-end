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

if __name__ == "__main__":
    import json
    import sys
    import urllib.request
    import requests
    import csv
    # using this url https://jsonplaceholder.typicode.com/todos/
    # add a query string of userId = 2 using the requests module
    url1 = "https://jsonplaceholder.typicode.com/todos"
    url2 = f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}"
    payload = {"userId": sys.argv[1]}
    # a single variable used to accept the response
    # after request is made using the module
    request_response1 = requests.get(url1, params=payload)
    request_response2 = requests.get(url2)
    request_response1 = request_response1.json()
    request_response2 = request_response2.json()
    # file name depends on ID
    filename2 = f"{sys.argv[1]}.json"
    # create a dictionary having the key "userid" and
    # the value should be an empty list
    user_data = {f'{request_response2["id"]}': []}
    # now get user keys
    user_keys = list(request_response1[0].keys())
    # iterate over request_response1 and request_response2 to get
    # a dictionary of task/title, completed, username
    # keyvalue pairs
    for data in request_response1:
        new_dict = {}
        for key in user_keys:
            if key != "title" and key != "completed":
                continue
            if key == "title":
                new_dict["task"] = data[key]
            else:
                new_dict[key] = data[key]
        new_dict["username"] = request_response2["username"]
        user_data.get(f"{sys.argv[1]}").append(new_dict)
    with open(filename2, 'w', encoding='utf-8') as jsonfile:
        json.dump(user_data, jsonfile)
