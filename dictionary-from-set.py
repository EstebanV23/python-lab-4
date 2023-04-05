setA = {'Juan', 'Pedro', 'Cristian', 'Carlos', 'Rodrigo', 'Luis'}
       
setB = {1, 3, 5, 50, 32, 4}

def dictionaryFromSet (keys, values):
  dictionary = {x: y for x, y in zip(keys, values)}
  return dictionary

print(dictionaryFromSet(setA, setB))