# print("Welcome to the roller coaster!")
# height = int(input("Enter your height in cm: "))

# bill = 0

# if (height > 120):
#     print("You can ride the roller coaster!")
#     age = int(input("Enter your age in years: "))
#     wantPhotos = input("Do you want photos? y/n ").lower()
#     if (age <= 12):
#         bill += 5
#         if (wantPhotos == "y"):
#             bill += 3
#         print(f"Your total bill is ${bill}")
#     elif (12 < age < 18):
#         bill += 7
#         if (wantPhotos == "y"):
#             bill += 3
#         print(f"Your total bill is ${bill}")
#     else:
#         bill += 12
#         if (wantPhotos == "y"):
#             bill += 3
#         print(f"Your total bill is ${bill}")
# else:
#     print("You can't ride the roller coaster!")

################################################################

print("""
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"'"-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
""")

# Day 3 Project: Treasure island

print("Welcome to the Treasure Island!")
print("Your mission is to find the treasure.")

direction = input("You're at a cross road. Where do you want to go? Type 'l' for 'left' or 'r' for 'right': ").lower()

if (direction == "r"):
    print("You fell into a hole. Game over!")
elif (direction == "l"):
    decision1 = input("""You've come to a lake. There is an island in the middle of the lake. 
    Type 'w' to 'wait' for a boat or type 's' to 'swim' across: """).lower()
    if (decision1 == "w"):
        decision2 = input("""You arrived at the island unharmed. 
        There is a house with 3 doors. One red, one yellow and one blue. 
        Which colour do you chose? Type 'r' for 'red', 'y' for 'yellow' or 'b' for 'blue': """).lower()
        if (decision2 == "r"):
            print("It's a room full of fire. Game over!")
        elif (decision2 == "y"):
            print("You entered a room full of beasts. Game over!")
        elif (decision2 == "b"):
            print("You found the treasure! You won!")
    elif (decision1 == "s"):
        print("You got attacked by an angry trout. Game over!")



