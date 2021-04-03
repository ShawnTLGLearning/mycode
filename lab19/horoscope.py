#!/usr/bin/env python3
"""SC Research || Author: ShawnCharles@protonmail.com"""
import requests
from os import system
import crayons


def clearScreen():
    """Clears the terminal"""
    print("\033[H\033[J")
    print("#########################")
    print("####",crayons.red("Horoscope Quest"),"####")
    print("#########################")

def getDay():
    """Prompts to get user Birthday"""
    day = 0
    while not(day>=1 and day<=31):
        try:
            inputDay = input("Input birthday(e.g. 1-31): \n")
            day = int(inputDay)
        except:
            clearScreen()
            print(f"{inputDay} is not a valid day")
    return day

def getSign(day):
    """Prompts to get user BirthMonth"""
    months={
           "december" :{"changeDay":22,"signs":["sagittarius","capricorn"]},
           "january" :{"changeDay":20,"signs":["capricorn","aquarius"]},
           "february" :{"changeDay":19,"signs":["aquarius","pisces"]},
           "march" :{"changeDay":21,"signs":["pisces","aries"]},
           "april" :{"changeDay":20,"signs":["aries","taurus"]},
           "may" :{"changeDay":21,"signs":["taurus","gemini"]},
           "june" :{"changeDay":21,"signs":["gemini","cancer"]},
           "july" :{"changeDay":23,"signs":["cancer","leo"]},
           "august" :{"changeDay":23,"signs":["leo","virgo"]},
           "september" :{"changeDay":23,"signs":["virgo","libra"]},
           "october" :{"changeDay":23,"signs":["libra","scorpio"]},
           "november" :{"changeDay":22,"signs":["scorpio","sagittarius"]}
           }
    inputMonth=""
    while inputMonth not in months:
        inputMonth = input("Input your month of birth (e.g. March, July etc): \n").lower()
        if inputMonth not in months:
            print(f"{inputMonth} not a valid month! Try May")
    monthInfo = months[inputMonth]
    return monthInfo["signs"][0] if day < monthInfo["changeDay"] else monthInfo["signs"][1] 

def getHoroscope(sign):
    """fetches daily horoscope of input sign"""
    url="http://horoscope-api.herokuapp.com/horoscope/today/" +sign
    response = requests.get(url).json()["horoscope"]
    betterAnswer ="Shawn".join(response.split("Ganesha"))
    return betterAnswer

def playerBuilder(name="randomPlayer",sign="libra",horoscope="Destined For Greatness",hp=50,attack=15,defense=15,magic=15,perks=["elif eliminator","YOLO"]):
    return {
            "name":name.title(),
            "sign":sign,
            "horoscope":horoscope,
            'hp':hp,
            'attack':attack,
            'defense':defense,
            'magic':magic,
            'perks':perks
            }

def willCheck(player):
    """updates attack & defense based on input"""
    print(f"Puny Adventurer {player['name']} Do you think you're mighty enough to last the battle  with only\n{player    ['attack']} attack?"
    )
    while True:
        response = input("Y/N?\n").capitalize()
        if response == "Y": 
            player['attack']+=5
            player['defense']-=5
            player["perks"]+=['Will Of Fire']
            clearScreen()
            print(f"{player['name']} Obtained skill {crayons.red('Will Of Fire')}!")
            break
        if response == "N":
             player['attack']-=5
             player['defense']+=5
             player["perks"]+=['Cautius Mind']
             clearScreen()
             print(f"{player['name']} obtained skill {crayons.blue('Cautius Mind')}!")
             break
    return player

def enduranceCheck(player):
    """updates attack & defense based on input"""
    print(f"Puny Adventurer {crayons.blue(player['name'])}, as a {player['sign'].title()} the universe must know your oppinion ?"
    )
    while True:
        response = input("(M)arathon or (S)print?\n").upper()
        if (response == "M" or  response == "MARATHON"):
            player['defense']+=5
            player['magic']+=10
            player['hp']+=25
            player["perks"]+=['Slow&Steady']
            clearScreen()
            print(f"{player['name']} obtained skill '{crayons.blue(player['perks'][-1:][0])}'!")
            break
        if (response == "S" or response=="SPRINT"):
             player['attack']+=10
             player["perks"]+=['Quick as Flash']
             clearScreen()
             print(f"{player['name']} obtained skill '{crayons.red(player['perks'][-1:][0])}'!")
             break
    return player

