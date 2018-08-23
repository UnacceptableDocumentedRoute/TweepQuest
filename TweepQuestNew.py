import tweepy
import sys
from random import randint
from random import choice
from time import sleep
import math

fp = open("TweepQuestKeys", "r")
consumer_key = fp.readline()
consumer_secret = fp.readline()
access_token = fp.readline()
access_token_secret = fp.readline()
fp.close()
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth.secure = True
api = tweepy.API(auth)

duplicateprevention = " (DP:" + str(randint(1, 10000)) + ")"


def DuplicatePrevention():
    duplicateprevention = " (DP:" + str(randint(1, 10000)) + ")"
    return duplicateprevention


def Display(tweetandprint):
    status = api.update_status(status=str(tweetandprint + DuplicatePrevention()))
    print(str(tweetandprint + DuplicatePrevention()))


heroX = 0
heroY = 0
heroname = "Blank"
battling = 0
goalX = randint(-100, 100)
goalY = randint(-100, 100)

goal_announce = (" Goal:" + "(" + str(goalX) + "," + str(goalY) + ")")

Display(
    "[Tweep Quest is currently under development.]\n New adventure starting! What should the hero's name be?\n(Input comes after #TweepQuest.)")

# Out of Battle Stats
Vitality = 10
Spirit = 10
Strength = 10
Guard = 10
Agility = 10
Movement = 10
Intellect = 10
Wisdom = 10
Skill = 1
Luck = 1
Moves = ["Identify"]
Items = {"Apples": 1, "Ice Pack": 0}
Points = 0
# Out of Battle Stats
playerchoice = 100


