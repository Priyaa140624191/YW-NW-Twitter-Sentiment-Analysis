# @BEGIN Sentiment_TextBLOB @desc Exercise YW for Analysing Tweets with TextBLOB
# @IN tweet.csv @AS TweetsinCSV @URI file:tweet.csv
# @out  matplotlib.pyplot @as plt  @URI file:Scores_TextBLOB.jpg

import json
import simplejson as json
from textblob import TextBlob
from collections import Counter
import re
import matplotlib.pyplot as plt

# @BEGIN AccessTweets @desc To read the tweets from tweet.csv file
# @IN tweet.csv @AS TweetsinCSV @URI file:tweet.csv
# @OUT tweets_file @AS TweetRead
tweets_data = []
tweets_file = open(tweets_data_path, 'r')
# @END AccessTweets

negative = 0
neutral = 0
positive = 0

# @BEGIN CountSentiments @desc Calculate sentiments with TextBLOB
# @IN tweets_file @AS TweetRead
# @OUT positive @AS PositiveCount
# @OUT negative @AS NegativeCount
# @OUT neutral @AS NeutralCount
for line in tweets_file:
    tweet = TextBlob(line)
    print(tweet.sentiment.polarity)
    
    if tweet.sentiment.polarity < 0:
        sentiment = "negative"
        negative = negative+1
        
    elif tweet.sentiment.polarity == 0:
        sentiment = "neutral"
        neutral = neutral+1
           
    else:
        sentiment = "positive"
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

# @BEGIN DrawPieChart @desc Pie chart saved in Scores_TextBLOB.jpeg
# @IN explode @AS Explode
# @IN labels @AS Labels
# @IN sizes @AS Sizes
# @IN colors @AS Colors
# @out  matplotlib.pyplot @as plt  @URI file:Scores_TextBLOB.jpg
plt.pie(sizes, explode=explode, colors=colors,
        autopct='%1.1f%%', startangle=120)
plt.legend(labels, loc=(-0.05, 0.05), shadow=True)
plt.axis('equal')
plt.savefig('D:\Case Studies - Reproducibility\YesWorkflow\Scores_TextBLOB.jpg')
# @END DrawPieChart

# @END Sentiment_TextBLOB