# Finds the max and min number in a list.

def max_min():

  exampleList = [42, 7, 91, 13, 58, 24, 76, 3, 65, 89, 31, 50, 17, 99, 8, 60, 27, 74, 12, 45]

  maxNum = exampleList[0]
  minNum = exampleList[0]



  for num in exampleList[1:]:
    if num > maxNum:
      maxNum = num

    elif num < minNum:
      minNum = num

  return maxNum, minNum

Max_Num, Min_Num = max_min()
print("Largest Number is: ", Max_Num)
print("Smallest Number is: ", Min_Num)
