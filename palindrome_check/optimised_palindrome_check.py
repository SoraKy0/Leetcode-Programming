# A Palindrome is when a word, phrase or sequence reads the same backwards as forwards.
# This is more efficient than reversing the entire string.
# It returns False immediately when two characters don't match,
# rather than completing the full loop before comparing.

def palindrome_check(word):

  L = 0
  R = len(word) - 1

  while L < R:
    if word[L] != word[R]: # If letter at L and R pointer differ, they cannot be a palindrome.
      return False
    L += 1
    R -= 1

  return True  


word = input("Enter a word you want to check: ")

print(palindrome_check(word))