setA={2, 3, 5, 7, 11}
def primeNumber (number):
    for i in range(2, int(number ** (1/2))):
        if number % i == 0:
            return False
    return True
setPrimesNumbers = {x for x in setA if primeNumber(x)}
print(setPrimesNumbers == setA)