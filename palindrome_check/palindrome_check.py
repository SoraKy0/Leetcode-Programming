# A Palindrome is when a word, phrase or sequence reads the same backwards as forwards.

def palindrome_check(word):

  listString = list(word)

  L = 0
  R = len(listString) - 1

  while L < R:
    listString[L], listString[R] = listString[R], listString[L]
    
    L += 1
    R -= 1
  
  reveredWord = "".join(listString)

  if reveredWord == word:
    return True
  else:
    return False


word = input("Enter a word you want to check: ")

result = palindrome_check(word)

print(result)