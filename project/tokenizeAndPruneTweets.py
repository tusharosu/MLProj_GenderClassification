import sys
import string
import unicodedata
import unidecode
import pruneWordLists
from pruneWordLists import skipLettersList,skipSubstrList,stripCharacters,checkWholeWordToSkip,checkLetterToSkip,checkSubstrToSkip

def pruneFile(filename):
	readFile = open(filename+'.txt', 'r')
	writeFile = open(filename+'_pruned.txt', 'w')
	for line in readFile:
		wordsList = line.split('\t')
		curWordList=wordsList[0].split()
		for i in range(0,len(curWordList)-1):
			cmpWord =  curWordList[i].lower()
			ignore = True
			ignore = checkWholeWordToSkip(cmpWord)
			if ignore == False:
				ignore = checkLetterToSkip(cmpWord)
			if ignore == False:
				ignore = checkSubstrToSkip(cmpWord)
			if ignore == False:
				if i==len(curWordList)-1:
					writeFile.write(curWordList[i])
				else:
					writeFile.write(curWordList[i]+' ')
		writeFile.write('\t'+ wordsList[1])
	return filename+'_pruned.txt'

def groupSameWords(outFileName):
	readFile = open(outFileName, 'r')
	writeFile = open('pruned_final.txt', 'w')
	count = 0
	for line in readFile:
		wordToCountMap = {}
		wordsList = line.split('\t')
		if(len(wordsList)==1):
			wordsList = line.split(' \t')
		curWordList=wordsList[0].split()
		for i in range(0,len(curWordList)-1):
			curWord =  curWordList[i].lower()
			curWord= unicode(curWord, "utf-8")
			curWord = unidecode.unidecode(curWord)
			curWord = curWord.strip(stripCharacters)
			if not curWord or len(curWord) == 1:
				continue
			curWord = curWord.lower()
			if wordToCountMap.has_key(curWord):
				wordToCountMap[curWord] += 1
			else:
				wordToCountMap[curWord] = 1
		tempList = []
		for key,value in wordToCountMap.iteritems():
			tempList.append([key,int(value)])
		if tempList:
			for i in range(0,len(tempList)-1):
				if i==len(curWordList)-1:
					writeFile.write(str(tempList[i]))
				else:
					writeFile.write(str(tempList[i]) + ' ')
			writeFile.write('\t'+ wordsList[1])

outFileNameMale = pruneFile('myDataModified')
groupSameWords(outFileNameMale)