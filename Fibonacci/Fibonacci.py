# Fibonacci Sequence is the sum of two numbers before it.

def Fibonacci(ls):

  if ls <= 0:
    return []
  elif ls == 1:
    return [0]

  fibSeq = [0,1]
  for i in range(ls-2):
    nextNum = fibSeq[-1] + fibSeq[-2]
    fibSeq.append(nextNum)


  return fibSeq


listSize = int(input("Enter a number: "))
print(Fibonacci(listSize))