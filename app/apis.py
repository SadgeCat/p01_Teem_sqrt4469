# Yuhang Pan (PM), Matthew Ciu, Michelle Chen, Thomas Mackey
# Hero Wars by Teem_sqrt4469
# SoftDev
# P01: ArRESTed Development
# Dec 2025

import json, urllib.request, time
import random

def get_random_profile_pic():
    randomint = random.randint(1, 1025)
    with urllib.request.urlopen(f"https://pokeapi.co/api/v2/pokemon/{randomint}/") as response:
        data = response.read()
    result = json.loads(data.decode('utf-8'))

    imgurl = result["sprites"]["other"]["official-artwork"]["front_default"]
    return imgurl

def get_pokemon(id):
    if id == 0:
        id = random.randint(1,1025)
    with urllib.request.urlopen(f"https://pokeapi.co/api/v2/pokemon/{id}/") as response:
        data = response.read()
    result = json.loads(data.decode('utf-8'))
    return result

def check_stat(val):
    if val is None or (isinstance(val, str) and not val.isdigit()):
        return random.randint(1, 100)
    return int(val)

def check_key(url, key):
    with urllib.request.urlopen(f"{url}/{key}/") as response:
        data = response.read()
    result = json.loads(data.decode('utf-8'))
    return result["response"] == "error"

def get_superhero(id):
    if id == 0:
        id = random.randint(1,613)
    with open("keys/key_SuperheroAPI.txt") as file:
        superhero_key = file.read()
    with urllib.request.urlopen(f"https://www.superheroapi.com/api.php/{superhero_key}/{id}") as response:
        data = response.read()
    result = json.loads(data.decode('utf-8'))
    stats = result["powerstats"]
    hp = check_stat(stats["durability"])
    atk = check_stat(stats["power"])
    speed = check_stat(stats["speed"])
    defense = check_stat(stats["strength"])

    return {
        "name": result["name"],
        "image": result["image"]["url"],
        "hp": hp,
        "atk": atk,
        "speed": speed,
        "def": defense
    }

def check_rate(url):
    while True:
        try:
            with urllib.request.urlopen(url) as response:
                return response.read()
        except urllib.error.HTTPError as e:
            if e.code == 429:
                print("reached quota! waiting 3 seconds...")
                time.sleep(3)
            else:
                raise

def get_anime_character(id):
    if id == 0:
        id = random.randint(1,612)
    count = id % 25
    page = id // 25

    data = check_rate(f"https://api.jikan.moe/v4/characters?order_by=favorites&sort=desc&limit={count}&page={page}")
    result = json.loads(data.decode('utf-8'))["data"]

    chosen = random.choice(result)
    mal_id = chosen["mal_id"]

    data2 = check_rate(f"https://api.jikan.moe/v4/characters/{mal_id}/full")
    character = json.loads(data2.decode('utf-8'))["data"]

    return {
        "name": character["name"],
        "image": character["images"]["jpg"]["image_url"],
        "hp": round(0.5 * character["favorites"] ** 0.5), # hp = 0.5 * #favorites ** 0.5
        "atk": 10 * len(character["anime"]), # atk = #anime * 10
        "speed": 10 * len(character["manga"]), # speed = #manga * 10
        "def": 10 * len(character["voices"]), # defense = #voice * 10
    }
