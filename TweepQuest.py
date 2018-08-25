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

battling = 0 

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
        turns =+ 1
        moved = 0
        command = status.text
        print("Recived:\n" + command + "\n")
        #Naming the hero
        if Player.name == "Player":
            Player.name = command[12:]
            if len(Player.name) > 20:
                Player.name =  Player.name[:20]
            #, in_reply_to_status_id = status.id?
            Display("The hero's name shall be " + Player.name + "!" + goal_announce)

        #Command outside battle
        elif Player.name != "Blank" and battling == 0:
            splitcommand = command.split(" ")

            if "improve" in command:
                amount = 0
                if splitcommand[4] in splitcommand:
                    amount = splitcommand[4]
        #        else:
        #            amount = Points
        #        if "Vitality" in command: Vitality += amount, Display(Player.name + " allocated " + str(amount) + " Points into Vitality.")
        #        if "Spirit" in command: Spirit += amount, Display(Player.name + " allocated " + str(amount) + " Points into Spirit.")
        #        Points -= amount

            elif splitcommand[2] in splitcommand and type(int(splitcommand[2])) == type(1):
                steps = int(splitcommand[2])
                if steps <= Player.speed:
                    if "right" in splitcommand[1]: Player.x += steps
                    elif "left" in splitcommand[1]: Player.x -= steps
                    elif "up" in splitcommand[1]: Player.y += steps
                    elif "down" in splitcommand[1]: Player.y -= steps
                    Display(Player.name + " moved right " + str(steps) + " steps.\nCurrent position: (" + str(Player.x) + "," + str(Player.y) + ")")
                    moved = 1
                else:
                    Display("Not enough Movement for that distance!")
                    moved = 0
            else:
                Display("Invalid syntax. Please")
                moved = 0

            sleep(5)

            #Encountering enemies
            battlechance = 1 #randint(1, 3)
            if battlechance == 1 and moved == 1:
                self.fight(Vitality, Spirit, Strength, Guard, Agility, Movement, Intellect, Wisdom, Skill, Luck, Moves, Items, Points, status)

            if Player.x == goalX and Player.y == goalY:
                Display(Player.name + " reached the objective. Congratulations, you won!\nTurns: " + str(turns))
                sys.exit()

        elif Player.name != "Blank" and battling == 1:
            if "attack" in command: playerchoice = 1
            if "special" in command: playerchoice = 2
            if "item" in command: playerchoice = 3


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
myStream.filter(track=["#TweepQuest"], newasync=True)