"""
Just a basic idea of how it might work.
- 
"""

import requests
import threading
import sys
import time


# -1
# Not sure if i will be using this ?????
def find_directories2(url, dirList, max_num_threads):
	temp_packets = []
	total = len(dirList)
	iteration = 0
	_loadbar(iteration, total)
	for i, directory in enumerate(dirList):
		iteration = i
		if len(temp_packets) >= max_num_threads:
			
			_multithreading(temp_packets, url, iteration, total)
			temp_packets = []
		temp_packets.append(directory)
	
	# If any remaining in temp_packet run _multithreading
	_multithreading(temp_packets, url, iteration, total)

# -2
def _multithreading(packet_arr, url, iteration, total):
	thread = threading.Thread(target=__thread_packets(packet_arr, url, iteration, total), args=(1,))
	thread.start()
	

# -3
def __thread_packets(packets, url, iteration, total):
	found = []
	#_loadbar(0, total)
	for i, directory in enumerate(packets):
		test_site = "http://" + url + "/" + directory
		request = requests.get(test_site)
		result = str(request.status_code)
		# Found Connection
		if result == "200":
			found.append('/' + directory)
			# append to found
			print('/' + directory)
			found.append('/' + directory)
		_loadbar(iteration, total)


def get_directory_list(filename):
	with open(filename, "r") as file:
		return file.readlines()

def create_report(filename_output, data):
	with open(filename_output + ".txt", "w") as file:
		for line in data:
			file.write(line + "\n")

def _loadbar(iteration, total, prefix='Progress', suffix='Complete', decimals=1, length=30, fill='#'):
	percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration/float(total)))
	filledlength = int(length * iteration // total)
	bar = fill * filledlength + '-' * (length - filledlength)
	print(f'\r{prefix}|{bar}|{percent}% {suffix}', end='\r')

def main():
	url = 'www.karlduggan.com'
	# temp example with a list
	dirList = get_directory_list("directory-list.txt")

	find_directories2(url, dirList[:30], 3)


if __name__ == "__main__":
	main()
