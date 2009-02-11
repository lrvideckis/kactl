#!/usr/bin/env python
# encoding: utf-8

# Source code preprocessor for KACTL building process.
# Written by Håkan Terelius, 2008-11-24

import sys
import getopt

language = None
caption = None

def escape(input):
	input = input.replace('\\','\\\\')
	input = input.replace('_','\_')
	return input

def processcpp():
	global caption
	print "\\kactlref{"+escape(caption)+"}"
	print "\\begin{lstlisting}[caption={"+escape(caption)+"}]"
	try:
		while True:
			line = raw_input()
			print line
	except:
		pass
	print "\\end{lstlisting}"
	
def processjava():
	print "processjava()"
	return
	
def processps():
	global caption
	print "\\kactlref{"+escape(caption)+"}"
	print "\\begin{lstlisting}[language=TeX,caption={"+escape(caption)+"}]"
	try:
		while True:
			line = raw_input()
			print line
	except:
		pass
	print "\\end{lstlisting}"

def getlang(input):
	print "getlang("+ input +") = " + input.rsplit('.',1)[1]
	return input.rsplit('.',1)[-1]

def getfilename(input):
	return input.rsplit('/',1)[-1]

def main(argv=None):
	global language, caption
	if argv is None:
		argv = sys.argv
	try:
		opts, args = getopt.getopt(argv[1:], "ho:i:l:c:", ["help", "output=", "input=", "language=", "caption="])	
		for option, value in opts:
			if option in ("-h", "--help"):
				print "This is the help section for this program"
				print
				print "Available commands are:"
				print "\t -o --output"
				print "\t -h --help"
				print "\t -i --input"
				print "\t -l --language"
				return
			if option in ("-o", "--output"):
				sys.stdout = open(value, "w")
			if option in ("-i", "--input"):
				sys.stdin = open(value)
				if language == None:
					language = getlang(value)
				if caption == None:
					caption = getfilename(value)
			if option in ("-l", "--language"):
				language = value
			if option in ("-c", "--caption"):
				caption = value
				
		if language == "cpp" or language == "cc" or language == "c":
			processcpp()
		elif language == "java":
			processjava()
		elif language == "ps":
			processps()
		else:
			raise ValueError("Unkown language: " + str(language))
	except (ValueError, getopt.GetoptError, IOError), err:
		print >> sys.stderr, str(err)
		print >> sys.stderr, "\t for help use --help"
		return 2


if __name__ == "__main__":
	sys.exit(main())
