#!/usr/bin/python
import sys
import string
import unicodedata
import unidecode

skipLettersList = ['@','\u']
skipSubstrList = ['http:','.com', 'www.', '.me', '.co', '.net', '.org', '.ca', '.tv', 
				  '.in']
skipWordList = []

stripCharacters = '\t\n\r\'\"?~<>.&_-!\\:,'
stripSubstringList = ['\\t','\\n','\\r']

def stripChars(word):
	for item in stripSubstringList:
		if word.startswith(item):						
			word = word[len(item):]
		if word.endswith(item):						
			word = word[:-len(item)]
	word = word.strip(stripCharacters)
	return word

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
	writeTempFile = open("tempFile", 'w')
	wordToCountMap = {}
	for line in writeFile:
		wordsList = line.split('\t')
		curWord = wordsList[1]
		curWord= unicode(curWord, "utf-8")
		curWord = unidecode.unidecode(curWord)
		for item in stripSubstringList:
				if curWord.startswith(item):
					curWord = words[len(item):]
				if curWord.endswith(item):
					curWord = words[:-len(item)]

		curWord = curWord.strip(stripCharacters)
		
		if not '.' in curWord and not '\n' in curWord:
				tmpWrdLst1.append(curWord)
		else:
				dotWordList = curWord.split('.')
				wordListMayHaveNL = [""]
				for item in dotWordList:
					if len(item) > 0:
						nlWordList = item.split('\n')
						for item2 in nlWordList:
							if len(item2) >0:
								print item2
								item2 = stripChars(item2)
								print item2
								tmpWrdLst1.append(stripChars(item2))

		for word in tmpWrdLst1:
			if not word or len(word) == 1:
				if len(word) == 1:
					writeTempFile.write(str(word) + '\n')
				continue
			word = word.lower()
			if wordToCountMap.has_key(word):
				wordToCountMap[word] += int(wordsList[0])
			else:
				wordToCountMap[word] = int(wordsList[0])

	writeFile.truncate()
	writeFile.close()
	writeFile = open(outFileName, 'w')
	tempList = [[]]
	for key,value in wordToCountMap.iteritems():
		tempList.append([int(value), key])

	tempList.pop(0)
	tempList.sort(key=lambda x: x[0], reverse=True)
	for item in tempList:
		writeFile.write(str(item[0]) + '\t' + item[1] + '\n')

def main():
	outFileNameMale = pruneFile('words_1gm_malef_dist', 1)
	groupSameWords(outFileNameMale)
	outFileNameFem = pruneFile('words_1gm_femf_dist', 1)
	groupSameWords(outFileNameFem)

if __name__ == '__main__':
	main()