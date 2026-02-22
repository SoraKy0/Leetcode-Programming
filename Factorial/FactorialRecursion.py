# Factorial Recursion: calculates n! = n × factorial(n - 1) by calling itself

def factorialRecursion(n):
  if n < 1:
    return 1
  else:
    return(n * factorialRecursion(n-1))


num = int(input("Enter a number: "))

print(factorialRecursion(num))