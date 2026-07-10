import os
import random

class Player:
    def __init__(self, name):
        self.name  = name
        self.maxHealth = 100
        self.health = self.maxHealth
        self.attack = 10
        self.defense = 1

class Spider (object):
    name = "Spider"
    maxHealth = 20
    health = maxHealth
    attack = 10
    defense = 1

class Wolf (object):
    name = "Wolf"
    maxHealth = 70
    health = maxHealth
    attack = 15
    defense = 2

class Beast (object):
    name = "Beast"
    maxHealth = 150
    health = maxHealth
    attack = 20
    defense = 1

Map = {
    'Beginning' : {'s' : 'Dining Hall'},
    'Dining Hall' : {'n' : 'Beginning', 's' : 'Hall of Metis', 'e' : 'Iron Vault', 'w' : 'Mythical Tree', 'Item' : 'Iron Armor'},
    'Mythical Tree' : {'s' : 'Stone Vault', 'e' : 'Dining Hall', 'w' : 'Thief Shrine', 'Item' : 'Golden Mango'},
    'Thief Shrine' : {'e' : 'Mythical Tree', 'Item' : 'Dagger'},
    'Stone Vault' : {'n' : 'Mythical Tree', 'Key' : 'Key of Instinct'},
    'Hall of Metis' : {'n' : 'Dining Hall', 's' : 'Gold Vault', 'e' : 'Barbarian Statue', 'Item' : 'Steak', 'Require' : 'Key of Instinct'},
    'Barbarian Statue' : {'n' : 'Iron Vault', 's' : 'Fountain of Destiny', 'w' : 'Hall of Metis', 'Item' : 'Strength Elixr'},
    'Iron Vault' : {'n' : 'Barbarian Shrine', 's' : 'Barbarian Statue', 'w' : 'Dining Hall', 'Key' : 'Key of Valor', 'Require' : 'Key of Instinct'},
    'Barbarian Shrine' : {'s' : 'Iron Vault', 'Item' : 'Black Steel Sword', 'Require' : 'Key of Honor'},
    'Gold Vault' : {'n' : 'Hall of Metis', 'e' : 'Fountain of Destiny', 'w' : 'Samurai Shrine', 'Key' : 'Key of Honor', 'Require' : 'Key of Valor'},
    'Samurai Shrine' : {'e' : 'Gold Vault', 'Item' : 'Black Steel Armor'},
    'Fountain of Destiny' : {'n' : 'Barbarian Statue', 's' : 'Void', 'e' : 'Hall of Greed', 'w' : 'Gold Vault', 'Item' : 'Ambrosia', 'Require' : 'Key of Honor'},
    'Hall of Greed' : {'n' : 'Hall of Avarice', 'w' : 'Fountain of Destiny', 'Item' : 'Steak'},
    'Hall of Avarice' : {'n' : 'Graveyard', 's' : 'Hall of Greed', 'Item' : 'Ambrosia'},
    'Graveyard' : {'n' : 'Diamond Vault', 's' : 'Hall of Avarice', 'Item' : 'Steak'},
    'Diamond Vault' : {'s' : 'Graveyard', 'Key' : 'Key of Sealing'},
    'Void' : {'n' : 'Fountain of Destiny', 'Require' : 'Key of Sealing'}
}

Tools = {
    'Iron Armor' : {'defense' : 3},
    'Black Steel Armor' : {'defense' : 5},
    'Dagger' : {'attack' : 15},
    'Black Steel Sword' : {'attack' : 25}
}

Items = {
    'Golden Mango' : {'health' : 200},
    'Strength Elixr' : {'attack' : 3},
    'Ambrosia' : {'health' : 20},
    'Steak' : {'health' : 10},
}

