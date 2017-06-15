import tweepy
import urllib.request
from bs4 import BeautifulSoup
import tweepy
import matplotlib.pyplot as plt
from textblob import TextBlob

googleTrends=[]
#create a list of google trending search items
trendHtml=urllib.request.urlopen("https://trends.google.com/trends/hottrends/atom/feed").read()
soup = BeautifulSoup(trendHtml, "lxml")
for title in soup.find_all('title'):
    if (title.string!="Hot Trends"):
        googleTrends.append(title.string)
#connect to twitter
consumer_key="###"
consumer_key_secret="###"

access_token="###"
access_token_secret="###"
auth = tweepy.OAuthHandler(consumer_key,consumer_key_secret)
auth.set_access_token(access_token,access_token_secret)

tweet_api=tweepy.API(auth)

#get tweeter sentiment analysis for each trending topics and plot the graph
for topic in googleTrends:
        tweet_polarity= []
        public_tweets= tweet_api.search(q=topic,rpp=100)
        for tweets in public_tweets:
                analysis=TextBlob(str(tweets.text))
                tweet_polarity.append(analysis.sentiment.polarity)
        positive_cnt=0
        negative_cnt=0
        neutral_cnt=0
        for i in tweet_polarity:
            if (i>0):
                positive_cnt = positive_cnt + 1
            elif (i<0):
                negative_cnt = negative_cnt + 1
            else:
                neutral_cnt = neutral_cnt + 1
        labels = 'Positive', 'Negative', 'Neutral'
        size = [positive_cnt, negative_cnt, neutral_cnt]
        explode = (0, 0.1, 0)
        plt.pie(size, explode=explode, labels=labels, shadow=True, startangle=90)
        plt.title(topic)
        plt.show()
        plt.clf()

