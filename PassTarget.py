from itertools import permutations, product
import sys, os
"""
Cartesian product.
"""

def welcome():
	os.system('clear')
	print(
	"""
	 _____           _______                   _   
	|  __ \         |__   __|                 | |  
	| |__) |_ _ ___ ___| | __ _ _ __ __ _  ___| |_ 
	|  ___/ _` / __/ __| |/ _` | '__/ _` |/ _ \ __|
	| |  | (_| \__ \__ \ | (_| | | | (_| |  __/ |_ 
	|_|   \__,_|___/___/_|\__,_|_|  \__, |\___|\__|
	                                 __/ |         
	                                |___/ 
	Version 0.5         
	"""
		)
	print("How to use:\n")
	print("Create a permuation wordlist and find the password.")
	print("Enter the fragments of the password known and\nenter ? for missing the characters.\n")
	return

def get_word():
	word = input("Enter the known password fragments: ")
	return word

def get_number_Repetition():
	repeats = int(input("Enter the number of repetitions: "))
	print()
	return repeats

def get_number_of_permutations(n,r):
	""" 
	n : The number of possible characters
	r : The number of postions 
	"""
	if r > 1:
		return (n ** r) - n
	else:
		return (n ** r)

def save_output(filename, wordlist):
	wordlist_length = len(wordlist)
	_loadbar(0, wordlist_length)
	with open(filename + ".txt", "w") as file:
		for i, line in enumerate(wordlist):
			file.write(line + "\n")
			_loadbar(i+1, wordlist_length)

def all_chars(repeats):
	numbers = [chr(i) for i in range(48,57 + 1) ]
	up_letters = [chr(i) for i in range(65,90 + 1)]
	low_letters = [chr(i) for i in range(97,122 + 1)]
	all_char = numbers + up_letters + low_letters

	for _ in range(repeats):
		all_char = all_char + all_char
	return all_char 

def getTargets(word):
	targets = []
	length_count = 0
	for i in range(len(word)):
		if word[i] == "?":
			targets.append(i)
			length_count += 1
	return targets, length_count

def create_combinations(list_of_char,length_of_set, total_iterations):
	_loadbar(0, total_iterations)
	perm = permutations(list_of_char, length_of_set)
	combinations = []
	count = 0
	for i, idx in enumerate(perm):
		combinations.append(idx)
		count += 1
		_loadbar(i + 1, total_iterations)
	
	return combinations

def create_wordlist(word, combinations, points):
	wordlist = []
	wordToList = list(word)
	for seq in combinations:
		for i in range(len(points)):
			wordToList[points[i]] = seq[i]
		password = "".join(wordToList)
		wordlist.append(password)

	return wordlist

def check_entry(length, num_iterations, repeats):
	if length > 3:
		print('**************************************************************')
		print('This may take some time as permutations set it greater than 3.')
		print(f'The total number of iteration would be {str(num_iterations)} \n')
		user_request = input('Do you want to continue, y/n: ')
		if user_request == 'n':
			return False
	if repeats > length:
		print('Repetition can not be greater than questionables unknowns!')
		return False

def _loadbar(iteration, total, prefix='Progress', suffix='Complete', decimals=1, length=30, fill='#'):
	percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration/float(total)))
	filledlength = int(length * iteration // total)
	bar = fill * filledlength + '-' * (length - filledlength)
	print(f'\r{prefix}|{bar}|{percent}% {suffix}', end='\r')
	

def main():
	welcome()
	word = get_word()
	repeats = get_number_Repetition()
	all_char = all_chars(repeats)
	points, length = getTargets(word)
	num_iterations = get_number_of_permutations(len(all_char), length)

	result = check_entry(length, num_iterations, repeats)
	if result == False:
		sys.exit()

	combinations = create_combinations(all_char, length, num_iterations)
	wordlist = create_wordlist(word, combinations, points)
	
	save_output("wordlist", wordlist)

	print("\n\n**** Completed ****\n")

if __name__ == "__main__":
	main()