def opening():
    print("You wake up in a dark, stone room that's covered in moss. Light barely reaches your eyes and you feel exhausted, cold, and hungry.")
    print("You don't know how you ended up here, but the only thing to do now is to move forward.")
    print("You turn your head and notice an empty hall to the South.\n\n")
    print("TIPS:\n")
    print("Type 'search' to look around the room and see what you can find.")
    print("Type 'get' and the name of an item to get an item that you have found.")
    print("Type 'use' and the name of an item to use an item from your inventory.")
    print("Type 'locate' to find the different paths ahead.")
    print("Type 'move' and a letter representing a cardinal direction ('n' 'e' 's' 'w') to enter a room in that direction.\n")
    print("While in battle, type 'attack' to attack the enemy. Enemies that you have slain have a chance of dropping some items.")
    print("While in battle, type 'use' and the name of an item to use an item from your inventory.")
    print("While in battle, type 'run' to run away.\n")


    return input("What is your name? ")


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

cls()


plr = Player(opening())

armor = "Nothing"
weapon = "Fist"
inventory = []
keys = []
currentRoom = 'Beginning'
msg = ""

Death = False

def EnemyGenerate(Spider, Wolf, Beast):
    randInt = random.randint(0, 15)
    enemy = ""

    if randInt == 15:
        enemy = Beast
    elif randInt <= 14 and randInt >= 10:
        enemy = Wolf
    else:
        enemy = Spider

    return enemy

def Battle(bmsg, Enemy):
    global Death
    while True:
        if plr.health <= 0:
            Death = True
            return

        if Enemy.health <= 0:
            randGen = random.randint(0, 5)

            if randGen == 5:
                inventory.append(random.choice(list(Items)))

            return

        cls()

        enemyAction = random.randint(0,1)

        print(f"You are equipped with {armor} and are wielding a {weapon}.\n")
        print(f"Attack: {plr.attack}\nDefense: {plr.defense}")
        print(f"Your current Health is: {plr.health}/{plr.maxHealth}")
        print(f"You have the following Items: {inventory}\n{'-' * 35}")
        print(f"\n[{Enemy.name}'s Health: {Enemy.health}/{Enemy.maxHealth}]\n")
        print(f"{bmsg}\n\n")

        bInput = input("How will you Respond? ")
        bMove = bInput.split(' ')
        actionList = ['Attack', 'Use', 'Run']
        bAction = bMove[0].title()


        while bAction not in actionList:

            cls()

            print(f"You are equipped with {armor} and are wielding a {weapon}.\n")
            print(f"Attack: {plr.attack}\nDefense: {plr.defense}")
            print(f"Your current Health is: {plr.health}/{plr.maxHealth}")
            print(f"You have the following Items: {inventory}\n{'-' * 35}")
            print(f"\n[{Enemy.name}'s Health: {Enemy.health}/{Enemy.maxHealth}]\n")
            print(f"{bmsg}\n\n")

            bInput = input("How will you Respond? ")
            bMove = bInput.split(' ')
            bAction = bMove[0].title()

        if len(bAction) > 1:
            bItem = bMove[1:]
            bItem = ' '.join(bItem).title()

        if bAction == 'Attack':
            Enemy.health -= (plr.attack / Enemy.defense)
            Enemy.health = round(Enemy.health)
            bmsg = f"You fiercely attack with your {weapon}, "

        elif bAction == 'Use':
            if bItem in Items:
                food = Items[bItem]
                stat = ""
                amount = 0

                for key in food:
                    stat = key

                    amount = food[stat]

                setattr(plr, stat, getattr(plr, stat) + amount)
                inventory.remove(bItem)
                bmsg = f"You consume the {bItem}, "

        elif bAction == 'Run':
            return

        if enemyAction == 0:
            plr.health -= (Enemy.attack / plr.defense)
            plr.health = round(plr.health)
            bmsg += f"The {Enemy.name} viciously attacks you. "
        else:
            bmsg += f"The {Enemy.name} attacked, but missed. "

