wordFile = open('Datasets\\tweets_without_RT.txt', 'w')
with open('RawTweets.txt') as f:
    for line in f:
        if not'RT' in line:
            wordFile.write(line)