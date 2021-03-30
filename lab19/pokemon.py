#!/usr/bin/env python3
import requests
response = requests.get('https://pokeapi.co/api/v2/pokemon/1')
print(response.json())
