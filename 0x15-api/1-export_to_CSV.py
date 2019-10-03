#!/usr/bin/python3
""" script that give information employee with  REST API """
import requests
import sys
import csv

try:
	URL = 'https://jsonplaceholder.typicode.com/todos?userId=' + sys.argv[1]
	params = {"userId": sys.argv[1]}
	URL2 = 'https://jsonplaceholder.typicode.com/users/' + sys.argv[1]
	req_datos = requests.get(URL).json()
	req_user = requests.get(URL2).json()

	file = sys.argv[1] + ".csv"
	new_list = []
	for x in req_datos:
		x['username'] = req_user['username']
		sec_list = []
		sec_list.append(x['userId'])
		sec_list.append(x['username'])
		sec_list.append(x['completed'])
		sec_list.append(x['title'])
		new_list.append(sec_list)

	csv.register_dialect('quotes', quoting=csv.QUOTE_ALL, skipinitialspace=True)

	with open(file, 'w') as f:
		writer = csv.writer(f, dialect='quotes')
		for x in new_list:
			writer.writerow(x)
	f.close()

except Exception as er:
	print(er)
