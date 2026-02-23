# Fibonacci Sequence is the sum of two numbers before it.

def Fibonacci(ls):

  fibSeq = [0,1]
  for i in range(ls-2):
    nextNum= fibSeq[i] + fibSeq[i-1]
    fibSeq.append(nextNum)


  return fibSeq


listSize = int(input("Enter a number: "))
print(Fibonacci(listSize))
    
    