def Game():
    global armor
    global weapon
    global inventory
    global keys
    global currentRoom
    global msg

    while True:
        cls()

        if plr.health > plr.maxHealth:
            plr.maxHealth = plr.health
        elif plr.health <= 0:
            return

        print(f"{plr.name}, you are in the {currentRoom}.\n")
        print(f"You are equipped with {armor} and are wielding a {weapon}.\n")
        print(f"Attack: {plr.attack}\nDefense: {plr.defense}")
        print(f"Your current Health is: {plr.health}/{plr.maxHealth}")
        print(f"\nYou have the following Keys: {keys}")
        print(f"You have the following Items: {inventory}\n{'-' * 35}")
        print(f"{msg}\n\n")

        uInput = input("What do you want to do? ")
        nMove = uInput.split(' ')
        action = nMove[0].title()

        if len(nMove) > 1:
            item = nMove[1:]
            direction = nMove[1].lower()
            item = ' '.join(item).title()

        if action == 'Move':
            try:
                nextRoom = Map[currentRoom][direction]

                if Map[nextRoom] != "Void":
                    bttlGen = random.randint(0, 5)

                    if bttlGen == 0:
                        Enemy = EnemyGenerate(Spider, Wolf, Beast)
                        bmsg = f"A wild {Enemy.name} jumps towards you!"

                        Battle(bmsg, Enemy)

                if not "Require" in Map[nextRoom].keys():
                    currentRoom = nextRoom
                    msg = f"you traveled to the {nextRoom}."
                else:
                    lock = Map[nextRoom]["Require"]

                    if len(keys) == 0:
                        msg = f"You do not have any keys."
                    else:
                        for key in keys:
                            if key == lock:
                                currentRoom = nextRoom

                                if currentRoom != "Void":
                                    msg = f"you unlocked the door and traveled to the {nextRoom}."
                                else:
                                    return
                            elif key != lock:
                                msg = f"This room requires {lock}."
            except:
                msg = f"You cannot go there."

        elif action == 'Get':
            if "Item" in Map[currentRoom].keys():
                currItem = Map[currentRoom]["Item"]
                inventory.append(currItem)
                msg = f"You picked up the {currItem}."
                Map[currentRoom].pop("Item")

            elif "Key" in Map[currentRoom].keys():
                currItem = Map[currentRoom]["Key"]
                keys.append(currItem)
                msg = f"You picked up the {currItem}."
                Map[currentRoom].pop("Key")
            else:
                msg = f"Cannot find {item}."


        elif action == 'Locate':
            directions = ""

            for i in Map[currentRoom]:
                if i != "Item" and i != "Require" and i != "Key" :
                    directions += f"{i.upper()} "

            msg = f"Your may try to move [ {directions}]"

        elif action == 'Search':
            if "Item" in Map[currentRoom].keys():
                new_item = Map[currentRoom]["Item"]

                msg = f"You see (an) {new_item}"
            elif "Key" in Map[currentRoom].keys():
                new_key = Map[currentRoom]["Key"]

                msg = f"You found {new_key}."

        elif action == 'Use':
            try:
                if item not in inventory:
                    msg = f"This item does not exist."
                else:
                    if item in Tools:
                        tool = Tools[item]
                        stat = ""
                        amount = 0
                        itemType = ""

                        for key in tool:
                            stat = key

                        amount = tool[stat]

                        if stat == "defense":
                            armor = item
                        else:
                            weapon = item

                        setattr(plr, stat, amount)
                        inventory.remove(item)
                        msg = f"You equip your {item}. You can feel your power rising..."

                    else:
                        eat = Items[item]
                        stat = ""
                        amount = 0

                        for key in eat:
                            stat = key

                        amount = eat[stat]

                        setattr(plr, stat, getattr(plr, stat) + amount)
                        inventory.remove(item)
                        msg = f"You consume the {item}. It was delicious. Your soul grows stronger..."
            except:
                msg = f"Invalid Command."

        elif action == 'Help':
            msg = """Type 'search' to look around the room and see what you can find.
    Type 'get' and the name of an item to get an item that you have found.
    Type 'use' and the name of an item to use an item from your inventory.
    Type 'locate' to find the different paths ahead.
    Type 'move' plus a letter representing cardinal direction ('N' 'E' 'S' 'W') to enter a room in that direction.\n
    While in battle, type 'attack' to attack the enemy. Enemies that you have slain have a chance of dropping some items.
    While in battle, type 'use' and the name of an item to use an item from your inventory.
    While in battle, type 'run' to run away.
    """

        else:
            msg = "You cannot do this action."

Game()

cls()

if Death == False:
    print("As you step into the Void, darkness surrounds you. You feel your conscious clearing...\n\n\n\nGAME END.")
else:
    print(f"Standing in the {currentRoom}, you take your last breath...\nyou have met your END.")
