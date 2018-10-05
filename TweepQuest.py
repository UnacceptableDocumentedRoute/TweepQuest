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
    def __init__(self, name="Player", x=0, y=0, health=100, attack=10, defense=10, speed=10):
        self.x = x
        self.y = y
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed

class Enemy():
    def __init__(self, currentenemy=None):
        if currentenemy ==None:
            self.health = 100
            self.attack = 10
            self.defense = 10
            self.speed = 10

        else:
            self.health = currentenemy['health']
            self.attack = currentenemy['attack']
            self.defense = currentenemy['defense']
            self.speed = currentenemy['speed']

goalX = randint(-100,100)
goalY = randint(-100,100)

goal_announce = ("\nGoal:" + "(" + str(goalX) + "," + str(goalY) + ")")

Display("[Tweep Quest is currently under development.]\n New adventure starting! What should the player's name be?\n(Input comes after #TweepQuest.)")


class MyStreamListener(tweepy.StreamListener):
    #Class Values here
    myPlayer = Player()
    playerbase = Player()
    playerstate = copy.copy(playerbase)

    myEnemy = None
    enemystate = None
    enemylist = [{'name': "Enemy1", 'health':150, 'attack': 20, 'defense': 10, 'speed': 5},
                 {'name': "Enemy2", 'health':100, 'attack': 10, 'defense': 15, 'speed': 15}]

    battling = False

    def fightnotify(self):
        Display(self.myPlayer.name + " has encountered an enemy!")

    def on_status(self, status):
        command = status.text
        moved = 0
        print("Recived:\n" + command + "\n")

        #Intialize Battling
        if self.myEnemy != None and self.battling == False:
            self.battling = True

            self.playerstate.health = self.playerbase.health
            self.playerstate.attack = self.playerbase.attack
            self.playerstate.defense = self.playerbase.defense
            self.playerstate.speed = self.playerbase.speed

            self.enemystate.health = self.myEnemy.health
            self.enemystate.attack = self.myEnemy.attack
            self.enemystate.defense = self.myEnemy.defense
            self.enemystate.speed = self.myEnemy.speed

        if self.battling == True:
            if self.playerstate.speed == self.enemystate.speed:
                battleturn = randint(1, 2)
                if battleturn == 1:
                    self.playerTurn(command, self.enemystate)
                    self.enemyTurn(command, self.enemystate)
                elif battleturn == 2:
                    self.enemyTurn(command, self.enemystate)
                    self.playerTurn(command, self.enemystate)

            elif self.playerstate.speed > self.enemystate.speed:
                self.playerTurn(command, self.enemystate)
                self.enemyTurn(command, self.enemystate)

            elif self.playerstate.speed < self.enemystate.speed:
                self.enemyTurn(command, self.enemystate)
                self.playerTurn(command, self.enemystate)
                #Battling end

        # Naming the hero
        if self.myPlayer.name == "Player":
            self.myPlayer.name = command[12:]
            if len(self.myPlayer.name) > 20:
                self.myPlayer.name = self.myPlayer.name[:20]
            # , in_reply_to_status_id = status.id?
            Display("The hero's name shall be " + self.myPlayer.name + "!" + goal_announce)

        # Command outside battle
        elif self.myPlayer.name != "Blank" and self.battling == 0:
            splitcommand = command.split(" ")
            if "improve" in command:
                amount = 0
                if splitcommand[4] in splitcommand:
                    amount = splitcommand[4]
            #        else:
            #            amount = Points
            #        if "Vitality" in command: Vitality += amount, Display(self.myPlayer.name + " allocated " + str(amount) + " Points into Vitality.")
            #        if "Spirit" in command: Spirit += amount, Display(self.myPlayer.name + " allocated " + str(amount) + " Points into Spirit.")
            #        Points -= amount

            elif splitcommand[2] in splitcommand and type(int(splitcommand[2])) == type(1):
                steps = int(splitcommand[2])
                if steps <= self.myPlayer.speed:
                    if "right" in splitcommand[1]:
                        self.myPlayer.x += steps
                    elif "left" in splitcommand[1]:
                        self.myPlayer.x -= steps
                    elif "up" in splitcommand[1]:
                        self.myPlayer.y += steps
                    elif "down" in splitcommand[1]:
                        self.myPlayer.y -= steps
                    Display(self.myPlayer.name + " moved right " + str(
                        steps) + " steps.\nCurrent position: (" + str(self.myPlayer.x) + "," + str(
                        self.myPlayer.y) + ")")
                    moved = 1
                else:
                    Display("Not enough Movement for that distance!")
                    moved = 0
            else:
                Display("Invalid syntax. Please")
                moved = 0

            sleep(1)

            # Encountering enemies
            battlechance = 1  # randint(1, 3)
            if battlechance == 1 and moved == 1:
                currentenemy = choice(self.enemylist)
                self.myEnemy = Enemy(currentenemy)
                self.enemystate = copy.copy(self.myEnemy)
                self.fightnotify()

            if self.myPlayer.x == goalX and self.myPlayer.y == goalY:
                Display(self.myPlayer.name + " reached the objective. Congratulations, you won!")
                sys.exit()


        #Battling
    def playerTurn(self, command, enemystate):
        if "special" in command: playerchoice = 2
        if "item" in command: playerchoice = 3
        if "attack" in command:
            damage = ceil(self.playerstate.attack - ((enemystate.defense/100) * self.playerstate.attack))
            enemystate.health -= damage
            Display(self.myPlayer.name + " attacks! " + str(damage) + " damage to the enemy! Enemy Health: %s / %s"%(self.enemystate.health, self.myEnemy.health))
        #keep deathCheck() at the end
        self.deathCheck(enemystate)

    def enemyTurn(self, command, enemystate):
        enemymove = 1
        if enemymove == 1:
            damage = ceil(enemystate.attack - (self.playerstate.defense/2))
            self.playerstate.health -= damage
            Display("Enemy attacks! " + str(damage) + " damage to " + self.myPlayer.name + "!\nCurrent health: " + str(self.playerstate.health) + "/" + str(self.playerbase.health))
        #keep deathCheck() at the end
        self.deathCheck(enemystate)

    def battleLose(self):
        Display(self.myPlayer.name + " lost...")

    def battleWin(self):
        Display(self.myPlayer.name + " won the battle!")

    def deathCheck(self, enemystate):
        if enemystate.health <= 0:
            self.battleWin()

        if self.playerstate.health <= 0:
            self.battleLose()

    def descriptionUpdate(self):
        print("filler")
        #get description from account
        #put string into variable
        #modify description variable with regular expression
        #send new string back to Twitter

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
myStream.filter(track=["#TweepQuest"], newasync=True)
