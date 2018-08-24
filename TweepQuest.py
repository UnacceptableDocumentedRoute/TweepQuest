import tweepy
import sys
from random import randint
from random import choice
from time import sleep
import math

fp = open("TweepQuestKeys", "r")
consumer_key = fp.readline(1)
consumer_secret = fp.readline(2)
access_token = fp.readline(3)
access_token_secret = fp.readline(4)
fp.close()
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth.secure = True
api = tweepy.API(auth)

duplicateprevention = "\n(DP:" + str(randint(1, 10000)) + ")"
def DuplicatePrevention():
        duplicateprevention = "\n(DP:" + str(randint(1, 10000)) + ")"
        return duplicateprevention

def Display(tweetandprint):
    status = api.update_status(status=str(tweetandprint + DuplicatePrevention()))
    print(str(tweetandprint + DuplicatePrevention()))

class MyStreamListener(tweepy.StreamListener):
    #Class Values here
    def on_status(self, status):
        command = status.body
        print("Tweet received: " + command)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
myStream.filter(track=["#TweepQuest"], newasync=True)