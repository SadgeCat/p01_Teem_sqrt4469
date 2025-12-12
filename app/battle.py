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
    if(button is pressed):
        


def apply_move(state, move_key):

    if state["winner"] is not None:
        return state

    attacker_key = state["turn"]
    defender_key = "p1" if attacker_key == "p2" else "p2"

    attacker = state[attacker_key]
    defender = state[defender_key]

    move = MOVES[move_key]
    power = move["power"]

    # Damage formula:
    damage = attacker["atk"] - (math.log10(defender["def"])/10 + 0.003*defender["def"])

    if damage < 1:
        damage = 1

    defender["current_hp"] -= damage
    if defender["current_hp"] < 0:
        defender["current_hp"] = 0

    message = f"{attacker['name']} used {move['name']} and dealt {damage} damage."
    state["log"].append(message)

    # Check if defender is defeated
    if defender["current_hp"] == 0:
        state["winner"] = attacker_key
        state["log"].append(f"{defender['name']} is defeated!")
    else:
        # Switch turns if no one has won yet
        state["turn"] = defender_key

    return state
