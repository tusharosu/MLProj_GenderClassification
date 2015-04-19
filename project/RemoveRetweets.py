wordFile = open('myDataModified.txt', 'w')
with open('myData.txt') as f:
    for line in f:
        if not'RT' in line:
            wordFile.write(line+'\n')