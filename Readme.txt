Execute the following python commands:

>>python -m RemoveRetweets
This will remove retweets from the text file "RawTweetsTraining.txt" and "RawTweetsTesting.txt" and create 2 new files "Trainingtweets_without_RT.txt" and "Testingtweets_without_RT.txt"

>>python -m tokenizeAndPruneTweets
This will create the required 2 files "Trainingtweets_without_RT_final_prune.txt" and "Testingtweets_without_RT_final_prune.txt" which contains the tweets pruned and cleaned up, and the file "1gm_trng_tweets.txt" which conatins the words with female user count and male user count from the collected "Trainingtweets_without_RT_final_prune".

>>python -m MergeFiles fs_remainingWords Trainingtweets_without_RT_final_prune
This will give us the 2 important files:
"fs_remainingWords_featureSet.txt" - FeatureSet for 1 grams and collected
"fs_remainingWords_probablility.txt" - probablity for 1 gram females
