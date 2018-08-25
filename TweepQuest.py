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

class Player():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.name = "Player"
        self.health = 100
        self.attack = 10
        self.defense = 10
        self.speed = 10

class Enemy():
    def __init__(self):
        self.health = 100
        self.attack = 10
        self.defense = 10
        self.speed = 10

goalX = randint(-100,100)
goalY = randint(-100,100)

goal_announce = ("\nGoal:" + "(" + str(goalX) + "," + str(goalY) + ")")

Display("[Tweep Quest is currently under development.]\n New adventure starting! What should the player's name be?\n(Input comes after #TweepQuest.)")


class MyStreamListener(tweepy.StreamListener):
    #Class Values here
    def on_status(self, status):
        command = status.body
        print("Tweet received: " + command)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
myStream.filter(track=["#TweepQuest"], newasync=True)