#!/usr/bin/python
import sys

count = 0

wordFile = open('words_1gm.txt', 'w')
wordFile_mf = open('words_1gm_malef.txt', 'w')
wordFile_ff = open('words_1gm_femf.txt', 'w')
wordFile2 = open('words_2gm.txt', 'w')

sortedFreqListFem = [[]]
sortedFreqListMale = [[]]

with open('en.1grams') as f:
    for line in f:
        count = count +1
        if (count <= 5):
            continue
        word = line.split('\t');
        wordFile.write(word[0]+'\t')
        femaleFrequency=0
        maleFrequency=0

        for i in range(1,1198,6):
            femaleFrequency = femaleFrequency + int(word[i]);
        for i in range(3,1198,6):
            maleFrequency = maleFrequency + int(word[i]);

        # skip words that have 0 freq count for both male and female
        if femaleFrequency > 0 or maleFrequency > 0:
            sortedFreqListFem.append([femaleFrequency, word[0]])
            sortedFreqListMale.append([maleFrequency, word[0]])

        wordFile.write(str(femaleFrequency)+'\t'+str(maleFrequency) + '\n')
        print "\rProgress  : " + str(count),

sortedFreqListFem.pop(0);
sortedFreqListMale.pop(0);

sortedFreqListFem.sort(key=lambda x: x[0], reverse=True)
sortedFreqListMale.sort(key=lambda x: x[0], reverse=True)

for item in sortedFreqListMale:
    wordFile_mf.write(str(item[0]) + '\t' + str(item[1]) + '\n')
for item in sortedFreqListFem:
    wordFile_ff.write(str(item[0]) + '\t' + str(item[1]) + '\n')

# print "\n Starting 2grams....\n"
# count=0
# with open('en.2grams') as f:
#     for line in f:
#         count = count +1
#         if (count <= 5):
#             continue;
#         word = line.split('\t');
#         wordFile2.write(word[0]+'\t')
#         femaleFrequency=0
#         maleFrequency=0
#         for i in range(1,1198,6):
#             femaleFrequency = femaleFrequency + int(word[i]);
#         for i in range(3,1198,6):
#             maleFrequency = maleFrequency + int(word[i]);
#         wordFile2.write(str(femaleFrequency)+'\t'+str(maleFrequency) + '\n')
#         print "\rProgress  : " + str(count),