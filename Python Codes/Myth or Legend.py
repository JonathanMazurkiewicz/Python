#Jonathan Mazurkiewicz
#Dillon Stickler, 'Will of a thousand errors'
#Do Not Alter Code!

import time
import random

charcreate = True
characterdeny = True

class Player(object):
    def __init__(self, name, creature, order, health, speed, defense, attack):
        self.name = name
        self.creature = creature
        self.order = order
        self.health = health
        self.speed = speed
        self.defense = defense
        self.attack = attack

    def dead(self):
        if self.health <= 0:
            while self.health <= 0:
                print("You have Died.")
        else:
            print("You have Died.")
        
    def creatures(self):
        if self.creature == "DWARF":
            self.speed = 70
            self.health = 140
            self.defense = 160
        elif self.creature == "ELF":
             self.speed = 120
             self.health = 80
             self.defense = 130
        elif self.creature == "HUMAN":
             self.speed = 100
             self.health = 100
             self.defense = 115
        elif self.creature == "HOBBIT" or self.creature == "HALFLING":
             self.speed = 115
             self.health = 100
             self.defense = 90
#Undead Creature
        else:
            print("That creature as gone extinct, you are now an undead")
            self.creature = "UNDEAD"

    def Class(self):
        if self.order == "MAGE":
            self.attack = 125
        elif self.order == "WARRIOR":
            self.attack = 133
            self.speed = self.speed - 20
            self.defense = self.defense + 30
        elif self.order == "ARCHER":
            self.attack = 118
        elif self.order == "ROGUE":
            self.attack = 100
            self.speed = self.speed + 30
            self.defense = self.defense - 10
#Trainee Class
        else:
            print("You didn't choose a valid class, you are now a trainee")
            self.attack = 50
            self.order = "TRAINEE"

class Enemy(object):
    def __init__(self, name, creature, order, health, speed, defense, attack):
        self.name = name
        self.creature = creature
        self.order = order
        self.health = health
        self.speed = speed
        self.defense = defense
        self.attack = attack
        
    def creatures(self):
#Enemy Only Creatures
        if self.creature == "Dummy":
             self.speed = 30
             self.health = 350
             self.defense = 30
        elif self.creature == "Drunkard":
             self.speed = 70
             self.health = 130
             self.defense = 80
        elif self.creature == "Monster":
             self.speed = 140
             self.health = 360
             self.defense = 250
        elif self.creature == "Titan":
             self.speed = 200
             self.health = 500
             self.defense = 300
        elif self.creature == "Primordial":
             self.speed = 250
             self.health = 1000
             self.defense = 500

    def Class(self):
#Enemy Only Classes
        if self.order == "Dummy":
            self.attack = 10
        elif self.order == "Will of a thousand beers":
            self.attack = 125
        elif self.order == "Chimera":
            self.attack = 150
        elif self.order == "Lord of Time":
            self.attack = 175
        elif self.order == "Lord of the Pit":
            self.attack = 350

            

def charprint():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Name:")
    print(player.name)
    print("")
    print("Creature:")
    print(player.creature)
    print("")
    print("Class:")
    print(player.order)
    print("")
    print("Health:")
    print(player.health)
    print("")
    print("Speed:")
    print(player.speed)
    print("")
    print("Defense:")
    print(player.defense)
    print("")
    print("Attack:")
    print(player.attack)
    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def charactercreate():
    global charcreate
    global player
    if charcreate == True:
        player = Player(input("Name of Character: "),input("Are you a Dwarf, Elf, Human, or a Halfling? ").upper(),input("Are you a Mage, Warrior, Archer, or Rogue? ").upper(),int(40),int(40),int(40),int(20))
        player.creatures()
        player.Class()
        charprint()
        charcreate = False

def charchoice():
    global charcreate
    global characterdeny
    while characterdeny == True:
        x = input("Is this what you want? Yes or No. ").upper()
        if x == "NO":
            charcreate = True
            charactercreate()
        elif x == "YES":
            print("")
            print("Best of Luck")
            characterdeny = False

