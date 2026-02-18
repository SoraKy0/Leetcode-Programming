def reverseString (string):

  L_string= list(string)

  l = 0
  r = len(string) - 1

  while l < r:
    L_string[l] , L_string[r] = L_string[r], L_string[l]
    l += 1
    r -= 1

  return "".join(L_string)

word = input("Enter your String: ")
result = reverseString(word)
print(result)