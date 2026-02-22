# Factorial loop is where you multiply all numbers from 1 to n.

def factorialLoop(n):

  i = 1
  total = 1

  while i <= n:
    total = i * total

    i += 1
  
  return total


num = int(input("Enter a number: "))
print(factorialLoop(num))