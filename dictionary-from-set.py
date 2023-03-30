setA = {2, 4, 6, 32, 10, 3}
       
setB = {1, 3, 5, 50, 32, 4}

def dictionaryFromSet (keys, values):
  for y in values:
    dictionary = dict.fromkeys(keys, y)
  return dictionary

print(dictionaryFromSet(setA, setB))