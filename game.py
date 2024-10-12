import time
import sys
import os
import math


def init():
    os.system('cls' if os.name == 'nt' else 'clear')
    global saveplace
    saveplace = init
    global items
    items = ["Poppy","M.Candy","B.Pie","G.Pudding","Ginger.Man","Blacoffee","Nice.Cream","ApriLobster","Burger","MonkeyTail","V.Delight","AvacadoToast","Sw'ore","LevvySteak"]
    global xpgive
    xpgive = [2,3,5,6,22,150,25,18,22,30,35,340,40,46,52,700,1700,70,80,95,150,180,220,300,800] # 0-4 = Catacombs norm, 6-10 = Frostin norm,
    global xp # 12-14 = Calico norm, 17-21 = Vertica norm, 5 = Tutoria, 11 = Impact, 15 = norm Boarstle, 16 = geno Boarstle, 22 = Royal Guards, 23 = 3 Dancing Dogs,
    xp=0 # 24 = Levvy.
    lvcalc()
    global geno
    geno = False
    global equipped
    equipped = ["Stick", "Band-aid"] # 0 is weapon, 1 is def.
    global inventory
    inventory = ["Poppy"] # Inventory
    if "Stick" in equipped:
        global attackmult # Weapons use this
        attackmult = 3
    if "Band-aid" in equipped:
        global dfmult # Defensive items use this
        dfmult = 1
    dfcalc()
    atkcalc()
    hpcalc()
    global hp
    hp = maxhp # If it drops to 0, you lose
    FTO()

def hpcalc():
    global maxhp
    maxhp = 16+(4*love) # Max Health math

def dfcalc():
    global df 
    df = math.floor((love - 1) / 4)+dfmult+9 # Defence math

def atkcalc():
    global atk
    atk = (-2+(2*love))+attackmult+7 # Attack math

def lvcalc():
    global love
    global xp
    global lovecalc # LOVE calculations
    global xp
    lovecalc = [0, 10, 30, 70, 120, 200, 300, 500, 800, 1200, 1700, 2500, 3500, 5000, 7000, 10000, 15000, 25000, 50000, 99999] # XP thresholds
    love = 1
    for i in range(len(lovecalc) - 1, 0, -1): # for loop that checks if the xp is above the threshold and if not, i decreases and if it is, sets LOVE to i+1.
        if xp / lovecalc[i] >= 1:
            love = i + 1
            break # Stops the for loop.


def start():
    time.sleep(3)
    print("* GREETINGS. ") # The Introduction.
    time.sleep(2)
    print("* I HOPE WE ARE CONNECTED. ")
    time.sleep(1.5)
    print("* ...  ")
    time.sleep(3.25)
    print("* EXCELLENT. ")
    time.sleep(1.5)

    os.system('cls' if os.name == 'nt' else 'clear') # Clears the terminal.
    print("* NOW, WE MUST CREATE A VESSEL. ")
    time.sleep(1.5)
    print("* THIS VESSEL NEEDS A NAME. ")
    time.sleep(1.5)
    global name
    name=input("* WHAT SHALL IT BE? \n ") # Lets the player choose the name.
    time.sleep(1.5)
    if name == "AILBHE":  
        print("* EXCELLENT. ")
    elif name == "ASTER" or name == "BONBON": # dont spoil the game.
        print("* ! ")
        time.sleep(0.75)
        sys.exit()
    elif name == "BIOME" or name == "MARS" or name == "TUTORIA" or name == "IMPACT":  print("* HOW FAMILIAR. ") # Special text that hints at some characters
    else:  print(f"* \"{name}\". WONDERFUL.")
    time.sleep(3)

    print("* NOW, IT NEEDS A GENDER.") # The player assigns the gender.
    time.sleep(1.5)
    print("* WHAT SHALL IT BE? ")
    global gender
    gender=input(" ")

    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(2)
    print("* WHAT A WONDERFUL VESSEL. ")
    time.sleep(1.5)
    print("* THANK YOU FOR YOUR TIME.. ")
    time.sleep(1.5)
    print("* AND THIS WONDERFUL CREATION OF YOURS...")
    time.sleep(2.2)

    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(0.87)
    print("* Will now be overwritten.") # deltarune ref #2
    time.sleep(1)
    print("* Nobody chooses their own names.")
    time.sleep(1)
    print("* Did you choose your own original name?")
    time.sleep(1.5)
    os.system('cls' if os.name == 'nt' else 'clear')
    legend()

def legend():
    print("* Their name is Elo.")
    global truename
    truename = "Elo" # got this from a name generator
    time.sleep(1)
    print("* ...")
    time.sleep(4)

    os.system('cls' if os.name == 'nt' else 'clear')
    print("* Long ago, Humans and Monsters lived in harmony, coexisting for a millennium.") # The story that is always told.
    time.sleep(2)
    print("* Then, tension grew too high.")
    time.sleep(1.5)
    print("* Humans and Monsters went to war. \n* After years of fighting, Humans won.")
    time.sleep(1.5)
    print("* The remaining Monsters were sealed under a mountain with the power of nine Human Souls.")
    time.sleep(2)

    os.system('cls' if os.name == 'nt' else 'clear')
    print("* Elo is the last to fall.")
    time.sleep(1.5)
    print("* They have fallen here on a bed of red flowers.")
    time.sleep(1.5)
    print("* What choices will you have them make?") # There are many paths you can take.
    time.sleep(5)
    fallen1()

