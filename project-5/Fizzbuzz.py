#fizzbuzz needs to be first in loop, otherwise:
#number 15 for example, can't be modulo'd (%)

#so if you turn 15 into fizz first, you can't modulo fizz, because
#fizz is no longer a number

for i in range(1, 101):
  if i % 5 == 0 and i % 3 == 0:
    print("fizzbuzz")
  elif i % 5 == 0:
    print ("buzz")
  elif i % 3 == 0:
    print ("fizz")
  else:
    print(i)
