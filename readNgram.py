#!/usr/bin/python

import sys
count = 0

wordFile = open('words_2g.txt', 'w')

with open('en.2grams') as f:
	for line in f:
		count = count +1
		if (count <= 5):
			continue;
		word = line.split('\t', 1)[0] + '\n'
		wordFile.write(word)
		
		print "\rProgress  : " + str(count),

print "number of lines : " + str(count)