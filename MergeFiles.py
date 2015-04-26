import sys
import string
import unicodedata
import unidecode

def CreateDataSet(featureFileList,filename2):
	
	
	for filename in featureFileList:
		wordMap = {}		
		featureList=[]
		c=0
		wordList=[]
		probList=[]
		readFile1 = open(filename+'.txt', 'r')
		readFile2 = open(filename2+'.txt', 'r')	

		writeFile1 = open(filename+'_probablility.txt', 'w')
		writeFile2 = open(filename+'_featureSet.txt', 'w')

		for line in readFile1:	
			featureSet = line.split('\t')
			word=featureSet[0]
			prob=featureSet[1]
			wordList.append(word)
			wordMap[word] = c
			c=c+1
			probList.append(prob)
			writeFile1.write(prob+'\n')
	
		for i in range(0,len(wordList)+1):
			featureList.append(0)

		for line in readFile2:
			indexList=[]		
			trainingSet = line.split('\t')
			if len(trainingSet) != 2:
				continue
			tokenizedTweets=trainingSet[0]
			wordList2=tokenizedTweets.split(" ")
			for word2 in wordList2:
				if wordMap.has_key(word2):
					index = wordMap[word2]
					indexList.append(index)
					featureList[index] = 1
			if 'M' in trainingSet[1]:
				Male=1
			else:
				Male=2
			featureList[len(wordList)] = Male
			for item in featureList:
				writeFile2.write(str(item))
			for ind in indexList:
				featureList[ind]=0

featureFileList=[]
for i in range(1,len(sys.argv)-1):
	featureFileList.append('Datasets\\'+sys.argv[i])
filename2 = 'Datasets\\'+sys.argv[len(sys.argv)-1]

CreateDataSet(featureFileList,filename2)

