import random, math
from apis import get_superhero, get_anime_character, get_superhero2

# All charatcers will share the same 3 moves for now
MOVES = {
    "strike": {
        "name": "Strike",
        "power": 20,
        "description": "A basic, reliable attack."
    },
    "power_blast": {
        "name": "Power Blast",
        "power": 30,
        "description": "Stronger hit."
    },
    "quick_hit": {
        "name": "Quick Hit",
        "power": 15,
        "description": "Weaker hit."
    }
}


# ------------- FIGHTER CREATION -------------

def make_random_fighter():
    source = random.choice(["superhero", "anime"])

    if source == "superhero":
        base = get_superhero2(0)
    else:
        base = get_anime_character(0)

    if base == None:
        return None

    fighter = {
        "name": base["name"],
        "image": base["image"],
        "hp": int(base["hp"]),
        "current_hp": int(base["hp"]),
        "atk": int(base["atk"]),
        "def": int(base["def"]),
        "speed": int(base["speed"]),
        "source": source
    }
    return fighter


def create_game_state():

    p1 = make_random_fighter()
    p2 = make_random_fighter()

    if p1["speed"] >= p2["speed"]:
        first = "p1"
    else:
        first = "p2"

    state = {
        "p1": p1,
        "p2": p2,
        "turn": first,
        "log": [f"{p1['name']} vs {p2['name']}! {first.upper()} goes first."],
        "winner": None
    }
    return state

#add button to switch pokemon mid-game
def switch_Character():
    return

def attack(attacker, defender, move_name):
    move = attacker["moves"][move_name]
    defender["current_hp"] = defender["current_hp"] - ((move["damage"] ** (math.log10(10-move["pp"])) / 2.5) * 20)
    return