def fallen1():
    global subroutine
    os.system('cls' if os.name == 'nt' else 'clear')
    print("* You - Elo - hear footsteps, and..")
    time.sleep(2)
    print("???: 'Hm.. What was that? Oh! My child, I can see you have fallen down.'")
    time.sleep(1.5)
    global MATK # Tutoria's ATK.
    MATK = 3
    global MHP # Tutoria's HP.
    MHP = 28
    global MDF # Tutoria's DF.
    MDF = 2
    print("Tutoria: 'My name is Tutoria. You must be new. This is the Underground.'")
    time.sleep(2)
    print("Tutoria: 'Now, if you would like to follow me..")
    option1 = input("* Say 'Yes' or 'No' here. \n ") # this may or may not lead to the same place
    time.sleep(1.5)
    if option1 == 'Yes':
        print(f"Tutoria: 'And {name} is your name?'")
        time.sleep(1.5)
        print("Tutoria: 'Now, follow me to my home. Get adjusted to the puzzles.'")
        print("         'They are around every corner.'")
        time.sleep(3)
        subroutine = house
        house()
    else:
        print("Tutoria: Oh. Well, I will not force you, my child.'")
        time.sleep(3)
        fallen2()

def house():
    global saveplace
    os.system('cls' if os.name == 'nt' else 'clear')
    print("* It smells of pie. Chocolate, to be exact.") # Yvira no. (* Yvira yes.)
    time.sleep(1.5)
    print("* Would you like to save?")
    option2 = input("(Yes / No) \n")
    time.sleep(1.5)
    if option2.casefold() == "yes":
        print("* The smell of the pie fills them with a certain power.")
        saveplace = house
        time.sleep(1.5)
        print("* Current game saved.")
    else: print("* HP not restored.")
    time.sleep(2)
    print("* They feel tired, yet Elo is curious what lies outside.")
    time.sleep(1)
    print("* Shall they go outside, into the kitchen, or to bed?")
    option1 = input(" ")
    time.sleep(3)
    if option1 == 'outside': fallen2()
    elif option1 == 'kitchen': kitchen()
    else: bed()

def fallen2(): # Speedrunners, hate me!
    global subroutine
    time.sleep(1.5)
    print("* The first thing they see here is a tree.")
    time.sleep(1)
    print("* Would you like to save?")
    option = input("")
    time.sleep(1.5)
    if option.casefold() == "yes":
        print("* The falling leaves are a spectacle for them in the spring.")
        subroutine = fallen2
        time.sleep(1.5)
        print("* Current game saved.")
    else: print("* Game not saved.")
    time.sleep(2)


def kitchen():
    print("")

def bed():
    print("")

def FTO():
    time.sleep(1.5)
    print("* Attack, Act, Item or Mercy. \n Choose one.")
    FTOp = input("")
    if FTOp == "Attack":
        time.sleep(1)
        Attack()
    elif FTOp == "Act":
        time.sleep(1)
        Act()
    elif FTOp == "Item":
        time.sleep(1)
        Item()
    elif FTOp == "Mercy":
        time.sleep(1)
        Mercy()
    else:
        FTO()


def Attack():
    print("* I will not show the math.")

def Act():
    print("* For mercy, or for idiocy.")

def Item():
    global hp
    global maxhp
    nothing = []
    if inventory != nothing:
        print(f"* You have: {inventory} in your bag.")
    else:
        print(f"There is nothing in your bag..")
        FTO()
    print("* Any item you would like to use?")
    iFTO = input(" ")
    item_effects = { # Dictionary that contains all item effects
        0: 10,
        1: 10,
        2: maxhp - hp,
        3: 10,
        4: 10,
        5: 10,
        6: 10,
        7: 10,
        8: 10,
        9: 10,
        10: 10,
        11: 10,
        12: 10
    }
    for i in items:
        if i in inventory and i == iFTO.casefold():
            hp += item_effects.get(i, 10) # Default to adding 10 if not found
        else:
            FATK()
    


def Mercy():
    print("* Showing your benevolence.")

def FATK():
    print("* It is now their turn to fight you.")
    hp = hp - (MATK - df/5) # Undertale's Math..?
    time.sleep(1.5)
    print("They dealt ", str(MATK - df/5), " damage.")
    time.sleep(1.5)
    print(f"* Your HP is now at {hp}.")
    if hp > 0:
        FTO()
    else:
        death()

def death():
    global subroutine
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(0.75)
    print("* ...")
    time.sleep(2.25)
    print("* You lost.")
    time.sleep(1.5)
    print("* Will you try again?")
    option = input("")
    if option.casefold() == "yes" or option.casefold() == "y":
        subroutine()
    else:
        time.sleep(1.5)
        sys.exit()

init()