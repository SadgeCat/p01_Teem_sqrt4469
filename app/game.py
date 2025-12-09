# Yuhang Pan (PM), Matthew Ciu, Michelle Chen, Thomas Mackey
# Hero Wars by Teem_sqrt4469
# SoftDev
# P01: ArRESTed Development
# Dec 2025
import random
from apis import get_pokemon, get_superhero
from battle import make_random_fighter

url = "https://pokeapi.co/api/v2/pokemon/"
"""
class player:
    def __init__(self, list):
        self.list = list # list of pokemon on their team
"""
def random_team():
    x = 0
    list = []
    while x <= 5:
        hero = make_random_fighter()
        list.append(hero)
        x+=1
    print(list)
    return list

# gamer = player()

random_team()
