import tweepy
import Quandl
from textblob import TextBlob
import numpy as np
import matplotlib.pyplot as plt
from Bandit import EpsilonGreedy

##keywords = ['oil','OPEC','Russia']

def FindCorr(keywords):
##    keywords = ['OPEC','gas','oil']
    input_com = 'oil'
    nplays = 50
    user = ['ReutersCommods']
    commodity=np.array(['oil'])
    icom = np.where(commodity==input_com)[0]
    commodities = ['OFDP/FUTURE_CL1']

    access_token = '1148875658-sOvCIg1rn389WlD21j5H05b6nX6QWwZT8SmKN4V'
    access_token_secret = 'btWyBBuNNYURADF85kQVaTopwMZZEWE68z8T9QRAFsRYw'
    consumer_key = 'EyqBLT3fXrvHLeQTg3fnjj3Rg'
    consumer_secret = 'Xiou4tnc3XfATrS9jM6WsoTLkckMqKtjLY3EvltkRVZ9B4n09M'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    #generate data first
    text =[]
    date =[]


    for status in tweepy.Cursor(api.user_timeline,id=user[0]).items(2000):
        tweet = status.text
        text.append(tweet)
        date.append(str(status.created_at.year)+'-'+str(status.created_at.month)+'-'+str(status.created_at.day))
    qdata = Quandl.get(commodities[icom], trim_start=date[-1:][0], trim_end=date[0])
    unq_dates = np.unique(date)
    date_table = np.zeros(len(unq_dates))

    senti =[]
    for itxt, txt in enumerate(text):
        for keyword in keywords:
           if txt.find(keyword)!= -1:
                date_table[np.where(unq_dates==date[itxt])] += 1
                senti.append(TextBlob(txt).polarity)
                break

    qdatanp = np.array(qdata.Open)
    qfluc = qdatanp.astype('float')/max(qdatanp)
    qfluc = qfluc-qfluc[0]

    arms = range(1,20)
    bandit = EpsilonGreedy(len(arms))

    for i in range(nplays):
        arm = bandit.choose_arm() 
        mdays = arms[arm]
        rwd = abs(np.corrcoef(qfluc[mdays:len(qfluc)],date_table[0:len(qfluc)-mdays])[1,0])
        bandit.update(arm,rwd)
    return qfluc[mdays:len(qfluc)], date_table[0:len(qfluc)-mdays], np.argmax(bandit.values)
