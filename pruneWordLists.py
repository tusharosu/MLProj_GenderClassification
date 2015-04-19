#!/usr/bin/python
import sys

skipLettersList = ['@']
skipSubstrList = ['http','.com', '.me', '.co']

def checkWholeWordToSkip(word):
	retVal = False
	return retVal

def checkLetterToSkip(word):
	retVal = False
	for c in skipLettersList:
		if c in word:
			retVal = True
			break;
	return retVal

def checkSubstrToSkip(word):
	retVal = False
	for c in skipSubstrList:
		if c in word:
			retVal = True
			break;
	return retVal

def pruneFile(filename, index):
	readFile = open(filename+'.txt', 'r')
	writeFile = open(filename+'_pruned.txt', 'w')
	for line in readFile:
		wordsList = line.split('\t')
		cmpWord =  wordsList[index].lower()
		ignore = True
		ignore = checkWholeWordToSkip(cmpWord)
		if ignore == False:
			ignore = checkLetterToSkip(cmpWord)
		if ignore == False:
			ignore = checkSubstrToSkip(cmpWord)
		if ignore == False:
			writeFile.write(line)
	return filename+'_pruned.txt'

def groupSameWords(outFileName):
	writeFile = open(outFileName, 'r+')
	wordToCountMap = {}
	for line in writeFile:
		wordsList = line.split('\t')
		curWord = wordsList[1]
		curWord = curWord.strip('\t\n\r')
		curWord = curWord.lower()
		if wordToCountMap.has_key(curWord):
			wordToCountMap[curWord] += int(wordsList[0])
		else:
			wordToCountMap[curWord] = int(wordsList[0])

	writeFile.truncate()
	writeFile.close()
	writeFile = open(outFileName, 'w')
	tempList = [[]]
	for key,value in wordToCountMap.iteritems():
		tempList.append([int(value), key])

	tempList.pop(0)
	tempList.sort(key=lambda x: x[0], reverse=True)
	for item in tempList:
		writeFile.write(str(tempList[0]) + '\t' + tempList[1] + '\n')

outFileNameMale = pruneFile('words_1gm_malef', 1)
groupSameWords(outFileNameMale)
outFileNameFem = pruneFile('words_1gm_femf', 1)
groupSameWords(outFileNameFem)