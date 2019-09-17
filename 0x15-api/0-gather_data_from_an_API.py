#!/usr/bin/python3
""" script that give information employee
    with  REST API
"""

import requests
import sys

URL = 'https://jsonplaceholder.typicode.com/todos'
params = {"userId": sys.argv[1]}
URL2 = 'https://jsonplaceholder.typicode.com/users'
params2 = {"id": sys.argv[1]}
req_datos = requests.get(URL, params=params).json()
req_user = requests.get(URL2, params=params2).json()

new_list = []
for x in req_datos:
    if x.get('completed') is True:
        new_list.append("{}".format(x.get('title')))

print("Employee {} is done with tasks({}/{}):"
      .format(req_user[0].get('name'),
              len(new_list), len(req_datos)))

for x in new_list:
    print("\t {}".format(x))

