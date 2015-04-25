wordFile = open('TweetsTemp.txt', 'w')
count=0
with open('TempList.txt') as f:
    for line in f:
        if '@' in line:
            wordFile.write(line+'\n')