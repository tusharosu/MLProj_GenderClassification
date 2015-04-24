import sys
import string
import unicodedata
import unidecode
from pruneWordLists import skipLettersList,skipSubstrList,stripCharacters,checkWholeWordToSkip,checkLetterToSkip,checkSubstrToSkip

def pruneFile(filename):
	readFile = open(filename+'.txt', 'r')
	writeFile = open(filename+'_pruned.txt', 'w')
	for line in readFile:
		wordsList = line.split('\t')
		curWordList=wordsList[0].split()
		for i in range(0,len(curWordList)):
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
	writeFile2 = open('pruned_final_onlywords.txt', 'w')
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
		tempList = [[]]
		tempList2=[[]]
		for key,value in wordToCountMap.iteritems():
			tempList.append([key,int(value)])
			tempList2.append(str(key))
		if tempList and tempList2:
			tempList.pop(0)
			tempList2.pop(0)
			tempList.sort(key=lambda x: x[0], reverse=False)
			tempList2.sort(key=lambda x: x[0], reverse=False)
			if len(tempList) !=0:
				for i in range(0,len(tempList)):
					if i==len(tempList)-1:
						writeFile.write(str(tempList[i]))
					else:
						writeFile.write(str(tempList[i]) + ' ')	
				writeFile.write('\t'+ wordsList[1])
			if len(tempList2) !=0:
				for i in range(0,len(tempList2)):
					if i==len(tempList)-1:
						writeFile2.write(str(tempList2[i]))
					else:
						writeFile2.write(str(tempList2[i]) + ' ')
				writeFile2.write('\t'+ wordsList[1])
			

outFileNameMale = pruneFile('myDataModified')
groupSameWords(outFileNameMale)