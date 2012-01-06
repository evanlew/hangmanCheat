import os,sys

class guessSuggestion(object):
	@classmethod
	def getBestChar(self, possibleWords):
		if type(possibleWords) is not list and type(possibleWords) is not str:
			raise TypeError("Argument must be a list or a string")
		
		charFreq = {}
		for char in ''.join(possibleWords):
			if char in charFreq.keys():
				charFreq[char] = charFreq.get(char) + 1
			else:
				charFreq[char] = 1
		return max(charFreq, key = charFreq.get)
