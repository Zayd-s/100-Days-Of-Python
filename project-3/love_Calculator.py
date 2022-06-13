# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

upp_name1 = name1.upper()
upp_name2 = name2.upper()

count1 = upp_name1.count("T") + upp_name1.count("R") + upp_name1.count("U") + upp_name1.count("E") + upp_name1.count("L") + upp_name1.count("O") + upp_name1.count("V") + upp_name1.count("E")

count2 = upp_name2.count("T") + upp_name2.count("R") + upp_name2.count("U") + upp_name2.count("E") + upp_name2.count("L") + upp_name2.count("O") + upp_name2.count("V") + upp_name2.count("E")

fin_Count = str(count1) + str(count2)


if int(fin_Count) < 10 or int(fin_Count) > 90:
  print(f"Your score is {fin_Count}, you go together like coke and mentos.")
elif int(fin_Count) >=40 and int(fin_Count) <= 50:
  print(f"Your score is {fin_Count}, you are alright together.")
else:
  print(f"Your score is {fin_Count}")



"""
#Easier method of counting:

from collections import Counter
my_str = "Mary had a little lamb"
counter = Counter(my_str)
print counter['a']
"""
