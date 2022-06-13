# 🚨 Don't change the code below 👇
age = int(input("What is your current age? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

agePick = int(input("What age do you want to calculate to? "))

days = (agePick*365) - (age*365)
weeks = (agePick*52) - (age*52)
months = (agePick*12) - (age*12)

print(f"You have, {days} days, {weeks} weeks, or {months} months until you're {agePick} years old.")

"""
Original code --- calculate time until you're 90 years old

age = input("What is your current age? ")

days = (90*365) - (int(age)*365)
weeks = (90*52) - (int(age)*52)
months = (90*12) - (int(age)*12)

print(f"You have, {days} days, {weeks} weeks, or {months} months until you're 90 years old.")

"""
