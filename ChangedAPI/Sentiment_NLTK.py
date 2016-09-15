# @BEGIN Sentiment_TextBLOB @desc Exercise YW for Analysing Tweets with NLTK
# @IN tweet.csv @AS TweetsinCSV @URI file:tweet.csv
# @OUT matplotlib.pyplot @desc Pie chart with Sentiment Scores Displayed

import json
import simplejson as json
from textblob import TextBlob
from collections import Counter
import re
import matplotlib.pyplot as plt
import requests

# @BEGIN AccessTweets @desc To read the tweets from tweet.csv file
# @IN tweet.csv @AS TweetsinCSV @URI file:tweet.csv
# @OUT tweets_file @AS TweetRead
tweets_data_path = 'tweet.csv'
tweets_data = []
tweets_file = open(tweets_data_path, "r")
# @END AccessTweets

negative = 0
neutral = 0
positive = 0

# @BEGIN CountSentiments @desc Calculate sentiments with NLTK
# @IN tweets_file @AS TweetRead
# @OUT positive @AS PositiveCount
# @OUT negative @AS NegativeCount
# @OUT neutral @AS NeutralCount
for line in tweets_file:

    r = requests.post("http://text-processing.com/api/sentiment/",data={'text':line})
    jsn_dict = r.json()
    sentiment = jsn_dict["label"]

    if sentiment == 'neg':
        negative = negative+1

    elif sentiment == 'neutral':
        neutral = neutral+1
   
    else:
        positive = positive+1
# @END CountSentiments
   
# @BEGIN Measures  @desc SetPieChartMeasures
# @IN positive @AS PositiveCount
# @IN negative @AS NegativeCount
# @IN neutral @AS NeutralCount
# @OUT explode @AS Explode
# @OUT labels @AS Labels
# @OUT sizes @AS Sizes
# @OUT colors @AS Colors
explode = (0, 0.1, 0) 
labels = 'Positive', 'Negative', 'Neutral'
sizes = [positive, negative, neutral]
colors = ['gold', 'yellowgreen', 'lightcoral']
# @END SetPieChartMeasures

# @BEGIN DrawPieChart @desc Pie chart saved in Scores_NLTK.jpeg
# @IN explode @AS Explode
# @IN labels @AS Labels
# @IN sizes @AS Sizes
# @IN colors @AS Colors
# @OUT matplotlib.pyplot @as plt
plt.pie(sizes, explode=explode, colors=colors,
        autopct='%1.1f%%', startangle=120)
plt.legend(labels, loc=(-0.05, 0.05), shadow=True)
plt.axis('equal')
plt.savefig('D:\Case Studies - Reproducibility\YesWorkflow\Scores_NLTK.jpg')
# @END DrawPieChart

# @END Sentiment_NLTK
