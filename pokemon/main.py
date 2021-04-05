#!/usr/bin/env python3
"""SC Research || Author: ShawnCharles@protonmail.com"""
"Pokemon Classes and useful dictionaries"
import crayons
import random
from assets.chadtricks import clear, print1by1, video
from assets.rooms import rooms
from assets.descriptions import descriptions
import json
#to start and stop music if we werent in virtual environment
#import pygame.mixer

class Pokemon:
    def __init__(self,pokemonId,level):
        self.level = level
        self.id = pokemonId
        with open('assets/pokedex.txt',"r") as pokedex:
            stats = pokedex.readlines()
            self.name = stats[0].split("-")[pokemonId]
            self.attack = stats[1].split("-")[pokemonId]
            self.hp = {"base":int(stats[3].split("-")[pokemonId]), "max": (1+(level/25))*int(stats[3].split("-")[pokemonId]),"current":(1+(level/25))*int(stats[3].split("-")[pokemonId])}

            self.defense = stats[2].split("-")[pokemonId]
            self.speed = stats[4].split("-")[pokemonId]
            self.spAttack = stats[6].split("-")[pokemonId]
            self.spDefense = stats[5].split("-")[pokemonId]
            self.move1 = stats[7].split(".")[pokemonId]
            self.move2 = stats[8].split(".")[pokemonId]
            self.move3 = stats[9].split(".")[pokemonId]
            self.move4 = stats[10].split(".")[pokemonId]
            self.growth = 1+(level/25)

##Evolutions - nested Classes - Bulbasaur is-a Ivysaur, Ivysaur is-a Venusaur
##dont have time to do

class Player:
    def __init__(self,room,inventory,badges,skills,pokemon):
        self.currentRoom = room
        self.inventory=inventory
        self.badges = badges
        self.skills = skills
        self.pokemon = pokemon

class Trainer(Player):
  def __init__(self, name, pokemon):
    super().__init__('',[],[],[],pokemon)
    self.name = name

#    start of save feature
#def loadPlayer(player):
   #"""load user data at start of game"""
    # Open the file in append & read mode ('a+')
    #with open("assets/user.txt", "a+") as user:
        # Move read cursor to the start of file.
        #user.seek(0)
        # If file is not empty then append '\n'
        #data = user.read(100)
        #if len(data) > 0:
        #user.write("\n")
        # Append text at the end of file
        #user.write("hello")

def validAction(action,player):
    currentPokemon = player.pokemon[0]
    validActions = {
            "R":True,
            "RUN":True,
            "C":True,
            "CATCH":True,
            currentPokemon.move1.upper():True,
            currentPokemon.move2.upper():True,
            currentPokemon.move3.upper():True,
            currentPokemon.move4.upper():True
            }
    if action in validActions:
        return True
    else:
        return False


