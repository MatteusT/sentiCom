import json
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
import Quandl
from textblob import TextBlob
import numpy as np


def conv_tweet_date(tweet_date):
    split_tweet = tweet_date.split(' ')
    months = np.array(['','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
    mon = np.where(months==split_tweet[1])[0][0]
    date = int(split_tweet[2])
    time = split_tweet[3]
    year = int(split_tweet[5]) 
    return time, date, mon, year
    
ACCESS_TOKEN = '1148875658-sOvCIg1rn389WlD21j5H05b6nX6QWwZT8SmKN4V'
ACCESS_SECRET = 'btWyBBuNNYURADF85kQVaTopwMZZEWE68z8T9QRAFsRYw'
CONSUMER_KEY = 'EyqBLT3fXrvHLeQTg3fnjj3Rg'
CONSUMER_SECRET = 'Xiou4tnc3XfATrS9jM6WsoTLkckMqKtjLY3EvltkRVZ9B4n09M'

##quandl_token = 'Qk9s2moCegjZuEpAqs7Y'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
iterator = twitter_stream.statuses.filter(track="ruthenium")



date = []
time = []
mon =[]
year= []
sentiment = []
tweet_count = 2
for tweet in iterator:
    tweet_count -= 1
#    jtweet =  json.dumps(tweet)
##    t_time, t_date , t_mon, t_year = conv_tweet_date(tweet['created_at'])
##    mon.append(t_mon)
##    date.append(t_date)
##    time.append(t_time)
##    year.append(t_year)
    print tweet['text']
    print tweet['created_at']
    blob = TextBlob(tweet['text'])
    sentiment.append(blob.polarity)
    if tweet_count <= 0:
        break

##qdata = Quandl.get('WGC/GOLD_DAILY_USD', trim_start="2016-01-01", trim_end="2016-02-05")
