import json
import simplejson as json
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt
import re
import collections
from collections import Counter
from pylab import *

# @BEGIN main
# @IN tweet @as Tweets
# @OUT matplotlib.pyplot @as plt
# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="yiHz2vJPQmHRIZ3WcAZcbhloY"
consumer_secret="N1kGE6Y46z1KETOpUdMD1wqWQLGI35smz4f48k0wa4C4h9kUYv"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="2670240956-3D795oeGR2BFIbKqVmn1Fdy2mjINAbnBI1Ks4XU"
access_token_secret="WNcDtRDkI6JPv2QsXq5jJ10AwiiawfQNcJrvhXyNqmWye"

# @BEGIN OpenAuthentication
# @IN consumer_key
# @IN consumer_secret
# @IN access_token
# @IN access_token_secret
# @OUT oauth @AS OpenAuthentication
oauth = OAuth(access_token, access_token_secret, consumer_key, consumer_secret)
# @END OpenAuthentication

# Initiate the connection to Twitter Streaming API
# @BEGIN InitiateConnection
# @IN oauth @AS OpenAuthentication
# @OUT twitter_stream @AS ConnectionObject
twitter_stream = TwitterStream(auth=oauth)
# @END InitiateConnection

# Get a sample of the public data following through Twitter
# @BEGIN GetTweets
# @IN twitter_stream @AS ConnectionObject
# @IN track @AS SearchTerm
# @IN language @AS TweetLanguage
# @OUT iterator @AS SampleTweets
iterator = twitter_stream.statuses.filter(track="Cricket", language="en")
# @END GetTweets

# Print each tweet in the stream to the screen 
# Here we set it to stop after getting limited tweets. 
# You don't have to set it to stop, but can continue running 
# the Twitter API to collect data for days or even longer. 
tweet_count = 5

# @BEGIN AnalyseSentiments
# @IN iterator @AS SampleTweets
# @OUT output.csv @AS SentimentsInCSV
for tweet1 in iterator:
    tweet_count -= 1
    
    json_str = json.dumps(tweet1)
    data = json.loads(json_str)
   
    tweet = TextBlob(data["text"])
    # output sentiment polarity
    print(tweet.sentiment.polarity)
        
        # determine if sentiment is positive,negative, or neutral
	# @BEGIN DetermineSentiments
	# @IN tweet.sentiment.polarity @AS SentimentPolarity
	# @OUT sentiment as Sentiments
    if tweet.sentiment.polarity < 0:
        sentiment = "negative"
            
    elif tweet.sentiment.polarity == 0:
        sentiment = "neutral"
           
    else:
        sentiment = "positive"
        #sentimentAnalysis(sentiment)
	# @END DetermineSentiments
	
	# @BEGIN WriteToCSV
	# @IN sentiment as Sentiments
	# @OUT output.csv @AS SentimentFile
    output = open('output.csv','a')
    output.write(sentiment)
    output.write("\n")
    output.close()
    # @END WriteToCSV
	
    #If count reached the limit specified stop getting tweets       
    if tweet_count <= 0:
        break
# @END AnalyseSentiments
        
tweets_data_path = 'output.csv'

tweets_data = []
tweets_file = open(tweets_data_path, "r")


for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue
# @BEGIN CountSentiments
# @IN output.csv @AS SentimentsInCSV
# @OUT cnt @AS PositiveCount
# @OUT cnt1 @AS NegativeCount
# @OUT cnt2 @AS NeutralCount
positive_count = "positive"
cnt = Counter()
words = re.findall(r"\w+itive", open('output.csv').read().lower())
for word in words:
    if word in positive_count:
        cnt[word] += 1
print(cnt)

negative_count = "negative"
cnt1 = Counter()
words = re.findall(r"\w+ative", open('output.csv').read().lower())
for word in words:
    if word in negative_count:
        cnt1[word] += 1
print(cnt1)

neutral_count = "neutral"
cnt2 = Counter()
words = re.findall(r"\w+eutral", open('output.csv').read().lower())
for word in words:
    if word in neutral_count:
        cnt2[word] += 1
print(cnt2)
# @END CountSentiments

# @BEGIN SetPieChartMeasures
# @IN cnt @AS PositiveCount
# @IN cnt1 @AS NegativeCount
# @IN cnt2 @AS NeutralCount
# @OUT explode @AS Explode
# @OUT labels @AS Labels
# @OUT sizes @AS Sizes
# @OUT colors @AS Colors
explode = (0, 0.1, 0) 
labels = 'Positive', 'Negative', 'Neutral'
sizes = [cnt["positive"], cnt1["negative"], cnt2["neutral"]]
colors = ['gold', 'yellowgreen', 'lightcoral']
# @END SetPieChartMeasures

# @BEGIN DrawPieChart
# @IN explode @AS Explode
# @IN labels @AS Labels
# @IN sizes @AS Sizes
# @IN colors @AS Colors
# @OUT matplotlib.pyplot @as plt
plt.pie(sizes, explode=explode, colors=colors,
        autopct='%1.1f%%', startangle=120)
plt.legend(labels, loc=(-0.05, 0.05), shadow=True)
plt.axis('equal')
plt.show()
# @END DrawPieChart
# @END main