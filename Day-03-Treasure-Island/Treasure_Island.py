print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

directions = input('You are at a crossroad. Would you like to take: "left" or "right"?\n').strip().lower()

if directions == "left":
    choice = input("You are at the edge of a lake. Do you want to swim or wait for a boat?\n").strip().lower()
    if choice == "wait":
        door = input('You arrived at the Island unharmed. Choose a door to enter: "red", "blue", "yellow"?\n').lower()
        if door == "red":
            print("Burned by Fire. Game Over")
        elif door == "blue":
            print("Eaten by beast. Game Over")
        elif door == "yellow":
            print("Found the treasure. You win.\n")
        else:
            print("That door doesn't exist. Game Over.\n")
    else:
        print("You have been attacked by a trout. Game Over.\n")
else:
    print("Fell into a hole. Game Over.\n")
