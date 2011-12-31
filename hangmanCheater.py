import os,sys
import re

class HangmanCheater(object):
	def __init__(self, dictionary, patternInitial=None, impossibleCharsInitial=None):
		self.dictionary = dictionary
		self.pattern = patternInitial
		self.impossibleChars = impossibleCharsInitial

	def updatePattern(self, newPattern):
		if re.search(newPatter, "!^[a-z_]+$"):
			raise VauleError("Not a valid pattern. Patterns must only contain lowercase letters and underscores")
		else:
			self.pattern = newPattern
	
	def addImpossibleChar(self, newImpossibleChar):
		if not newImpossibleChar in string.ascii_lowercase:
			raise VauleError("Not a valid impossible char. Impossible chars must be lowercase letters")
		else:
			if not newImpossibleChar in self.impossibleChars:
				self.impossibleChars.append(newImpossibleChar)

	def getPossibilities(self):
		possibleWords = []
		for word in self.dictionary:
			if self.__stringContainsAny(word, self.impossibleChars):
				continue #do bother if the word contains black listed chars
			if self.__isPossible(self.pattern, word):
				possibleWords.append(word)
		return possibleWords


	def __isPossible(self, pattern, word):
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
	
	
	def __stringContainsAny(self, str, chars):
		for char in chars:
			if char in str:
				return True
		return False


if __name__ == '__main__':
	#grab dictionary
	DICTPATH = "resources/dictionaries/master.txt"
	wordlist = open(DICTPATH,"r").read().split("\n")

	#Ask for pattern and blacklisted chars
	notLetters = list(raw_input("What letters are not in the word: "))
	pattern = raw_input("Enter current know letters and blanks: ")
	
	hangmanGame = HangmanCheater(wordlist,pattern,notLetters)
	print hangmanGame.getPossibilities()

