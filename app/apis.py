import json, urllib.request
import random

def get_random_profile_pic():
    randomint = random.randint(1, 1025)
    with urllib.request.urlopen(f"https://pokeapi.co/api/v2/pokemon/{randomint}/") as response:
        data = response.read()
    result = json.loads(data.decode('utf-8'))

    imgurl = result["sprites"]["other"]["official-artwork"]["front_default"]
    return imgurl