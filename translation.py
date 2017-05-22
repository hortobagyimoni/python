#! /usr/bin/python
import sys, re, exceptions, cStringIO

class Error(Exception):
    pass

class MyError(Error):
	def __init__(self, value):
		self.value = value

	def __str__(self):
		return repr(self.value)

class Translator:

	def __init__(self, dictionary):
		if not(isinstance(dictionary, dict)):
			raise MyError('Translator init: Not input dictionary type')
		self.dictionary = dictionary

	def __str__(self):
		return str(self.dictionary)

	def addElement(self, newElement):
		self.dictionary.update(newElement)

	def translation(self, input, output):
		for lb in input:
			linesB = lb.split(' ')
			for x in range(len(linesB)):
				if linesB[x] in self.dictionary:
					linesB[x] = self.dictionary[linesB[x]]
				elif linesB[x][:-2] in self.dictionary:
					linesB[x] = self.dictionary[linesB[x][:-2]] + ".\n"
			output.write((" ").join(linesB))

	def reTranslation(self, input, output):
		for lb in input.getvalue().split("\n"):
			linesB = lb.split(' ')
			for x in range(len(linesB)):
				if linesB[x] in self.dictionary.values():
					linesB[x] = self.dictionary.keys()[self.dictionary.values().index(linesB[x])]
				elif linesB[x][:-1] in self.dictionary.values():
					linesB[x] = self.dictionary.keys()[self.dictionary.values().index(linesB[x][:-1])] + ".\n"
			output.write((" ").join(linesB))
	

myDict = {"The" : "A", "sun": "nap", "shining" : "sut", "wind" : "szel", "not" : "nem", "blowing" : "fuj"}
inputF = cStringIO.StringIO()
inputF.write('A nap is sut.\nA szel nem fuj.\n')
outputF = cStringIO.StringIO()

try:
	print "TEST: Not input dictionary type"
	tlError = Translator("Test\n")
except MyError as me:
	print me
finally:
	print "\n\nSOLUTION:\n"
	tl = Translator(myDict)

tl.reTranslation(inputF, outputF)
print outputF.getvalue()

tl.translation(outputF, inputF)
print inputF.getvalue()

tl.addElement( { "apple" : "alma" } )
print tl