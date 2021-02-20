from itertools import permutations
import sys

"""
Any thing above a range of 5 will take much longer to calculate.
Note! if the range is above 5 confirm with teh user if they wish to continue.
"""

def save_output(filename, wordlist):
	with open(filename + ".txt", "w") as file:
		for line in wordlist:
			file.write(line + "\n")

def all_chars():
	numbers = [chr(i) for i in range(48,57 + 1) ]
	up_letters = [chr(i) for i in range(65,90 + 1)]
	low_letters = [chr(i) for i in range(97,122 + 1)]
	all_char = numbers + up_letters + low_letters
	return all_char

def getTargets(word):
	targets = []
	length_count = 0
	for i in range(len(word)):
		if word[i] == "?":
			targets.append(i)
			length_count += 1
	return targets, length_count

def create_combinations(list_of_char,length_of_set):
	perm = permutations(list_of_char, length_of_set)
	combinations = []
	for idx in perm:
		combinations.append(idx)
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

def main():
	word = str(inputWord)

	all_char = all_chars()
	points, length = getTargets(word)
	combinations = create_combinations(all_char, length)
	wordlist = create_wordlist(word, combinations, points)

	save_output("wordlist_temp", wordlist)
if __name__ == "__main__":
	inputWord = sys.argv[1]
	main()





