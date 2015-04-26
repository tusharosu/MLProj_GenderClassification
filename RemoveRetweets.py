wordFile = open('Datasets\\Trainingtweets_without_RT.txt', 'w')
wordFile1 = open('Datasets\\Testingtweets_without_RT.txt', 'w')
with open('RawTweetsTraining.txt') as f:
    for line in f:
        if not'RT' in line:
            wordFile.write(line)
with open('RawTweetsTesting.txt') as f:
    for line in f:
        if not'RT' in line:
            wordFile1.write(line)