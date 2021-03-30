#!/usr/bin/env python3
heroes=  {
"wolverine":
    {"real name": "James Howlett",
    "powers": "regeneration",
    "archenemy": "Sabertooth",},
"harry potter":
    {"real name": "Harry Potter",
    "powers": "he's a wizard",
    "archenemy": "Voldemort",},
"agent fitz":
    {"real name": "Leopold Fitz",
    "powers": "intelligence",
    "archenemy": "Hydra",}
        }
char_name = char_stat = stop = ""
while stop != "Y":
    while char_name not in heroes:
        char_name = input("Which character do you want to know about? (Wolverine, Harry Potter, Agent Fitz)").lower()
    while char_stat not in heroes[char_name]:
        char_stat = input("What statistic do you want to know about? (real name, powers, archenemy)").lower()
    print(f"{char_name.title()}'s {char_stat} is: {heroes[char_name][char_stat]}")
    stop = input("wanna stop?(Y/N)").upper()
    if stop=="N":
        char_name = char_stat = ""
