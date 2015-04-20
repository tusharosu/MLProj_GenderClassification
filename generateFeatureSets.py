#!/usr/bin/python
from __future__ import division
import sys

def calcProb(key, wordCountDict):
	return ((wordCountDict[key][0]) / (wordCountDict[key][0] + wordCountDict[key][1]))

def generateFreqBelowThresholdFS(wordCountDict, threshold):
	keysToDeleteList = []
	f = open('fs_wordsBelowThreshold.txt', 'w')
	for key in wordCountDict:
		if wordCountDict[key][0] < threshold and wordCountDict[key][1] < threshold:
			prob = calcProb(key, wordCountDict)
			f.write(key + '\t' + str(prob) + '\n')
			keysToDeleteList.append(key)

	for key in keysToDeleteList:
		wordCountDict.pop(key, None)

	return wordCountDict


def generateObsceneJunkWordsFS(wordCountDict):
	substrWordsList = ['nigga', 'fuck', 'sex']
	keysToDeleteList = []
	f = open('fs_obsceneJunkWords.txt', 'w')
	for key in wordCountDict:
		for w in substrWordsList:
			if w in key:
				prob = calcProb(key, wordCountDict)
				f.write(key + '\t' + str(prob) + '\n')
				keysToDeleteList.append(key)

	for key in keysToDeleteList:
		wordCountDict.pop(key, None)

	return wordCountDict


def generateHashtagsFS(wordCountDict):
	keysToDeleteList = []
	f = open('fs_wordsWithHashtags.txt', 'w')
	for key in wordCountDict:
		if key[0] == '#':
			prob = calcProb(key, wordCountDict)
			f.write(key + '\t' + str(prob) + '\n')
			keysToDeleteList.append(key)

	for key in keysToDeleteList:
		wordCountDict.pop(key, None)

	return wordCountDict


def main():
	# A dictionary with word as the key
	# and a list as value
	# list has two coloumns : [female freq, male freq]
	femFileName = 'words_1gm_femf_dist_pruned.txt'
	maleFileName = 'words_1gm_malef_dist_pruned.txt'
	wordCountDict = {}
	femFile = open(femFileName, 'r')
	for line in femFile:
		line = line.rstrip('\n')
		words = line.split('\t')
		if wordCountDict.has_key(words[1]):
			wordCountDict[words[1]][0] = int(words[0])
		else:
			wordCountDict[words[1]] = [int(words[0]), 0]

	maleFile = open(maleFileName, 'r')
	for line in maleFile:
		line = line.rstrip('\n')
		words = line.split('\t')
		if wordCountDict.has_key(words[1]):
			wordCountDict[words[1]][1] = int(words[0])
		else:
			wordCountDict[words[1]] = [0, int(words[0])]

	# Generate all the data sets
	print 'Number of words in dict : ' + str(len(wordCountDict))

	print 'Writing words below threshold words feature set...',
	wordCountDict = generateFreqBelowThresholdFS(wordCountDict, 10)
	print 'done'
	print 'Number of remaining words in dict : ' + str(len(wordCountDict))

	print 'Writing obscene/junk words feature set...',
	wordCountDict = generateObsceneJunkWordsFS(wordCountDict)
	print 'done'
	print 'Number of remaining words in dict : ' + str(len(wordCountDict))

	print 'Writing hashtags words feature set...',
	wordCountDict = generateHashtagsFS(wordCountDict)
	print 'done'
	print 'Number of remaining words in dict : ' + str(len(wordCountDict))

	print 'Writing remaining words feature set...',
	f = open('fs_remainingWords.txt', 'w')
	for key in wordCountDict:
		prob = calcProb(key, wordCountDict)
		f.write(key + '\t' + str(prob) + '\n')
	print 'done'

	
if __name__ == "__main__":
	main()