def heartCheck(player):
    """updates attack & defense based on input"""
    print(f"Puny Adventurer {player['name']}, as a {player['sign'].title()} the universe must know your oppinion ?"
    )
    while True:
        response = input("(E)arly Bird or (N)ight Owl?\n").upper()
        if (response == "N" or  response == "NIGHT OWL"):
            player['defense']+=5
            player['magic']+=25
            player['hp']+=25
            player["perks"]+=['StrongFinish']
            clearScreen()
            print(f"{player['name']} obtained skill '{crayons.red(player['perks'][-1:][0])}'!")
            break
        if (response == "E" or response=="EARLY BIRD"):
             player['attack']+=10
             player["perks"]+=['FirstAttack']
             clearScreen()
             print(f"{player['name']} obtained skill '{crayons.red(player['perks'][-1:][0])}'!")
             break
    return player

def chooseClass(player):
    player = enduranceCheck(player)
    player = willCheck(player)
    player = heartCheck(player)
    player = nextRound(player)
    return player

def levelUp(player):
    player["attack"]+=5
    player["defense"]+=5
    player["magic"]+=5
    player["hp"]+=25
    return player

def nextRound(ai):
    ai["attack"]+=25
    ai["defense"]+=25
    ai["magic"]+=25
    ai["hp"]+=125
    return ai

def battle(player):
    actions = ["A","B","M","H"]
    roundCount=1
    randomOpponent = playerBuilder("Darth Vader")
    randomOpponent = nextRound(randomOpponent)
    print(f"Battle with {randomOpponent['name']} has begun")
    while player["hp"]>0:
        print(f"Score: {player['points']}")
        print()
        print('{0:<}              {1:>}'.format(player['name'],randomOpponent['name']))
        print('{0:<}              {1:>}'.format(f"hp: {player['hp']}",randomOpponent['hp']))
        print('{0:<}            {1:>}'.format(f"attack: {player['attack']}",randomOpponent['attack']))
        print('{0:<}           {1:>}'.format(f"defense: {player['defense']}",randomOpponent['defense']))
        print('{0:<}             {1:>}'.format(f"magic: {player['magic']}",randomOpponent['magic']))
        action = ''
        while len(action)<1 or action not in actions:
            action = input("(A)ttack, (M)agic Attack, (H)eal, (B)lock?\n").upper()
            if action not in actions:
                print("enter valid action!")
        if action =="A":
            randomOpponent["hp"]-=player["attack"]
            player['points']+=player['attack']
            print(f"You dealt {player['attack']} points of damage to {randomOpponent['name']}")
        if action =="M":
            randomOpponent["hp"]-=player["magic"]
            player['points']+=player['magic']
            print(f"You dealt {player['magic']} points of magic damage to {randomOpponent['name']}")
        if action =="B":
            print(f"You unlocked the super secret Chad Mode")
            player["hp"]=9999999
            player["name"]="CHAD"
            player["attack"]=9999999
            player["defense"]=9999999
            player["magic"]=9999999
            player["points"]=9999999
            print(f"You Force Choke Vader and save the universe!!")
            break
        if action =="H":
            player["hp"]+=player["magic"]
            print(f"You healed {player['magic']} hp points")
        if randomOpponent["hp"]>0:
            player["hp"]-=randomOpponent["attack"]
            print(f"{randomOpponent['name']} used the force and dealt {randomOpponent['attack']} points of damage to {player['name']}")
        else:
            print("you defeated an enemy")
            print("but he came back stronger!")
            randomOpponent = nextRound(randomOpponent)
        input(f"Round {roundCount}. Press Enter")
        roundCount+=1
        clearScreen()
    print(f"You lasted {roundCount} rounds")
    print(player['horoscope'])

def main():
    """ Run-time code"""
    clearScreen()
    inputDay = getDay()
    clearScreen()
    inputSign = getSign(inputDay)
    clearScreen()
    name = input("What's your name?\n")
    clearScreen()
    player = playerBuilder(name,inputSign,getHoroscope(inputSign))
    player["points"]=0
    player = chooseClass(player)
    battle(player)
    print(f"Good Job {player['name']} You got {player['points']} points!")

if __name__ == "__main__":
    main()