class MyStreamListener(tweepy.StreamListener):
    CurrentHP = Vitality
    worldmap = 100 * [100 * [True]]
    heroname = "Blank"
    heroX = 0
    heroY = 0
    battling = 0
    enemylist = [["TEST_1", 10, 10, 10, 10, 10, 10, 10, 10, 1, 1, ["???"], 5],
                 ["TEST_2", 8, 20, 5, 5, 10, 10, 15, 20, 1, 0, ["Teleport", "Impair"], 8]
                 ]
    bosslist = [
        ["TEST_A", 50, 50, 50, 50, 50, 50, 50, 50, 5, 5, ["!!!"], 100]
    ]
    enemy = []

    # Player Stat Initialization
    health = Vitality * 10
    magic = Spirit * 10
    physicalattack = Strength
    physicaldefense = Guard / 2
    speed = Agility
    evasion = Movement
    magicattack = Intellect
    magicdefense = Wisdom / 2
    physicalsecurity = Skill
    magicalsecurity = Luck
    playermoveset = Moves
    fire_weakness = 1
    earth_weakness = 1
    electric_weakness = 1
    grass_weakness = 1
    wind_weakness = 1
    water_weakness = 1
    dark_weakness = 1
    light_weakness = 1
    stance = 0
    burn = 0
    confusion = 0
    paralysis = 0
    poison = 0
    rage = 0
    boint = 0

    def define_fight(self):
        self.battling = 1
        playerchoice = 100
        if self.heroX == goalX and self.heroY == goalY:
            enemy = choice(self.bosslist)
            Display(self.heroname + " challenged the final boss: " + self.enemyname + "!")
        else:
            enemy = choice(self.enemylist)
            Display(self.heroname + " encountered an enemy: " + self.enemyname + "!!")

        # Enemy Stat Initialization
        enemyname = self.enemy[0]
        enemyhealth = self.enemy[1] * 10
        enemymagic = self.enemy[2] * 10
        enemyphysicalattack = self.enemy[3]
        enemyphysicaldefense = self.enemy[4] / 2
        enemyspeed = self.enemy[5]
        enemyevasion = self.enemy[6]
        enemymagicattack = self.enemy[7]
        enemymagicdefense = self.enemy[8] / 2
        enemyphysicalsecurity = self.enemy[9]
        enemymagicalsecurity = self.enemy[10]
        enemymoveset = self.enemy[11]
        enemyexperience = self.enemy[12]
        enemyfire_weakness = 1
        enemyearth_weakness = 1
        enemyelectric_weakness = 1
        enemygrass_weakness = 1
        enemywind_weakness = 1
        enemywater_weakness = 1
        enemydark_weakness = 1
        enemylight_weakness = 1
        enemystance = "Default"
        enemyburn = 0
        enemyconfusion = 0
        enemyparalysis = 0
        enemypoison = 0
        enemyrage = 0
        enemyboint = 0

        sleep(5)

    def fight(self, Vitality, Spirit, Strength, Guard, Agility, Movement, Intellect, Wisdom, Skill, Luck, Moves, Items,
              Points, status):

        while health > 0 and enemyhealth > 0 and enemystance != "Fled":
            magic += Spirit
            enemymagic += self.enemy[2]

            if health > Vitality * 10: health = Vitality * 10
            if magic > Spirit * 10: magic = Spirit * 10
            if enemyhealth > self.enemy[1] * 10: enemyhealth = self.enemy[1] * 10
            if enemymagic > self.enemy[2] * 10: enemymagic = self.enemy[2] * 10

            # Player Condition Effects
            if self.burn > 0:
                damage = Vitality * 0.05 * self.fire_weakness
                damage = math.ceil(damage)
                health -= damage
                self.burn -= 1
                Display(self.heroname + " was hurt by the burn! It did " + str(damage) + " damage.")

            if self.confusion > 0:
                self.confusion -= 1
                Display(self.heroname + " is confused!")

            if self.paralysis > 0:
                self.paralysis -= 1
                Display(self.heroname + " is paralyzed!")

            if self.poison > 0:
                damage = Vitality * 0.1
                damage = math.ceil(damage)
                health -= damage
                self.poison -= 1
                Display(self.heroname + " was hurt by the poison! It did " + str(damage) + " damage.")

            if self.rage > 0:
                self.rage -= 1
                Display(self.heroname + " is enraged!")

            if self.boint > 0:
                Display(self.heroname + " is boint!")
                self.physicalattack = randint(1, 100)
                self.physicaldefense = randint(1, 50)
                self.speed = randint(1, 100)
                self.evasion = randint(1, 100)
                self.magicattack = randint(1, 100)
                self.magicdefense = randint(1, 50)

            # Enemy Condition Effects
            if self.enemyburn > 0:
                damage = self.enemy[1] * 0.05 * self.enemyfire_weakness
                damage = math.ceil(damage)
                enemyhealth -= damage
                self.burn -= 1
                Display(self.enemyname + " was hurt by the burn! It did " + str(damage) + " damage.")

            if self.enemyconfusion > 0:
                self.enemyconfusion -= 0
                Display(self.enemyname + " is confused!")

            if self.enemyparalysis > 0:
                self.enemyparalysis -= 1
                Display(self.enemyname + " is paralyzed!")

            if self.enemypoison > 0:
                damage = self.enemy[1] * 0.1
                damage = math.ceil(damage)
                enemyhealth -= damage
                self.poison -= 1
                Display(self.enemyname + " was hurt by the poison! It did " + str(damage) + " damage.")

            if self.enemyrage > 0:
                self.enemyrage -= 1
                Display(self.enemyname + " is enraged!")

            if self.enemyboint > 0:
                Display(self.enemyname + " is boint!")
                enemyphysicalattack = randint(1, 100)
                enemyphysicaldefense = randint(1, 50)
                enemyspeed = randint(1, 100)
                enemyevasion = randint(1, 100)
                enemymagicattack = randint(1, 100)
                enemymagicdefense = randint(1, 50)

            nextmove = randint(1, speed + enemyspeed)
            if nextmove > speed:
                enemychoice = randint(1, 2)
                if self.enemyrage > 0: enemychoice = 1
                if self.enemyconfusion > 0: enemychoice = 3.14159265
                if self.enemyparalysis > 0: enemychoice = 0

                if enemychoice == 1:
                    # Enemy Attack
                    damage = (enemyphysicalattack + randint(enemyphysicalsecurity * -1, enemyphysicalsecurity)) - (
                        physicaldefense)
                    damage = math.ceil(damage)
                    dodgechance = randint(1, 125)
                    if dodgechance > evasion and damage > 0:
                        health = health - damage
                        Display(self.enemyname + " attacks! " + str(
                            damage) + " damage to " + self.heroname + ".\nCurrent health: " + str(health))
                    elif dodgechance <= evasion:
                        Display(
                            self.enemyname + " attacks! " + self.heroname + " dodged the attack.\nCurrent health: " + str(
                                health))
                    elif damage <= 0:
                        Display(
                            enemyname + " attacks! " + self.heroname + " blocked the attack.\nCurrent health: " + str(
                                health))

                elif enemychoice == 2:
                    # Enemy Move
                    enemymove = choice(enemymoveset)
                    if enemymove == "???":
                        Display(enemyname + " used ???")
                        print("Filler")
                    elif enemymove == "Identify":
                        Display(enemyname + " examined " + self.heroname + ".\nHealth:" + str(health) + "/" + str(
                            Vitality * 10) + "\nSpirit:" + str(magic) + "/" + str(Spirit * 10) + "\nAttack:" + str(
                            physicalattack) + "\nDefense:" + str(physicaldefense) + "\nSpeed:" + str(
                            speed) + "\nEvasion:" + str(evasion) + "\nMagicAttack:" + str(
                            magicattack) + "\nMagicDefense:" + str(magicdefense))
                        Display(self.heroname + "'s moves:" + str(playermoveset))
                    elif enemymove == "Teleport":
                        if enemymagic >= 100:
                            Display(enemyname + " suddenly disapeared!")
                            enemystance = "Fled"
                        else:
                            Display(enemyname + " tried to teleport, but didn't have enough Magic...")
                    elif enemymove == "Warp":
                        dodgechance = randint(1, 125)
                        if dodgechance > evasion:
                            Display(self.heroname + " was warped away!")
                            self.heroX = randint(-100, 100)
                            self.heroY = randint(-100, 100)
                            Display(self.heroname + " is currently at (" + self.heroX + ", " + self.heroY + ")")
                            enemystance = "Fled"
                    elif enemymove == "Impair":
                        if enemymagic >= 50:
                            Display(enemyname + " impaired " + self.heroname + "; All stats went down by 10%!")
                            physicalattack -= physicalattack * 0.1
                            physicaldefense -= physicaldefense * 0.1
                            speed -= speed * 0.1
                            evasion -= evasion * 0.1
                            magicattack -= magicattack * 0.1
                            magicdefense -= magicdefense * 0.1
                            enemymagic -= 50
                        else:
                            status = api.update_status(
                                status=enemyname + " tried to impair " + self.heroname + ", but didn't have enough Magic...")
                            print(enemyname + " tried to impair " + self.heroname + ", but didn't have enough Magic...")
                    elif enemymove == "Heal":
                        if enemymagic >= 20 and enemyhealth < enemy[1] * 10:
                            healing = enemymagicdefense * 2 + enemymagicattack + randint(enemymagicalsecurity * -2,
                                                                                         enemymagicalsecurity * 2)
                            enemyhealth += healing
                            Display(enemyname + " healed themselves; " + str(healing) + " HP gained!")
                            enemymagic -= 20
                        elif enemymagic < 20:
                            Display(enemyname + " tried to heal themselves, but didn't have enough magic.")
                        elif enemyhealth >= enemy[1] * 10:
                            Display(enemyname + " tried to heal themselves, but already has full health...")
                    elif enemymove == "Hype Up":
                        if enemymagic >= 10:
                            enemyphysicalsecurity += enemyphysicalsecurity * 0.1
                            enemymagicalsecurity += enemymagicalsecurity * 0.1
                            Display(
                                enemyname + " hyped themselves up! Physical and magical stability decreased by 10%!")
                            enemymagic -= 10
                        else:
                            Display(enemyname + " tried to hype themselves up, but didn't have enough Magic...")
                    elif enemymove == "Calm Down":
                        enemyphysicalsecurity = 1
                        enemymagicalsecurity = 1
                        Display(enemyname + " calmed down. Physical and magical stability reverted!")
                    elif enemymove == "Battle Cry":
                        enemyphysicalattack += enemyphysicalattack * 0.1
                        enemyphysicaldefense += enemyphysicaldefense * 0.1
                        enemyspeed += enemyspeed * 0.1
                        Display(
                            enemyname + " let out a tremendous battle cry! Attack, defense, and speed went up by 10%")
                        enemymove.remove("Battle Cry")
                    elif enemymove == "Charge":
                        dodgechance = randint(1, 200)
                        if dodgechance > evasion:
                            damage = (enemyphysicalattack + enemyphysicaldefense + enemyspeed) - physicaldefense
                            damage = math.ceil(damage)
                            if damage < 0: damage = 0
                            health -= damage
                            enemyhealth -= physicaldefense
                            Display(enemyname + " charged forward! Dealt " + str(damage) + " and suffered " + str(
                                physicaldefense) + " recoil damage!\nCurrent health: " + str(health))
                        else:
                            enemyhealth -= (enemyphysicaldefense + enemyspeed) * 0.8
                            Display(enemyname + " charged forward, but missed and fell on their face! Suffered " + str(
                                (enemyphysicaldefense + enemyspeed) * 0.8) + " recoil damage!")
                    elif enemymove == "Offensive Stance":
                        if enemystance != "Offensive":
                            enemyphysicalattack = enemy[3] * 2
                            enemymagicattack = enemy[7] * 2
                            enemyphysicaldefense = enemy[4] / 4
                            enemymagicdefense = enemy[8] / 4
                            enemystance = "Offensive"
                            Display(enemyname + " assumed an offensive stance! Attack double, defense halved.")
                        else:
                            Display(enemyname + " tried to assume an offensive stance, but was already in one...")
                    elif enemymove == "Defensive Stance":
                        if enemystance != "Defensive":
                            enemyphysicaldefense = enemy[4]
                            enemymagicdefense = enemy[8]
                            enemyphysicaldefense = enemy[3] / 2
                            enemymagicattack = enemy[7] / 2
                            Display(enemyname + " assumed a defensive stance! Defense doubled, attack halved.")
                            enemystance = "Defensive"
                        else:
                            Display(enemyname + " tried to assume a defensive stance, but was already in one...")
                    elif enemymove == "Flamethrower":
                        if enemymagic >= 50:
                            dodgechance = randint(1, 131)
                            if dodgechance > evasion and dodgechance % 2 == 0:
                                burn += 5
                                damage = (enemymagicattack * fire_weakness + randint(enemymagicalsecurity * -1,
                                                                                     enemymagicalsecurity)) - (
                                             magicdefense)
                                damage = math.ceil(damage)
                                if damage <= 0: damage = 0
                                health -= damage
                                Display(enemyname + " launched a stream of flames! " + str(
                                    damage) + " damage to " + self.heroname + "! They also caught on fire.\nCurrent health: " + str(
                                    health))
                            elif dodgechance > evasion and dodgechance % 2 == 1:
                                damage = (enemymagicattack * fire_weakness + randint(enemymagicalsecurity * -1,
                                                                                     enemymagicalsecurity)) - (
                                             magicdefense)
                                if damage <= 0:
                                    damage = 1
                                health -= damage
                                Display(enemyname + " launched a stream of flames! " + str(
                                    damage) + " damage to " + self.heroname + "!\nCurrent health: " + str(health))
                            elif dodgechance <= evasion:
                                Display(enemyname + " launched a stream of flames! " + self.heroname + " dodged!")
                            enemymagic -= 40
                        else:
                            Display(enemyname + " tried to launch a stream of flames, but didn't have enough Magic...")
                    elif enemymove == "Rock Throw":
                        dodgechance = randint(1, 80)
                        if dodgechance > evasion:
                            damage = (randint(5, 20) * earth_weakness) - (physicaldefense)
                            damage = math.ceil(damage)
                            if damage < 0: damage = 0
                            health -= damage
                            Display(enemyname + " threw a rock at " + self.heroname + ". It caused " + str(
                                damage) + " damage. How rude!\nCurrent health: " + str(health))
                        else:
                            status = api.update_status(
                                status=enemyname + " threw a rock at " + self.heroname + ", but it missed...")
                            print(enemyname + " threw a rock at " + self.heroname + ", but it missed...")
                    elif enemymove == "Lightning":
                        if enemymagic >= 25:
                            dodgechance = randint(1, 100)
                            if dodgechance > evasion and dodgechance % 5 == 0:
                                damage = (enemymagicattack * electric_weakness + randint(enemymagicalsecurity * -1,
                                                                                         enemymagicalsecurity)) - (
                                             magicdefense)
                                damage = math.ceil(damage)
                                if damage < 0: damage = 0
                                health -= damage
                                paralysis += 5
                                Display(enemyname + " struck " + self.heroname + " with a bolt of lightning!" + str(
                                    damage) + " damage to " + self.heroname + "! They also became paralyzed.")
                            elif dodgechance > evasion and dodgechance % 2 == 1:
                                damage = (enemymagicattack * electric_weakness + randint(enemymagicalsecurity * -1,
                                                                                         enemymagicalsecurity)) - (
                                             magicdefense)
                                if damage < 0: damage = 1
                                health -= damage
                                Display(enemyname + " struck " + self.heroname + " with a bolt of lightning!" + str(
                                    damage) + " damage to " + self.heroname + "!")
                            else:
                                Display(
                                    enemyname + " tried to strike " + self.heroname + " with a bolt of lightning, but missed...")
                            enemymagic -= 25
                        else:
                            status = api.update_status(
                                status=enemyname + " tried to strike " + self.heroname + " with a bolt of lightning, but didn't have enough Magic...")
                            print(
                                enemyname + " tried to strike " + self.heroname + " with a bolt of lightning, but missed...")
                    elif enemymove == "Leaf Barrage":
                        if enemymagic > 25:
                            dodgechance = randint(1, 200)
                            if dodgechance > evasion:
                                damage = (enemymagicattack * grass_weakness + randint(enemymagicalsecurity * -1,
                                                                                      enemymagicalsecurity) - physicaldefense)
                                damage = math.ceil(damage)
                                if damage < 0: damage = 0
                                Display(enemyname + " shot sharp leaves at incredible speed! " + str(
                                    damage) + " damage to " + self.heroname + ".")
                            else:
                                Display(enemyname + " shot sharp leaves at incredible speed! They all missed...")
                            enemymagic -= 25
                        else:
                            status = api.update_status(
                                status=enemyname + " wanted to shoot sharp leaves at incredible speed, but didn't have enough Magic... ")
                            print(
                                enemyname + " wanted to shoot sharp leaves at incredible speed, but didn't have enough Magic... ")
                    elif enemymove == "Gust":
                        if enemymagic >= 20:
                            dodgechance = randint(1, 135)
                            if dodgechance > evasion:
                                damage = enemymagicattack * wind_weakness + randint(enemymagicalsecurity * -1,
                                                                                    enemymagicalsecurity) - (
                                             magicdefense)
                                damage = math.ceil(damage)
                                if damage < 0: damage = 0
                                health -= damage
                                Display(enemyname + " launched a gust of wind! " + str(
                                    damage) + " damage to " + self.heroname + "!")
                            elif dodgechance <= evasion:
                                Display(enemyname + " launched a gust of wind! " + self.heroname + " dodged it!")
                            enemymagic -= 20
                        else:
                            Display(enemyname + " tried to launch a gust of wind, but didn't have enough Magic...")
                    elif enemymove == "Aqua Blast":
                        if enemymagic > 20:
                            dodgechance = randint(1, 125)
                            if dodgechance > evasion:
                                damage = enemymagicattack * water_weakness + randint(enemymagicalsecurity * -1,
                                                                                     enemymagicalsecurity) - (
                                             magicdefense)
                                damage = math.ceil(damage)
                                if damage < 0: damage = 0
                                health -= damage
                                Display(enemyname + " shot a jet of cold water! " + str(
                                    damage) + " damage to " + self.heroname + "!")
                            elif dodgechance <= evasion:
                                Display(enemyname + " shot a jet of cold water! " + self.heroname + "dodged it!")
                            enemymagic -= 20
                        else:
                            Display(enemyname + " tried to shoot a jet of cold water, but didn't have enough Magic...")
                    elif enemymove == "Abyss":
                        if enemymagic > 25:
                            dodgechance = randint(1, 200)
                            if dodgechance > evasion:
                                damage = (enemymagicattack * dark_weakness + randint(enemymagicalsecurity * -1,
                                                                                     enemymagicalsecurity)) - (
                                             magicdefense)
                                damage = math.ceil(damage)
                                health = - damage
                                Display(enemyname + " engulfed " + self.heroname + " in darkness! " + str(
                                    damage) + " damage to " + self.heroname + "!")
                            elif dodgechance <= evasion:
                                Display(
                                    enemyname + " engulfed " + self.heroname + " in darkness, but nothing happened?")
                            enemymagic -= 25
                        else:
                            Display(
                                enemyname + " wanted to engulf " + self.heroname + " in darkness, but didn't have enough Magic...")
                    elif enemymove == "Holy Arrow":
                        if enemymagic >= 25:
                            dodgechance = randint(1, 200)
                            if dodgechance > evasion:
                                damage = (enemymagicattack * light_weakness + randint(enemymagicalsecurity * -1,
                                                                                      enemymagicalsecurity)) - (
                                             magicdefense)
                                damage = math.ceil(damage)
                                health -= damage
                                Display(enemyname + " shot a radiant arrow. " + str(
                                    damage) + " damage to " + self.heroname + "!")
                            elif dodgechance <= evasion:
                                Display(enemyname + " shot a radiant arrow at " + self.heroname + ", but it missed...")
                            enemymagic -= 25
                        else:
                            Display(
                                enemyname + " tried to shoot a radiant arrow at " + self.heroname + ", but didn't have enough Magic...")
                    elif enemymove == "Transform":
                        enemyhealth = health
                        enemymagic = magic
                        enemyphysicalattack = physicalattack
                        enemyphysicaldefense = physicaldefense
                        enemyspeed = speed
                        enemyevasion = evasion
                        enemymagicattack = enemymagicattack
                        enemymagicdefense = magicdefense
                        enemyphysicalsecurity = physicalsecurity
                        enemymagicalsecurity = enemymagicalsecurity
                        enemymoveset = playermoveset
                        Display(enemyname + " transformed into " + heroname + "!")

                elif enemychoice == 3.14159265:
                    damage = enemyphysicalattack + randint(enemyphysicalsecurity * -1, enemyphysicalsecurity)
                    damage = math.ceil(damage)
                    enemyhealth -= damage
                    Display(enemyname + " did " + str(damage) + " damage to themselves in confusion!")

            elif nextmove <= speed:
                Display("What will " + self.heroname + " do?")
                while playerchoice >= 100:
                    sleep(1)
                if rage > 0: playerchoice = 1
                if confusion > 0: playerchoice = 3.14159265
                if paralysis > 0: playerchoice = 0

                if playerchoice == 1:
                    # Player Attack
                    damage = (physicalattack + randint(physicalsecurity * -1, physicalsecurity)) - (
                        enemyphysicaldefense)
                    damage = math.ceil(damage)
                    dodgechance = randint(1, 125)
                    if dodgechance > enemyevasion and damage > 0:
                        health -= damage
                        Display(self.heroname + " attacks! " + str(damage) + " damage to " + enemyname + ".")
                    elif dodgechance <= evasion:
                        Display(self.heroname + " attacks! " + enemyname + " dodged the attack.")
                    elif damage <= 0:
                        Display(self.heroname + " attacks! " + enemyname + " blocked the attack.")

                elif playerchoice == 2:
                    # Player Move
                    playermove = choice(playermoveset)
                    if playermove == "Identify":
                        Display(self.heroname + " examined " + enemyname + ".\nHealth:" + str(enemyhealth) + "/" + str(
                            enemy[1] * 10) + "\nSpirit:" + str(enemymagic) + "/" + str(
                            enemy[2] * 10) + "\nAttack:" + str(enemyphysicalattack) + "\nDefense:" + str(
                            enemyphysicaldefense) + "\nSpeed:" + str(enemyspeed) + "\nEvasion:" + str(
                            enemyevasion) + "\nMagicAttack:" + str(enemymagicattack) + "\nMagicDefense:" + str(
                            enemymagicdefense))
                        Display(enemyname + "'s moves:" + str(enemymoveset))
                    if playermove == "Heal":
                        if magic >= 20 and health < Vitality * 10:
                            healing = magicdefense * 2 + magicattack + randint(magicalsecurity * -2,
                                                                               magicalsecurity * 2)
                            health += healing
                            Display(self.heroname + " healed themselves; " + str(healing) + " HP gained!")
                            magic -= 20
                        elif magic < 20:
                            status = api.update_status(
                                status=self.heroname + " tried to heal themselves, but didn't have enough magic...")
                            print(self.heroname + " tried to heal themselves, but didn't have enough magic.")
                        elif health >= Vitality * 10:
                            status = api.update_status(
                                status=self.heroname + " tried to heal themselves, but was already at full health...")
                            print(self.heroname + " tried to heal themselves, but already has full health...")
                    if playermove == "Fireball":
                        if magic >= 25:
                            dodgechance = randint(1, 125)
                            if dodgechance > enemyevasion:
                                damage = (magicattack * enemyfire_weakness + randint(magicalsecurity * -1,
                                                                                     magicalsecurity) - (
                                              enemymagicdefense))
                                damage = math.ceil(damage)
                                if damage < 0: damage = 0
                                enemyhealth -= damage
                                Display(self.heroname + " threw a fireball! " + str(damage) + " to " + enemyname + "!")
                            elif dodgechance <= evasion:
                                Display(self.heroname + " threw a fireball! " + enemyname + " dodged it!")
                            magic -= 25
                        else:
                            Display(self.heroname + " wanted to throw a fireball, but didn't have enough Magic...")
                    if playermove == "Lightning":
                        print("dab")

                elif playerchoice == 3:
                    # Player Inventory
                    if health < Vitality * 0.8 and Items["Apples"] > 0:
                        health += Vitality * 0.8
                        Display(self.heroname + " ate an apple. Recovered " + str(Vitality * 0.8) + " health!")

                elif playerchoice == 3.14159265:
                    damage = physicalattack + randint(physicalsecurity * -1, physicalsecurity)
                    damage = math.ceil(damage)
                    health -= damage
                    Display(self.heroname + " did " + str(damage) + " damage to themselves in confusion!")

            sleep(5)
            playerchoice = 100

        if enemyhealth <= 0:
            Display(enemyname + " has been slain! " + self.heroname + " recived " + str(enemyexperience) + " Points!")
            Points += enemyexperience

        if health <= 0:
            Display(self.heroname + " has been slain.")
            sys.exit()

    def on_status(self, status):
        turns = + 1
        moved = 0
        command = status.text
        print("Recived:\n" + command + "\n")
        # Naming the hero
        if self.heroname == "Blank":
            self.heroname = command[12:]
            if len(self.heroname) > 20:
                self.heroname = self.heroname[:20]
            # , in_reply_to_status_id = status.id?
            Display("The hero's name shall be " + self.heroname + "!")

        # Command outside battle
        elif self.heroname != "Blank" and self.battling == 0:
            splitcommand = command.split(" ")

            if "improve" in command:
                amount = 0
                if splitcommand[4] in splitcommand:
                    amount = splitcommand[4]
            #        else:
            #            amount = Points
            #        if "Vitality" in command: Vitality += amount, Display(self.heroname + " allocated " + str(amount) + " Points into Vitality.")
            #        if "Spirit" in command: Spirit += amount, Display(self.heroname + " allocated " + str(amount) + " Points into Spirit.")
            #        Points -= amount

            elif splitcommand[2] in splitcommand and type(int(splitcommand[2])) == type(1):
                steps = int(splitcommand[2])
                if steps <= Movement:
                    if "right" in splitcommand[1]:
                        self.heroX += steps
                    elif "left" in splitcommand[1]:
                        self.heroX -= steps
                    elif "up" in splitcommand[1]:
                        self.heroY += steps
                    elif "down" in splitcommand[1]:
                        self.heroY -= steps
                    Display(self.heroname + " moved right " + str(steps) + " steps.\nCurrent position: (" + str(
                        self.heroX) + "," + str(self.heroY) + ")")
                    moved = 1
                else:
                    Display("Not enough Movement for that distance!")
                    moved = 0
            else:
                Display("Invalid syntax. Please")
                moved = 0

            sleep(5)

            # Finding items
            if moved == 1:
                itemchance = randint(1, 100)
                if itemchance == 1:
                    Items["Apples"] += 1
                    Display(self.heroname + " found an apple.")

                elif itemchance <= 100 and "Fireball" not in Moves:
                    Display(self.heroname + " found a scroll for the move 'Fireball!'")
                    Moves.append("Fireball")

            # Encountering enemies
            battlechance = 1  # randint(1, 3)
            if battlechance == 1 and moved == 1:
                self.define_fight()
                self.fight(Vitality, Spirit, Strength, Guard, Agility, Movement, Intellect, Wisdom, Skill, Luck, Moves,
                           Items, Points, status)

            if self.heroX == goalX and self.heroY == goalY:
                Display(self.heroname + " reached the objective. Congratulations, you won!\nTurns: " + str(turns))
                sys.exit()

        elif self.heroname != "Blank" and self.battling == 1:
            if "attack" in command: playerchoice = 1
            if "special" in command: playerchoice = 2
            if "item" in command: playerchoice = 3


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
myStream.filter(track=["#TweepQuest"], newasync=True)