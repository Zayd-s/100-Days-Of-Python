import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

options = [rock, paper, scissors]

playerPick = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
player = 0
bot = 0

if playerPick > 2 or playerPick < 0:
  print("No contest \n")
else:
  player = options[int(playerPick)]
  print(f"You choose: {player}")
  botPick = random.randint(0, len(options)-1 )
  bot = options[botPick]
  print(f"Bot chooses: {bot}")


if player == rock and bot == scissors:
  print("You win!")
elif player == paper and bot == rock:
  print("You win!")
elif player == scissors and bot == paper:
  print("You win!")
elif bot == rock and player == scissors:
  print("You lose!")
elif bot == paper and player == rock:
  print("You lose!")
elif bot == scissors and player == paper:
  print("You lose!")
elif player == bot and player and bot != (0, 2):
#elif player and bot != (0, 2): //also works
  print("Draw!")


"""
This can replace the botPick function in code above ^

bot = random.choice(options)
print(bot)
"""
