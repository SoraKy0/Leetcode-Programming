# FizzBuzz: It should print numbers from 1 to 100
# Where if the number is divisible bt 3 it should print Fizz
# and the number is divisible by 5, Buzz should print
# Finally if the number is divisible both by 3 and 5 FizzBuzz needs to be printed.

def fizzBuzz():

  for i in range (1, 101):
    if i % 3 == 0  and i % 5 == 0:
      print("FizzBuzz")
    elif i % 3 == 0:
      print("Fizz")
    elif i % 5 == 0:
      print("Buzz")
    else:
      print(i)

fizzBuzz()
