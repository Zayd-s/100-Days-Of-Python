# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆


#Write your code below this line 👇

bmi = weight / (height**2)

if bmi < 18.5:
  print(f"Your bmi is {bmi}. You're underweight.")
elif bmi > 18.5 and bmi < 25:
  print(f"Your bmi is {bmi}. You have a normal, healthy weight.")
elif bmi > 25 and bmi < 30:
  print(f"Your bmi is {bmi}. You are slightly overweight.")
elif bmi > 30 and bmi < 35:
  print(f"Your bmi is {bmi}. You are obese.")
elif bmi < 35:
  print(f"Your bmi is {bmi}. You are clinically obese.")
