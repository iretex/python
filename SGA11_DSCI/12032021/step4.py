# importing the required libraries

from joblib import load
import pandas as pd
# from get_tweets import get_related_tweets

# load the pipeline object
pipeline = load("model/text_classification.joblib")


# function to get results for a particular text query
def requestResults(name):
    # get the tweets text
    tweets = {'tweet_text':name.sample(1).tweet.tolist()}#get_related_tweets(name)
    # get the prediction
    tweets['prediction'] = pipeline.predict(tweets['tweet_text'])
    # get the value counts of different labels predicted
    data = str(pd.DataFrame(tweets).prediction.value_counts()) + '\n\n'
    return data + str(tweets)