def battle(player1, ai):
    """Battle Logic"""
    emoticons = [crayons.red("Θ"),f"(╯°□°)╯",f"(╯°□°)╯︵{crayons.red('◓')}",f"{crayons.yellow('ϞϞ')}({crayons.red('๑')}⚈ ․ ⚈{crayons.red('๑')})∩","><(((o.^.o)","ଘ @(￣▵—▵￣)v(￣▵▵￣)@ ଓ",">(8☉)@@@oo<>","(>￣ー￣)"]
    vid = [f"(╯°□°)╯  "+ emoticons[7],f"(╯°□°)╯︵"+emoticons[7],f"(╯°□°)╯︵{crayons.red('◓')}",f"(╯°□°)╯ ︵{crayons.red('◓')}",f"(╯°□°)╯ {crayons.red('◓')}︵",f"(╯°□°)╯ ︵{crayons.red('◓')}",f"(╯°□°)╯ {crayons.red('◓')}︵",f"(╯°□°)╯ {crayons.red('◓')}"] 
    clear()
    defeated = []
    if len(ai.pokemon)<2:
        #wild encounter
        print(f"A wild {ai.pokemon[0].name} has appeared!")
        while True:
            currentPokemon = player1.pokemon[0]
            wildPokemon = ai.pokemon[0]
            print('{0:<}              {1:>}'.format(currentPokemon.name,wildPokemon.name))
            print('{0:<}              {1:>}'.format(f"lvl: {currentPokemon.level}",wildPokemon.level))
            print('{0:<}              {1:>}'.format(f"hp:  {currentPokemon.hp['current']}",wildPokemon.hp["current"]))
            if wildPokemon.hp["current"]<=0:
                clear()
                print("You won the battle!")
                player1.pokemon[0] = Pokemon(currentPokemon.id,currentPokemon.level+1)
                return player1
            print(f"You can (R)un,\n use {player1.pokemon[0].move1}, {player1.pokemon[0].move2}, {player1.pokemon[0].move3}, {player1.pokemon[0].move4},\n or try to (C)atch {ai.pokemon[0].name}")
            action = None
            while validAction(action,player1) == False:
                action = input(f"<{crayons.red('◓')}>").upper()
            if action=="R" or action=="RUN":
                return player1
            elif action=="C" or action=="CATCH":
                video(vid)
                if random.random() > 0.5:
                    print(f"You caught {wildPokemon.name}")
                    return player1
                else:
                    clear()
                    print(vid[0])
                    print(f"{wildPokemon.name} broke free!")

                #will save pokemon if team > 5
            else:
                ##Attack process
                wildPokemon.hp["current"]-= int(currentPokemon.attack)*currentPokemon.growth

    else:
            #trainer battle
        print(f"{ai.name} wants to battle!")
        while True:
            if ai.pokemon[0].hp["current"]<=0:
                clear()
                print(f"You defeated {ai.pokemon[0].name}!")
                ai.pokemon.remove(ai.pokemon[0])
                ##levelup Pokemon
                player1.pokemon[0] = Pokemon(currentPokemon.id,currentPokemon.level+1)
                print(f"{player1.pokemon[0].name} leveled up!")
            if len(ai.pokemon)<=0:
                clear()
                print(f"You defeated {ai.name}!")
                #levelup
                player1.pokemon[0] = Pokemon(currentPokemon.id,currentPokemon.level+1)
                return player1
            #currentPokemon fainted
            if player1.pokemon[0].hp["current"]<=0:
                print(player1.pokemon[0].name,"has fainted!")
                player1.pokemon.sort(key=lambda poke:poke.hp["current"],reverse=True)
                if player1.pokemon[0].hp["current"]<=0:
                    ##All pokemon faint
                    clear()
                    print("You fainted!")
                    print("You wake up in Pallet Town!")
                    player1.currentRoom = "Pallet Town"
                    return player1
            currentPokemon = player1.pokemon[0]
            wildPokemon = ai.pokemon[0]
            print('{0:<}             {1:>}'.format(currentPokemon.name,wildPokemon.name))
            print('{0:<}                  {1:>}'.format(f"lvl: {currentPokemon.level}",wildPokemon.level))
            print('{0:<}              {1:>}'.format(f"hp:  {currentPokemon.hp['current']}",wildPokemon.hp["current"]))
            action = None
            print(f"You can (R)un,\n use {player1.pokemon[0].move1}, {player1.pokemon[0].move2}, {player1.pokemon[0].move3}, {player1.pokemon[0].move4}")
            while validAction(action,player1) == False:
                action = input(f"<{crayons.red('◓')}>").upper()
            if action=="R" or action=="RUN":
                return player1
            else:
                ##Attack process
                wildPokemon.hp["current"]-= int(currentPokemon.attack)*currentPokemon.growth
                currentPokemon.hp["current"]-= int(wildPokemon.attack)*wildPokemon.growth
                clear()
                print(f"{currentPokemon.name} dealt {int(currentPokemon.attack)*currentPokemon.growth} points of damage")
                print(f"{wildPokemon.name} dealt {int(wildPokemon.attack)*wildPokemon.growth} points of damage")
                

def grass(player):
    """simulates random encounters"""
    if random.random()>0.5:
        pokemonId = random.choice(rooms[player.currentRoom]["pokemon"]["ids"])
        roomLevel = rooms[player.currentRoom]["pokemon"]["level"]
        level = random.randrange(roomLevel[0],roomLevel[1])
        player = battle(player,Trainer("chad",[Pokemon(pokemonId,level)]))
        return player
    else:
        return player

def gymBattle(player):
    """returns player after running Gym Battle"""
    player = battle(player,Trainer("Gym Leader",[Pokemon(56,12),Pokemon(23,34),Pokemon(87,98),Pokemon(41,42)]))
    return player

def articunoBattle(player):
    """returns player after running Legendary Battle"""
    player = battle(player,Trainer("Legendary",[Pokemon(144,65)]))
    return player

def mewTwoBattle(player):
    """returns player after running Legendary Battle"""
    player = battle(player,Trainer("Legendary",[Pokemon(150,65)]))
    return player

def mewBattle(player):
    """returns player after running Legendary Battle"""
    player = battle(player,Trainer("Legendary",[Pokemon(151,65)]))
    return player
def heal(player):
    for pokemon in player.pokemon:
        pokemon.hp['current']=pokemon.hp['max']
    clear()
    print("Your pokemon have been healed!")
    return player

def showInstructions():
    ##write good instructions

  #print a main menu and the commands
    print('''
Pokemon
========
Commands:
  go [direction]
  get [item]
  talk [person]
  use [skill]
  q (quit)
''')

