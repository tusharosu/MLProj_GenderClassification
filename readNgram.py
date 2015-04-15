#!/usr/bin/python

import sys
count = 0

with open("en.1grams") as f:
	for line in f:
		print line
		print 'end of line'
		count = count +1
		if count == 100:
			break

