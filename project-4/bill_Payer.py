import random
import sys
print(sys.version)
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

numberpick = random.randint(0, len(names) - 1)
print(numberpick)

buyer = names[numberpick]
print(f"{buyer} is going to pay for everyone's meal.")




#other method:
"""
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

print(random.choice(names) + " is going to buy the meal today")
"""