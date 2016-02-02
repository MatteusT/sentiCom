import json
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
import Quandl
#from textblob import TextBlob

ACCESS_TOKEN = '1148875658-sOvCIg1rn389WlD21j5H05b6nX6QWwZT8SmKN4V'
ACCESS_SECRET = 'btWyBBuNNYURADF85kQVaTopwMZZEWE68z8T9QRAFsRYw'
CONSUMER_KEY = 'EyqBLT3fXrvHLeQTg3fnjj3Rg'
CONSUMER_SECRET = 'Xiou4tnc3XfATrS9jM6WsoTLkckMqKtjLY3EvltkRVZ9B4n09M'

quandl_token = 'Qk9s2moCegjZuEpAqs7Y'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
iterator = twitter_stream.statuses.filter(track="Gold", language="en")

# Print each tweet in the stream to the screen
# Here we set it to stop after getting 1000 tweets.
# You don't have to set it to stop, but can continue running
# the Twitter API to collect data for days or even longer.
date = []
sentiment = []
tweet_count = 10000
for tweet in iterator:
    tweet_count -= 1
            # Twitter Python Tool wraps the data returned by Twitter
                # as a TwitterDictResponse object.
                    # We convert it back to the JSON format to print/score
    jtweet =  json.dumps(tweet)
    print jtweet
   # date.append(jtweet['created_at'])
   # blob = TextBlob(jtweet['text'])
    #tsent = []
    #for sentence in blob.sentences:
     #   tsent.append(sentences.sentiment.polarity)
    #sentiment.append(tsent)
 #The command below will do pretty printing fo
                # JSON data, try it out
                 # print json.dumps(tweet, indent=4)
    if tweet_count <= 0:
        break

