import time

print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
fail = ("you're a massive noob, you died.")


print("You're at a crossroad. Where do you want to go? Type 'left' or 'right'")
step1 = input()
if step1 in ("right", "Right", "RIGHT"):
  print("You continue walking...")
  print("you've come to a lake. There's an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. ")
  step2 = input()
  if step2 in ("wait", "Wait", "WAIT"):
    print("You wait in the harsh cold...")
    time.sleep(3)
    print("You arrive at the island. There's a house with 3 doors. Red, yellow and blue, which do you enter?")
    step3 = input()
    if step3 in ("red", "Red", "RED"):
      print("You're burnt alive! You lose!")
    elif step3 in ("yellow", "Yellow", "YELLOW"):
      print("You found the Treasure, You win!")
    else:
      print("You drown! You lose!")
  else:
    print(fail)
else:
  print(fail)

