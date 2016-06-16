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

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="yiHz2vJPQmHRIZ3WcAZcbhloY"
consumer_secret="N1kGE6Y46z1KETOpUdMD1wqWQLGI35smz4f48k0wa4C4h9kUYv"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="2670240956-3D795oeGR2BFIbKqVmn1Fdy2mjINAbnBI1Ks4XU"
access_token_secret="WNcDtRDkI6JPv2QsXq5jJ10AwiiawfQNcJrvhXyNqmWye"

oauth = OAuth(access_token, access_token_secret, consumer_key, consumer_secret)

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
iterator = twitter_stream.statuses.filter(track="Cricket", language="en")


# Print each tweet in the stream to the screen 
# Here we set it to stop after getting limited tweets. 
# You don't have to set it to stop, but can continue running 
# the Twitter API to collect data for days or even longer. 
tweet_count = 5
for tweet1 in iterator:
    tweet_count -= 1
    
    json_str = json.dumps(tweet1)
    data = json.loads(json_str)
   
    tweet = TextBlob(data["text"])
    # output sentiment polarity
    print(tweet.sentiment.polarity)
        
        # determine if sentiment is positive,negative, or neutral
    if tweet.sentiment.polarity < 0:
        sentiment = "negative"
            
    elif tweet.sentiment.polarity == 0:
        sentiment = "neutral"
           
    else:
        sentiment = "positive"
        #sentimentAnalysis(sentiment)
    output = open('sentiments.csv','a')
    output.write(sentiment)
    output.write("\n")
    output.close()
    
    
    # The command below will do pretty printing for JSON data, try it out
    # print json.dumps(tweet, indent=4)
       
    if tweet_count <= 0:
        break 

tweets_data_path = 'sentiments.csv'

tweets_data = []
tweets_file = open(tweets_data_path, "r")

for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

positive_count = "positive"
cnt = Counter()
negative_count = "negative"
cnt1 = Counter()
neutral_count = "neutral"
cnt2 = Counter()
words = re.findall(r"\w+", open('sentiments.csv').read().lower())
for word in words:
    if word in positive_count:
        cnt[word] += 1
    elif word in negative_count:
        cnt1[word] += 1
    else:
        cnt2[word] += 1
print(cnt)
print(cnt1)
print(cnt2)

explode = (0, 0.1, 0) 
labels = 'Positive', 'Negative', 'Neutral'
sizes = [cnt["positive"], cnt1["negative"], cnt2["neutral"]]
colors = ['gold', 'yellowgreen', 'lightcoral']


plt.pie(sizes, explode=explode, colors=colors,
        autopct='%1.1f%%', startangle=120)
plt.legend(labels, loc=(-0.05, 0.05), shadow=True)
plt.axis('equal')
plt.show()

