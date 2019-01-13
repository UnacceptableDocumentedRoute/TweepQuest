import tweepy
import sys
import copy
from math import ceil
from random import randint
from random import choice
from time import sleep

fp = open("TweepQuestKeys", "r")
consumer_key = fp.readline().strip("\n")
consumer_secret = fp.readline().strip("\n")
access_token = fp.readline().strip("\n")
access_token_secret = fp.readline().strip("\n")
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

class Player():
    def __init__(self, name="Player", x=0, y=0):
        self.x = x
        self.y = y
        self.name = name
        tiles_explored = []