#Enemies
#Name, Creature, Class, Health, Speed, Defense, Attack        
e1 = Enemy("Training Dummy", "Dummy", "Dummy", int(350), int(30), int(30), int(10))
e1.creatures()
e1.Class()
e2 = Enemy("Local Drunk", "Drunkard", "Will of a thousand beers", int(130), int(70), int(80), int(125))
e2.creatures()
e2.Class()
e3 = Enemy("Bandit", "ELF", "ROGUE", int(80), int(150), int(120), int(100))
e3.creatures()
e3.Class()
e4 = Enemy("Possessed", "HUMAN", "WARRIOR", int(100), int(80), int(145), int(133))
e4.creatures()
e4.Class()
e5 = Enemy("Chimera", "Monster", "Chimera", int(360), int(140), int(250), int(150))
e5.creatures()
e5.Class()
e6 = Enemy("Saturn", "Titan", "Lord of Time", int(500), int(200), int(300), int(175))
e6.creatures()
e6.Class()
e7 = Enemy("The Ancient Being of the Pit", "Primordial", "Lord of the Pit", int(1000), int(250), int(500), int(350))
e7.creatures()
e7.Class()

#Character Create Code
charactercreate()
charchoice()

#Fighting Code

#Health - ((Attack / Defense) * 10)
#Player Speed - Enemy Speed. greater than 0 goes first
#Healh + (Health/10)
f = 0

def F():
    global f
    f = int(f)
    f = f + 1
    return f

if player.creature == "DWARF":
    max_health = 140
elif player.creature == "ELF":
    max_health = 80
elif player.creature == "HUMAN":
    max_health = 100
elif player.creature == "HOBBIT" or player.creature == "HALFLING":
    max_health = 100
else:
    max_health = 40

t = 0
u = 0
v = 0
w = 0
x = ""
y = ""
z = ""

def fight():
    global f
    F()
    global t
    global u
    global v
    global w
    global x
    global y
    global z

    if f == 1:
        t = e1.health
        u = e1.defense
        v = e1.attack
        w = e1.speed
        x = e1.name
        y = e1.creature
        z = e1.order
    elif f == 2:
        t = e2.health
        u = e2.defense
        v = e2.attack
        w = e2.speed
        x = e2.name
        y = e2.creature
        z = e2.order
    elif f == 3:
        t = e3.health
        u = e3.defense
        v = e3.attack
        w = e3.speed
        x = e3.name
        y = e3.creature
        z = e3.order
    elif f == 4:
        t = e4.health
        u = e4.defense
        v = e4.attack
        w = e4.speed
        x = e4.name
        y = e4.creature
        z = e4.order
    elif f == 5:
        t = e5.health
        u = e5.defense
        v = e5.attack
        w = e5.speed
        x = e5.name
        y = e5.creature
        z = e5.order
    elif f == 6:
        t = e6.health
        u = e6.defense
        v = e6.attack
        w = e6.speed
        x = e6.name
        y = e6.creature
        z = e6.order
    elif f == 7:
        t = e7.health
        u = e7.defense
        v = e7.attack
        w = e7.speed
        x = e7.name
        y = e7.creature
        z = e7.order

    block = False
    print("You are fighting:",x)
    print("It is a:",y)
    print("It's class is:",z)
    time.sleep(1.5)
    battle = True
    while battle == True:
        print("-------------------------------")
        print("~()~()~()~()~()~()~()~()~()~()~")
        print("-------------------------------")
        speed = player.speed - w
        if speed > 0:
            a = input("What action do you do? Attack, Block or Heal: ").upper()
            if a == "ATTACK" or a == "A":
                RNG = random.randint (0, 10)
                if RNG < 8:
                    print("You Attacked")
                    t = t - ((player.attack/u)*10)
                    print("Enemy Health",t)
                else:
                    print("You Missed")
                    t = t
                    print("Enemy Health",t)
            elif a == "BLOCK" or a == "B":
                RNG = random.randint (0,7)
                if RNG < 6:
                    print("You have successfully blocked")
                    block = True
                else:
                    print("Your Block has failed")
                    block = False
            elif a == "HEAL" or "H":
                if max_health <= player.health:
                    print("You are at max health")
                elif max_health > player.health:
                    player.health = player.health + (max_health/10)
            RNG = random.randint (0, 10)
            if RNG < 8:
                print("The Enemy Attacked")
                if block == False:
                    print("You take damage")
                    player.health = player.health - ((v/player.defense)*10)
                    print("Health",player.health)
                elif block == True:
                    print("You take no damage")
                    print("Health",player.health)
                    block = False
            else:
                print("The Enemy Missed")
                player.health = player.health
                print("Health",player.health)
        elif speed <= 0:
            RNG = random.randint (0, 10)
            if RNG < 8:
                print("The Enemy Attacked")
                if block == False:
                    print("You take damage")
                    player.health = player.health - ((v/player.defense)*10)
                    print("Health",player.health)
                elif block == True:
                    print("You take no damage")
                    print("Health",player.health)
                    block = False
            else:
                print("The Enemy Missed")
                player.health = player.health
            a = input("What action do you do? Attack, Block or Heal: ").upper()
            if a == "ATTACK" or a == "A":
                RNG = random.randint (0, 10)
                if RNG < 8:
                    print("You Attacked")
                    t = t - ((player.attack/u)*10)
                    print("Enemy Health",t)
                else:
                    print("You Missed")
                    t = t
                    print("Enemy Health",t)
            elif a == "BLOCK" or a == "B":
                RNG = random.randint (0,7)
                if RNG < 6:
                    print("You have successfully blocked")
                    block = True
                else:
                    print("Your Block has failed")
                    block = False
            elif a == "HEAL" or "H":
                if max_health <= player.health:
                    print("You are at max health")
                elif max_health > player.health:
                    player.health = player.health + (max_health/10)
        if player.health <= 0:
            print("You Have Died")
            player.dead()
        elif t <= 0:
            print("You have won this battle")
            player.creatures()
            print("Health",player.health)
            print("You have gained strength")
            player.attack = player.attack + 20
            player.defense = player.defense + 20
            print("Attack",player.attack)
            print("Defense",player.defense)
            time.sleep(2)
            battle = False

