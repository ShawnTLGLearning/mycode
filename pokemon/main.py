#!/usr/bin/env python3
"Pokemon Classes and useful dictionaries"
import crayons
import random
from assets.chadtricks import clear, print1by1
from assets.rooms import rooms
from assets.descriptions import descriptions
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
            self.move1 = stats[7].split("-")[pokemonId]
            self.move2 = stats[8].split("-")[pokemonId]
            self.move3 = stats[9].split("-")[pokemonId]
            self.move4 = stats[10].split("-")[pokemonId]
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
    
    clear()
    defeated = []
    if len(ai.pokemon)<2:
        #wild encounter
        print(f"A wild {ai.pokemon[0].name} has appeared!")
        while True:
            if ai.pokemon[0].hp["current"]<=0:
                clear()
                print("You won the battle!")
                return player1
            print(f"You can (R)un,\n use {player1.pokemon[0].move1}, {player1.pokemon[0].move2}, {player1.pokemon[0].move3}, {player1.pokemon[0].move4},\n or try to (C)atch {ai.pokemon[0].name}")
            action = None
            while validAction(action,player1) == False:
                action = input(">>").upper()
            if action=="R" or action=="RUN":
                break
            elif action=="C" or action=="CATCH":
                player1.pokemon += [Pokemon(ai.pokemon[0].id,ai.pokemon[0].level)]
                break

    else:
        if len(ai.pokemon)>1:
            #trainer battle
            print(f"{ai.name} wants to battle!")
        while True:
            if ai.pokemon[0].hp["current"]<=0:
                clear()
                print(f"You defeated {ai.pokemon[0].name}!")
                ai.pokemon.remove(ai.pokemon[0])
                print(f"{ai.name} !")
            if len(ai.pokemon)<=0:
                clear()
                print(f"You defeated {ai.name}!")
                return player1
            action = input("")

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
    validCommands = ["get","go","use", "fly","cut","climb", "surf", "hidden power", "flash","dig"]
    player = Player("Pallet Town", [],[],["fly","dig","surf","cut","strength","hidden power","flash"],[Pokemon(23,23)])
    move= ""
    inventory=[]
    emoticons = [crayons.red("Θ"),f"(╯°□°)╯︵{crayons.red('◓')}",f"{crayons.yellow('ϞϞ')}({crayons.red('๑')}⚈ ․ ⚈{crayons.red('๑')})∩","><(((o.^.o)","ଘ @(￣▵—▵￣)v(￣▵▵￣)@ ଓ",">(8☉)@@@oo<>","(>￣ー￣)"]
    def showStatus():
  #print the player's current status
        print('---------------------------')
        print('You are in',player.currentRoom)
  #print the current inventory
        print('Inventory :',inventory)
  #print an item if there is one
        print("You can go", ", ".join(rooms[player.currentRoom]['directions']))
        if len(rooms[player.currentRoom]['items']) != 0:
            for item in rooms[player.currentRoom]['items']:
                print(f'You see a {item}. {descriptions[item]}')
        print()
    clear()
    showInstructions()
    
    #plays music but server doesnt have speakers
    #pygame.mixer.init()
    #pygame.mixer.music.load("assets/music/battle.mp3")
    #pygame.mixer.music.play()
    #while pygame.mixer.music.get_busy() == True:
    #    continue


    while True and move!="q":

        ##conditional to create user file 
        ##if created start intro sequence to pick first pokemon
        ##if fail, load found file into game
        ##Battle Sequence and leveling pokemon
        ##Route Logic making a pokemon appear conditional before status message
        ##1Puzzle
        ##Skill directions
        ##Skill Event
        ##1Gym

        showStatus()
        player = battle(player,Trainer("jim",[Pokemon(44,44)]))
        move= ""
        while move == '':
            move=input(f"︵{crayons.red('◓')}>> ")
        move = move.lower().split(" ", 1)

        #if they type 'go' first
        if move[0] == 'go':
    #check that they are allowed wherever they want to go
            if move[1] in rooms[player.currentRoom]["directions"]:
      #set the current room to the new room
                player.currentRoom = rooms[player.currentRoom]["directions"][move[1]]
                clear()
    #there is no door (link) to the new room
            else:
                print('You can\'t go that way!')
        if move[0] == 'fly':
            if move[1].title() in rooms:
                player.currentRoom = move[1].title()
                clear()
            else:
                print('You can\'t fly there!')
        
        if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
            if move[1].title() in rooms[player.currentRoom]["items"]:
      #add the item to their inventory
                move[1] = move[1].title()
                inventory += [move[1]]
      #display a helpful message
                print(f"You put {move[1]} in your inventory")
    
      #delete the item from the room
                rooms[player.currentRoom]['items'].remove(move[1])
    #otherwise, if the item isn't there to get
            else:
      #tell them they can't get it  
                print('Can\'t get ' + move[1] + '!')

        if move[0] == 'help' :
            clear()
            showInstructions()


if __name__=="__main__":
    main()

