# Fibonacci Sequence is the sum of two numbers before it.

def Fibonacci(ls):

  fibSeq = [0,1]

  if ls == 0:
    return(fibSeq[0])
  elif ls == 1:
    return(fibSeq[0], fibSeq[1])
  
  else:
    for i in range(ls-2):
      nextNum= fibSeq[i] + fibSeq[i-1]
      fibSeq.append(nextNum)
    return fibSeq


listSize = int(input("Enter a number: "))
print(Fibonacci(listSize))
    
    
