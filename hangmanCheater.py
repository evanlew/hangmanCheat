import os,sys
import re
import string

class HangmanCheater(object):
	def __init__(self, dictionary, patternInitial=None, impossibleCharsInitial=None):
		self.dictionary = dictionary

		if patternInitial == None:
			self.pattern = []
		else:
			self.updatePattern(patternInitial)

		if impossibleCharsInitial == None:
			self.impossibleChars = []
		else:
			self.addImpossibleChar(impossibleCharsInitial)

	def updatePattern(self, newPattern):
		if not re.match("^[a-z|_]+$", newPattern):
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
				if wordChar in pattern:
					return False
				else:
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
