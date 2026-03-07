# Remove duplicate elements from an array

def remove_duplicate():
  array = [1,2,4,5,5,6,7,8,8,5,3,3,4,5,5,5,5,6,6,7,8,9,9,7,6,5,3,3,9,99,99,999,9999,99,999,9999,4,4,1,2,3,4,4,9,9,8]
  clean_array = []
 
  for num in array:
    if num not in clean_array:
      clean_array.append(num)

  return clean_array

print(remove_duplicate())

