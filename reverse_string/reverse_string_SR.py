
def reverse_string(word):

  wlist = list(word)

  l = 0
  r = len(wlist) - 1

  while l < r:
    wlist[l], wlist[r] = wlist[r], wlist[l]
  
    l += 1
    r -= 1

  return "".join(wlist)



word = input("Enter a word: ")
print(reverse_string(word))
