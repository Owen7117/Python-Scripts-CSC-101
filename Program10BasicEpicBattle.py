#Program 10 Basic: Epic Battle
#Owen O'Neil
#04/14/24

import random 
class Character:
    def __init__(self, name, classtype, hp, strength, defense):#instance variables
        self.name= name
        self.classtype= classtype
        self.hp= hp
        self.strength= strength
        self.defense= defense
    #getters   
    def getname(self):
        return self.name
    def getclasstype(self):
        return self.classtype
    def gethp(self):
        return self.hp
    def getstrength(self):
        return self.strength
    def getdefense(self):
        return self.defense
    #setters
    def setname(self, name):
        self.name= name
    def setclasstype(self, classtype):
        self.classtype= classtype
    def sethp(self, hp):
        self.hp= hp
    def setstrength(self, strength):
        self.strength= strength
    def setdefense(self, defense):
        self.defense= defense
    #assigning property values   
    _name= property(getname, setname)
    _classtype= property(getclasstype, setclasstype)
    _hp= property(gethp, sethp)
    _strength= property(getstrength, setstrength)
    _defense= property(getdefense, setdefense)
    
    #methods
    def attack(self, def_percent): #attack caluculation 
        return self.strength*(1-def_percent)
    def defend(self, atk_percent): #deffend calculation 
        return atk_percent*(1-self.defense)-6
    def IsStillAlive(self): #check if still alive 
        if self.hp > 0:
            return True
        else:
            return False
  
    def __str__(self):
        return self.name
    
#name and class select
name = input("Choose a name: ") 
CharacterSelect= input("""Choose a Class! 
Sword Fighter: HP= 120, Attack= 40, Defense= 0.2
Unicorn: HP= 80, Atack= 35, Defense= 0.6
Battle Monk: HP= 100, Attack= 20, Defense= 0.42
""")

#assigning user character choice   
if CharacterSelect == "Sword Fighter":
    userCharacter = Character(name, "Sword Fighter", 120, 40, 0.2)
if CharacterSelect == "Unicorn":
    userCharacter = Character(name, "Unicorn", 80, 35, 0.6)
if CharacterSelect == "Battle Monk":
    userCharacter = Character(name, "Battle Monk", 80, 35, 0.6)

#randomly selecting enemy name
namelist=["Hex","Megabite", "Glitch"] 
enemyname= random.choice(namelist)

#randomly selcting a enemy classtype
CharacterList= []
CharacterList.append(Character(enemyname,"Sword Fighter", 120, 40, .2))
CharacterList.append(Character(enemyname,"Unicorn", 80, 35, .6))
CharacterList.append(Character(enemyname,"Batte Monk", 100, 20, .42))
enemyCharacter= random.choice(CharacterList)

print("{} the {}, your opponent is {} the {}!".format(userCharacter.name, userCharacter.classtype, enemyCharacter.name, enemyCharacter.classtype))
enemychoice=["a","d"] #enemy battle options
round_num= 1 #round number

#Battle options and string responses 
while (userCharacter.IsStillAlive() and enemyCharacter.IsStillAlive()):
    print("-Round {}-".format(round_num))
    user_move= input("Do you (a)ttack or (d)efend?") #user chooses to attack or defend
    enemy_move=random.choice(enemychoice) #enemy randomly choses a to attack or defend
    if user_move== "d" and enemy_move== "d":
        #both defend, nothing happens
        print("{} the {} is on guard.".format(userCharacter.name, userCharacter.classtype))
        print("{} the {} is on guard.".format(enemyCharacter.name, enemyCharacter.classtype))
    if user_move== "a" and enemy_move== "a":
        #user attack
        print("{} the {} attacked {} the {}!".format(userCharacter.name, userCharacter.classtype, enemyCharacter.name, enemyCharacter.classtype))
        enemyCharacter.hp -= userCharacter.attack(enemyCharacter.defense)
        print("{} now has {:.2f} hp.".format(enemyCharacter.name, enemyCharacter.hp))
        #enemy attack
        print("{} the {} attacked {} the {}!".format(enemyCharacter.name, enemyCharacter.classtype, userCharacter.name, userCharacter.classtype))
        userCharacter.hp-=enemyCharacter.attack(userCharacter.defense)
        print("{} now has {:.2f} hp.".format(userCharacter.name, userCharacter.hp))
    #enemy defends user's attack
    if user_move == "a" and enemy_move== "d":
        enemyCharacter.hp-= enemyCharacter.defend(userCharacter.strength)
        print("{} the {} attacked {} the {}!".format(userCharacter.name, userCharacter.classtype, enemyCharacter.name, enemyCharacter.classtype))
        print("{} the {} has defended against {} the {}'s attack!".format(enemyCharacter.name, enemyCharacter.classtype, userCharacter.name, userCharacter.classtype))
        print("{} now has {:.2f} hp.".format(enemyCharacter.name, enemyCharacter.hp))
    #user defends enemy's attack
    if user_move == "d" and enemy_move== "a":
        userCharacter.hp-= userCharacter.defend(enemyCharacter.strength)
        print("{} the {} attacked {} the {}!".format(enemyCharacter.name, enemyCharacter.classtype, userCharacter.name, userCharacter.classtype))
        print("{} the {} has defended against {} the {}'s attack!".format(userCharacter.name, userCharacter.classtype, enemyCharacter.name, enemyCharacter.classtype))
        print("{} not has {:.2f} hp.".format(userCharacter.name, userCharacter.hp))
    round_num+=1 #go to next round
                           
#determine winner
if userCharacter.IsStillAlive(): #print if user wins
    print("{} the {} was defeated!".format(enemyCharacter.name, enemyCharacter.classtype))
    print("{} the {} wins!".format(userCharacter.name, userCharacter.classtype))
else:   #print if enemy wins
    print("{} the {} was defeated!".format(userCharacter.name, userCharacter.classtype))
    print("{} the {} wins!".format(enemyCharacter.name, enemyCharacter.classtype))
        