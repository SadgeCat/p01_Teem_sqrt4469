# Yuhang Pan (PM), Matthew Ciu, Michelle Chen, Thomas Mackey
# Hero Wars by Teem_sqrt4469
# SoftDev
# P01: ArRESTed Development
# Dec 2025
import random
from apis import get_pokemon
from apis import get_superhero

url = "https://pokeapi.co/api/v2/pokemon/"

class pokemon:
    id: int
    skin: str
    health: int
    pic: str

class player:
    id: int
    list: list # list of pokemon on their team
    poke_out: int

    def action(poke_out, move):
        get_pokemon()

def intialize():
    p1 = player()
    p1.id = 1


    p2 = player()

def random_poke(player):
    x = 0
    while x <= 5:
        # create pokemon obj WHERE
        id = random.randomint(1, 1025)
        getpokemon(id)
        #create adding to list here
        player.list[x] =


    get_pokemon()
# return pokemon

print(get_pokemon(150))