def main():
    clear()
    validCommands = ["get","go","use", "fly","cut","climb", "surf", "hidden power", "flash","dig"]
    player = Player("Pallet Town", [],[],["fly","dig","surf","cut","strength","hidden power","flash"],[Pokemon(25,95),Pokemon(25,150), Pokemon(6,95),Pokemon(25,95)])
    move= ""
    inventory=[]
    emoticons = [crayons.red("Θ"),f"(╯°□°)╯",f"(╯°□°)╯︵{crayons.red('◓')}",f"{crayons.yellow('ϞϞ')}({crayons.red('๑')}⚈ ․ ⚈{crayons.red('๑')})∩","><(((o.^.o)","ଘ @(￣▵—▵￣)v(￣▵▵￣)@ ଓ",">(8☉)@@@oo<>","(>￣ー￣)"]
    vid = [f"(╯°□°)╯  "+ emoticons[7],f"(╯°□°)╯︵"+emoticons[7],f"(╯°□°)╯︵{crayons.red('◓')}","(╯°□°)╯ ︵{crayons.red('◓')}","(╯°□°)╯ {crayons.red('◓')}︵","(╯°□°)╯ ︵{crayons.red('◓')}","(╯°□°)╯ {crayons.red('◓')}︵",f"(╯°□°)╯ {crayons.red('◓')}"]
    #Didnt have time to finish saves
    #loadPlayer()
    def showStatus():
  #print the player's current status
  #remove items from map that are in inventory
        for item in inventory:
            if item in rooms[player.currentRoom]["items"]:
                rooms[player.currentRoom]["items"].remove(item)
        print('Inventory :',inventory)
        print('Locations :',rooms[player.currentRoom]["locations"])
        print('Skills:',player.skills)
        print("You can go", ", ".join(rooms[player.currentRoom]['directions']))
        print('---------------------------')
        print('You are in',player.currentRoom)
        with open("assets/descriptions.txt","r") as allDescriptions:
  #print the Current Room description
            objects = allDescriptions.read().splitlines()
            for index,obj in enumerate(objects):
                if obj.split(" : ")[0]== player.currentRoom:
                    print(objects[index].split(" : ")[1])
                elif obj.split(" : ")[0] in rooms[player.currentRoom]["items"]:
                    print(objects[index].split(" : ")[1])
                    
    #clear()
    #showInstructions()
    
    #plays music but server doesnt have speakers
    #pygame.mixer.init()
    #pygame.mixer.music.load("assets/music/battle.mp3")
    #pygame.mixer.music.play()
    #while pygame.mixer.music.get_busy() == True:
    #    continue


    while True and move !="q":
        ##if fail, load found file into game - version2
        ##Battle Sequence and leveling pokemon - accomplished
        ##Route Logic making a pokemon appear conditional before status message- accomplished
        ##1Puzzle
        ##Skill directions
        ##Skill Event 
        ##1Gym - accomplished
        if player.currentRoom[0]=="R":
            player = grass(player)
        
        if player.currentRoom=="Mt. Silver" and "Kings Rock" in inventory:
            player = articunoBattle(player)
        
        showStatus()
        move= ""
        while move == '':
            move=input(f"<{crayons.red('◓')}>")
        move = move.lower().split(" ", 1)

        #if they type 'go' first
        if move[0] == 'go':
    #check that they are allowed wherever they want to go
            if move[1] in rooms[player.currentRoom]["directions"]:
      #set the current room to the new room
                player.currentRoom = rooms[player.currentRoom]["directions"][move[1]]
                clear()
            elif move[1] in rooms[player.currentRoom]["locations"]:
                if move[1] == "gym":
                    player=gymBattle(player)
                if move[1] == "pokecenter":
                    player=heal(player)
            else:
                clear()
                print('You can\'t go that way!')
        
        
        elif move[0] == 'fly':
            if move[1].title() in rooms:
                player.currentRoom = move[1].title()
                clear()
            else:
                print('You can\'t fly there!')
        
        elif move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
            if move[1].title() in rooms[player.currentRoom]["items"]:
      #add the item to their inventory
                move[1] = move[1].title()
                inventory += [move[1]]
      #display a helpful message
                clear()
                print(f"You put {move[1]} in your inventory")
    
      #delete the item from the room
                rooms[player.currentRoom]['items'].remove(move[1])
    #otherwise, if the item isn't there to get
            else:
      #tell them they can't get it  
                clear()
                print('Can\'t get ' + move[1] + '!')

        elif move[0] == 'help' :
            clear()
            showInstructions()
        else:
            clear()
            print("Say That Again Please!")

if __name__=="__main__":
    main()

