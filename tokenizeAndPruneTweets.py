import sys
import string
import unicodedata
import unidecode
from pruneWordLists import skipLettersList,skipSubstrList, \
stripSubstringList,stripCharacters, \
checkWholeWordToSkip,checkLetterToSkip,checkSubstrToSkip, \
stripChars, splitWord

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

def groupSameWords(outFileName,filename):
	readFile = open(outFileName, 'r')
	# writeFile = open('Datasets\pruned_final.txt', 'w')
	writeFile2 = open(filename+'_final_prune.txt', 'w')
	
	wordToCountMap_Final={}
	count = 0
	for line in readFile:
		wordToCountMap = {}
		wordsList = line.split('\t')
		if(len(wordsList)==1):
			wordsList = line.split(' \t')
		curWordList=wordsList[0].split()
		for i in range(0,len(curWordList)-1):
			tmpWrdLst1=[]
			tmpWrdLst2=[]
			curWord =  curWordList[i].lower()
			curWord= unicode(curWord, "utf-8")
			curWord = unidecode.unidecode(curWord)

			curWord = stripChars(curWord)

			if not curWord or len(curWord) == 1:
				continue
			curWord = curWord.lower()
			wordsAfterSplitList = splitWord(curWord)
			for item in wordsAfterSplitList:
				tmpWrdLst1.append(item)

			# Enable this to get distinct word counts
			# tmpWrdLst1 = list(set(tmpWrdLst1))
			for word in tmpWrdLst1:
				if wordToCountMap.has_key(word):
					wordToCountMap[word] += 1
				else:
					wordToCountMap[word] = 1
				if wordToCountMap_Final.has_key(word):
					if 'M' in wordsList[1]:
						wordToCountMap_Final[word][1] += 1
					else:
						wordToCountMap_Final[word][0] += 1
				else:
					wordToCountMap_Final[word] = [0,0]
					if 'M' in wordsList[1]:
						wordToCountMap_Final[word][1] = 1
					else:
						wordToCountMap_Final[word][0] = 1

		# tempList = [[]]
		tempList2=[[]]
		
		for key,value in wordToCountMap.iteritems():
			# tempList.append([key,int(value)])
			tempList2.append(str(key))
		if tempList2:
			# tempList.pop(0)
			tempList2.pop(0)
			# tempList.sort(key=lambda x: x[0], reverse=False)
			tempList2.sort(key=lambda x: x[0], reverse=False)
			# if len(tempList) !=0:
			# 	for i in range(0,len(tempList)):
			# 		if i==len(tempList)-1:
			# 			# writeFile.write(str(tempList[i]))
			# 		else:
			# 			# writeFile.write(str(tempList[i]) + ' ')	
			# 	# writeFile.write('\t'+ wordsList[1])
			if len(tempList2) !=0:
				for i in range(0,len(tempList2)):
					if i==len(tempList2)-1:
						writeFile2.write(str(tempList2[i]))
					else:
						writeFile2.write(str(tempList2[i]) + ' ')
				writeFile2.write('\t'+ wordsList[1])
	if 'Trainingtweets' in filename:
		writeFile3 = open('Datasets\\1gm_trng_male_pruned_dist.txt','w')
		writeFile4 = open('Datasets\\1gm_trng_female_pruned_dist.txt','w')
		tempList3=[[]]
		tempList4=[[]]
		for key,[value1,value2] in wordToCountMap_Final.iteritems():
			tempList3.append([int(value2),key])
			tempList4.append([int(value1),key])		
	
		if tempList3 and len(tempList3)!=0 and tempList4 and len(tempList4)!=0:
				tempList3.pop(0)
				tempList3.sort(key=lambda x: x[0], reverse=True)
				tempList4.pop(0)
				tempList4.sort(key=lambda x: x[0], reverse=True)
				for temp in tempList3:
					key = temp[1]
					MaleCount = temp[0]
					writeFile3.write(str(MaleCount) + '\t' + str(key)+'\n')
				for temp in tempList4:
					key = temp[1]
					FemaleCount = temp[0]
					writeFile4.write(str(FemaleCount) + '\t' + str(key)+'\n')

to_be_pruned_List = ['Datasets\\Trainingtweets_without_RT','Datasets\\Testingtweets_without_RT']
for filename in to_be_pruned_List:
	outFileName = pruneFile(filename)
	groupSameWords(outFileName,filename)