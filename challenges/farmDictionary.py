#!/usr/bin/env python3
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
def neAgriculture(farms):
    animals = []
    for farm in farms:
        if farm['name']=="NE Farm":
            animals += farm['agriculture']
    return animal

def inputAgriculture(farms):
    animals = []
    inputName = input("What farm? (NE Farm, W Farm, or SE Farm)")
    for farm in farms:
        if farm['name']==inputName:
            animals += farm['agriculture']
    return animals

def inputAnimalAgriculture(farms):
    possibleAnimals = ['sheep','cats','llamas','chickens','pigs','cows']
    animals = []
    inputName = input("What farm? (NE Farm, W Farm, or SE Farm)")
    for farm in farms:
        if farm['name']==inputName:
            for animal in farm['agriculture']:
                if animal in possibleAnimals:
                    animals += [animal]
    return animals
print(inputAnimalAgriculture(farms))

