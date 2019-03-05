# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 13:50:00 2019

@author: dupouyj
"""

import json

import tweepy #pip install tweepy


#user credentials to access Twitter API
access_token = "2228677797-iebszQqsQUyoM6QwtiQyIhlKpin7E7wdwz0wRDk"
access_secret = "mqy4mAgPN6UPiKZczXQfSfKVJlV7BmAfqnYW0QOBBipHT"
consumer_key = "aqiqQUMbJrpFEesvVGWzyNevY"
consumer_secret = "0uvB4JXW6WVtkeHE9gxaXZkiIbHG4AkMoHbbGtcqvJwpxheAWj"



# Setup tweepy to authenticate with Twitter credentials:
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

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

#file = open("tweets.txt",'w')

for status in tweepy.Cursor(api.home_timeline).items(200):
#    json.dump(status._json,file)  #ecrire le tweet dans le fichier
#    file.write("\n\n")
    print("Tweet :\n", status._json.get("text"),"\n\n")
    print("Details du tweet :\n",status._json,"\n\n")
    print("Infos de l'utilisateur :\n",status._json.get("user"))
    print("\n\nNom de l'utilisateur :\n",status._json.get("user").get("name"),",  ", status._json.get("user").get("screen_name"),"\n\n\n")

#file.close()


class StreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

        
    def on_error(self, status_code):
        if status_code == 420:
            return False

stream_listener = StreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
#search tweet that contain a track in a language
#stream.filter(track=["cyberespace"],languages=["fr"])
#get tweets by a specific user
#stream.filter(follow=["612655414"])