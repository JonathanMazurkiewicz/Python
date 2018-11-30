#Created by Jonathan M.

#Classes
class Player(object):
    def __init__(self, name, height, weight, water, food, health, walk):
        self.name = name
        self.height = height
        self.weight = weight
        self.water = water
        self.food = food
        self.health = health
        self.walk = walk
        
    def Thirst(self):
        water = self.water
        water = int(water)
        self.water = self.water - 15
        return water
    
    def Drink(self):
        water = self.water
        water = int(water)
        print("Drank 'Fluids'")
        self.water = self.water + 60
        return water
    
    def Hunger(self):
        food = self.food
        food = int(food)
        self.food = self.food - 10
        return food
    
    def Eat(self):
        food = self.food
        food = int(food)
        print("Ate sustenance")
        self.food = self.food + 40
        return food
    
    def Damage(self):
        health = self.health
        health = int(health)
        if self.water <= 0 and self.food <= 0:
            self.health = self.health - 3
            return health
        elif self.water <= 0:
            self.health = self.health - 2
            return health
        elif self.food <= 0:
            self.health = self.health - 1
            return health
        
    def Intoxication(self):
        health = self.health
        health = int(health)
        if self.water >= 150:
            self.health = self.health - 150
            print("Killed by Water Intoxication")
            return health
        else:
            print("To Die Or")
    def Diabetes(self):
        health = self.health
        health = int(health)
        if self.food >= 150:
            self.health = self.health - 150
            print("Killed by Obesity")
            return health
        else:
            print("Not To Die")
    def Death(self):
        health = self.health
        health = int(health)
        self.health = self.health - 100
        return health
    
    def Walk(self):
        walk = self.walk
        walk = int(walk)
        self.walk = self.walk + 1
        print("You Walked")
        return walk

    def Fall(self):
        health = self.health
        health = int(health)
        self.health = self.health - 70
        return health
        
    def Squirrel(self):
        health = self.health
        health = int(health)
        self.health = self.health - 15
        return health

    def Win(self):
        health = self.health
        health = int(health)
        self.health = 101
        return health
    
#Misc. Function
def walking():
    if player.walk == 4:
        print("A squirrel is stalking you?")
    elif player.walk == 6:
        print("You realize that there aren't supposed to be red squirrels in Romania...")
    elif player.walk == 9:
        print("You approach a rickety bridge")
        print("You decide to cross the bridge")
        print("The bridge broke while you were crossing")
        print("You took a long fall")
        player.Fall()
    elif player.walk == 16:
        print("~~~A Steam Sale appears~~~")
        print("~~~All your money disappears~~~")
        print("~~~The Steam Sale dissappears~~~")
    elif player.walk == 21:
        print("What is the Name?")
        input("Name please: ")
        print("It may be valid, but, it may also be invalid")
    elif player.walk == 27:
        print("~~~You feel as if something is watching from a distance~~~")
        print("~~~You see nothing other than trees and shadows~~~")
        print("~~~You get a feeling of dread in the air~~~")
    elif player.walk == 32:
        print("The squirrel was stalking you")
        print("It attacked")
        player.Squirrel()
    elif player.walk == 37:
        print("The squirrel came back to attack again")
        print("You punt the squirrel")
    elif player.walk == 40:
        print("You have finally reached the castle in the forest")
        print("...")
        print("You hear footsteps echoing")
        player.Win()

#Actions
def move():
    move = input("What action do you wish to do? ").lower()
    if move == ("walk"):
        player.Walk()
    elif move == ("drink"):
        player.Drink()
    elif move == ("eat"):
        player.Eat()
    elif move == ("die"):
        player.Death()
    else:
        print("Not an action that is possible, or is unclear")

#Characters
player = Player(input("Name[First]:"),input("Height[Feet.Inches]:"),input("Weight[lbs]:"), int(100), int(100), int(100), int(0))

#Game Code
print("Welcome to Iadul pe pamant. Your goal is to reach the Castle in the forest.")
print("The Castle is about 40 miles into the forest")
print("You do NOT want to linger in one place for too long")
print("###Read lines carefully, do not linger on those that damage you other wise you will lose health each time it 'reappears'###")
print("###Read lines carefully, do not linger on damaging events. Otherwise you will die quicker.###")

while player.health > 0 or game == True:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("---Read Carefully---")
    print("You can do these actions:")
    print("Walk, Drink, Eat, and maybe more")
    move()
    walking()
    player.Thirst()
    player.Hunger()
    player.Damage()
    player.Intoxication()
    player.Diabetes()
    print("Water", player.water)
    print("Food", player.food)
    print("Health", player.health)
    print("Do not linger")
    if player.health <= 0:
        print("You Died")
        break
    elif player.health >= 101:
        print("You Win?")
        break
