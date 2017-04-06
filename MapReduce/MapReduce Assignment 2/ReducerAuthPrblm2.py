#!/usr/bin/python
import sys

if __name__ == "__main__":

   currentAuth = None
   author = None
   authDict = {}
   # stdin input from the mapper
   for line in sys.stdin:
   #fnameOutput=open('MapperOutput.txt','r').readlines()
   #for line in fnameOutput:
	#strip leading and trailing white spaces
	line = line.strip()
	# split title word and author Name from input line from std in from mapper.py
        titalWord = line.split('\t')[1]
	tWord = titalWord.strip()	
	author = line.split('\t')[0]
	author = author.strip()
	#check if author name does exixtis in the finam author Directory if not then create new enty for author and add the title word with the count = 1.
        if author in authDict :
		#if author name does exists then check if title word exits for that perticular author,if so increament the county for the title word else add new title word with count = 1
		if tWord not in authDict[author] :
		      authDict[author][tWord]=1
		else:
		      authDict[author][tWord]+=1
			
        else :
	
		authDict[author] = {}
		authDict[author][tWord]=1

   # do not forget to output the last word if needed!
   if currentAuth == author:
	if author in authDict :
		if tWord not in authDict[author] :
		      authDict[author][tWord]=1
		else:
		      authDict[author][tWord]+=1
			
        else :
	
		authDict[author] = {}
		authDict[author][ftWord]=1

   for author in authDict:
       #print the author name and the dictionary containing title word along with the count to the stdout for printing it to output path on successful run od mapper.py and reducer.py
	sys.stdout.write("{0}  \t  {1}\n".format(author,authDict[author]))
	
