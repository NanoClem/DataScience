# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the tweepy library
import tweepy
from StreamListener import StreamListener


# Variables that contains the user credentials to access Twitter API
ACCESS_TOKEN = '1092779846172901376-rzTjfUFlaZPuOI5tgXIrTf9wnJl2Tp'
ACCESS_SECRET = 'wwyt5wgx8jkigFLKsGe3lLvjgUwvCy61Z5WkTws4Curho'
CONSUMER_KEY = 'v0PxxRjrbplzz2wLZxoHLnkQn'
CONSUMER_SECRET = 'faP12Gjc2X83rSHMbWmK2tGor0H235TVH24wovj2Sbq1zqCYOb'

# Setup tweepy to authenticate with Twitter credentials:
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# Create the api to connect to twitter with your creadentials
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
#---------------------------------------------------------------------------------------------------------------------
# wait_on_rate_limit= True;  will make the api to automatically wait for rate limits to replenish
# wait_on_rate_limit_notify= Ture;  will make the api  to print a notification when Tweepyis waiting for rate limits to replenish
#---------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------
# The following loop will print most recent statuses, including retweets, posted by the authenticating user and that user’s friends.
# This is the equivalent of /timeline/home on the Web.
#---------------------------------------------------------------------------------------------------------------------

for status in tweepy.Cursor(api.home_timeline).items(200):
    print(status._json)

#---------------------------------------------------------------------------------------------------------------------
# Twitter API development use pagination for Iterating through timelines, user lists, direct messages, etc.
# To help make pagination easier and Tweepy has the Cursor object.
#---------------------------------------------------------------------------------------------------------------------

#PREPARATION DE L'ECOUTE DU STREAM
# streamListener = StreamListener()
# tweetStream    = tweepy.Stream(auth=api.auth, listener=streamListener)
# tweetStream.filter(track=["google"], languages=["en"])
