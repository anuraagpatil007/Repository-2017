#!/usr/bin/python
import sys

if __name__ == "__main__":

   currentWord = None
   word = None
   WordDict = {}
   # stdin input
   for line in sys.stdin:
   #fnameOutput=open('MapperOutput.txt','r').readlines()
   #for line in fnameOutput:
	#Remove leading and trailing whitespaces
	line = line.strip()
	# parse the std input piped from mapper.py
	word = line.split('\t')[0]
	word = word.strip()
	fName = line.split('\t')[1]
	fName = fName.strip()	
        if word in WordDict :
		if fName not in WordDict[word] :
		      WordDict[word][fName]=1
		else:
		      WordDict[word][fName]+=1
			
        else :
	
		WordDict[word] = {}
		WordDict[word][fName]=1

   # do not forget to output the last word if needed!
   if currentWord == word:
	if word in WordDict :
		if fName not in WordDict[word] :
		      WordDict[word][fName]=1
		else:
		      WordDict[word][fName]+=1
	else :
		WordDict[word] = {}
		WordDict[word][fName]=1
   # traverse through the directory to std out the final output to the output directory.
   for word in WordDict:

       sys.stdout.write("{0} \t {1}\n".format(word,WordDict[word]))
	
