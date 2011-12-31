import os,sys


def possibility(pattern,word):
	if not len(pattern) == len(word):
		return False
	for wordChar, patternChar in zip(word, pattern):
		if patternChar == "_": 
			continue
		elif patternChar == wordChar:
			continue
		else:
			return False
	return True


def stringContains(str, chars):
	for char in chars:
		if char in str:
			return True
	return False


DICTPATH = "resources/dictionaries/master.txt"

wordlist = open(DICTPATH,"r").read().split("\n")

possibleWords = []

#Ask for patter
notLetters = list(raw_input("What letters are not in the word: "))
pattern = raw_input("Enter current know letters and blanks: ")


for word in wordlist:
	if stringContains(word,notLetters):
		continue
	if possibility(pattern, word):
		possibleWords.append(word)

print possibleWords
