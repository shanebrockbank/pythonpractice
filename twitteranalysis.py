import tweepy
from textblob import TextBlob

#Authenticate
consumer_key= 'zuOFUOrYxwEBLO61xIwRA2LLr'
consumer_secret= 'WlTbMXVhfO927vy2tkyO2iV4W7B1xie9tvpER4GHR0FIfnVIsY'

access_token='592359921-TFacvXLkzmtXViNvtWDtswG1peAH61KvhHis7kxm'
access_token_secret='ltPtVuXmGSHRvv62Uwg2cfYAMHw1UdeDHrO36qeLp2fa6'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Retrieve Tweets
public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    
    #Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
