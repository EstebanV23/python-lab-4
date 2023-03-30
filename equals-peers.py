setA ={2, 4, 6, 32, 10}
setB =  {1, 3, 5, 6, 32, 4}
finalSet = {x for x in setA if x % 2 == 0 and x in setB}
print(finalSet)