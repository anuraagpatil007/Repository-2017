#!/usr/bin/python

import sys
import string
import os
#from stop_words import get_stop_words


# dictionary to store the words as key and the value as list of the files that contain those words.
WordDict = dict()
fileList = list()

if __name__ == "__main__":
  
   # to get the filename which is being processed by the mapper.py
   try:
      filename = os.getenv('map_input_file')
   except KeyError:
      filename = os.getenv('map_input_file')
   #to extract the file name from the whole file path  
   fName= filename.split('/')[-1]

      
      
   #fileW=open("MapperOutput.txt",'w+')
   #to get std input from the files through the -input path
   for line in sys.stdin:
 	#fileData=open(filename,'r').read()
	#split and get the words from every line 
	for word in line.split():
                #strip leading and trailing white spaces from words and remove punctuations
		word = word.strip()
		word = word.translate(None, string.punctuation)
		#print out the word and corresponding file name to std out for further processing to be done by Reducer.	
		sys.stdout.write("{0} \t {1}\n".format(word,fName))

