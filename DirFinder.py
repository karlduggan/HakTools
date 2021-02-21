"""
Just a basic idea of how it might work.
- 
"""

import requests
import threading
import sys

url = 'www.bbc.co.uk'
# temp example with a list
dirList = ['bla','foo','robots.txt']

count = 0
for directory in dirList:
	site = 'http://' + url + '/' + directory
	request = requests.get(site)
	result = request.status_code
	if result == 200:
		print('/' + directory)
	count += 1
	print(count)