#Story/Game Code
time.sleep(2)
print("")
print("~Story Line~")
time.sleep(2)
print("")
print("It was ten centuries ago that they came to Terra")
time.sleep(2)
print("The Elders thought that they would be easy to defend against")
time.sleep(2)
print("...")
time.sleep(2)
print("They were wrong")
time.sleep(2)
print("The creatures of the pit destroyed our civilization, it is up to you now to rid the world of this evil")
time.sleep(2)
print("This is what you were born to do. It is as the Moirai decided. You are our last hope.",player.name,", Please save Terra.")
time.sleep(2)
print("This is where your story begins...")
print("-------------------------------")
time.sleep(2.5)
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
time.sleep(2.5)
print("...ke Up!",player.name,"You need to wake Up!")
print("It is time for you to train.")
time.sleep(2)
print("I have set up a training dummy for you to fight against")
fight()
time.sleep(1.5)
print("")
print("You have defeated the dummy")
time.sleep(1.5)
print("There has been a disturbance in town that we caught wind of")
print("The drunkard has been causing trouble again")
time.sleep(1.5)
print("I want you to go handle him before your journey starts")
print("-------------------------------")
time.sleep(2)
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
time.sleep(1)
print("--You enter the nearby town~~")
print("--The drunk is yelling obscenities--")
print("--You approach the drunk--")
print("~~He lunges at you~~")
time.sleep(2)
fight()
time.sleep(1.5)
print("")
print("You have managed to simply knock the drunk out")
print("I am surprised it took that much trouble")
print("I think that, while you have far to go, you will be prepared by the time you reach the Source")
time.sleep(2)
print("--You set out on your journey to reach the Source, the location of where the Lord is--")
print("--You pack up what belongings that you have and set out on your journey--")
print("-------------------------------")
time.sleep(2.5)
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
time.sleep(1)
print("--You see a figure off in the distance at the bridge--")
print("--You realise that it's a bandit that took over the bridge--")
time.sleep(1.5)
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
time.sleep(1)
print("--You approach the bridge and are spotted by the bandit--")
print("= You must pay a toll before you cross my bridge =")
print("= You must either pay or go back the way you went =")
time.sleep(1)
print("--This is the only bridge within 15 leagues--")
print("--You also don't want to pay the bandit in gold, so you decide to pay him in steel--")
time.sleep(2)
fight()
time.sleep(1.5)
print("")
print("--You leave the bandit to recover from his wounds that he gained from your fight--")
print("Nice job at beating the bandit")
print("--You realise that your teacher is nowhere near you and yet you can hear him as clear as if he was right beside you--")
print("--You then put it out of mind and continue on your journey--")
print("-------------------------------")
time.sleep(1)
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
time.sleep(1.5)
print("--You hear a noise that sounds like a groan--")
time.sleep(2)
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
time.sleep(1.5)
print("--You hear the groan again except that it sounds closer than before--")
time.sleep(2)
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
time.sleep(1.5)
print("--You hear the groan a third time, but, this time you get tackled off your steed by someone--")
time.sleep(1)
print("--You see that they look like they died many years, but you are wondering how it can still move--")
time.sleep(2)
fight()
time.sleep(1.5)
print("")
print("--This was the first time that you ever saw a possessed body--")
time.sleep(1.5)
print("--You rest for a bit before continuing--")
time.sleep(2)
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
time.sleep(1.5)
print("--You meet a being that towers over you, you do not know what or who the being is--")
print("~~I am Saturn, a being of Time. you will have to get passed myself and one other before you reach the Pit~~")
time.sleep(1.5)
print("~~You have to face the Chimera before we fight~~")
time.sleep(1.5)
fight()
time.sleep(2)
print("")
print("~~You fought valiantly, I will allow you a pause before we fight because of the entertainment you gave in your latest fight, and those previously~~")
print("--You become confused, '...and those previously?' it's like he saw them as they happened--")
time.sleep(1.5)
print("~~That confusion on your face can be ridden of because, I am the being of Time, I see all that happens.~~")
time.sleep(1)
print("~~I think that is enough of a rest~~")
time.sleep(1.5)
fight()
time.sleep(2)
print("")
print("~~You fought very well, but there will be more fighting in your future~~")
time.sleep(1.5)
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
time.sleep(1.5)
print("--You can't help but wonder what Saturn meant with his parting message--")
time.sleep(1.5)
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
time.sleep(1.5)
print("--You see a mass of creatures surrounding what seems to be a hole in the ground--")
print("--You realize that it is the Pit, what you have been traveling to get to--")
time.sleep(1.5)
print("--As you approach the creatures, they seem to prepare to attack you--")
time.sleep(1.5)
print("--Before anything can move, you hear a voice thundering over the mass--")
print("Halt, this",player.creature,"is mine to face")
print("--This voice seems familiar--")
time.sleep(1.5)
print("--A path is cleared through the creatures to the Pit--")
print("--You walk down the path, but as you approach the Pit, you notice a man standing at the edge looking into it--")
time.sleep(1.5)
print("I have seen you're travels and seen that you will give a good challenge when you fight the being of the Pit himself")
print("--You realize why the voice was famliar, he is your old teacher--")
time.sleep(2)
print("I see that you recognize me now, my student")
print("But there is no time for catching up as you have to face the being now")
time.sleep(1.5)
print("--He stops you before you jump into the pit--")
print("The being is not in the pit, I am right here")
time.sleep(1.5)
fight()
time.sleep(2)
print("")
print("You have given me the challenge I have been waiting for, I am calling back all the creatures that were released")
print("--You watch as all sorts of creatures are jumping into the pit--")
time.sleep(1.5)
print("I will be joining them in a few minutes, I just wish to say farewell")
print("I trained you myself because that would have been the only way to get a worthy fight")
time.sleep(1.5)
print("I pass my title as Lord of the Pit onto you as it was passed unto me millenia ago")
time.sleep(1.5)
player.order = "Lord of the Pit"
time.sleep(1.5)
print("It is time for me to leave")
print("Farewell", player.name)
time.sleep(3)
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("THE END OF THIS LEGEND")
time.sleep(2)
print("Ending stats")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Name:")
print(player.name)
print("")
print("Creature:")
print(player.creature)
print("")
print("Class:")
print(player.order)
print("")
print("Health:")
print(player.health)
print("")
print("Speed:")
print(player.speed)
print("")
print("Defense:")
print(player.defense)
print("")
print("Attack:")
print(player.attack)
print("")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
time.sleep(3)
print("YOU WIN")
