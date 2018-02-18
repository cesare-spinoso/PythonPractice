# Prompts the user for a certain number of fibonacci numbers
# This imports the time class from a Python library. I will be using it to show the time it takes for the program to
# compile.

import time
# Start timer
start = time.time()
def fibonacciSequence(lengthOfSequence):
    baseCase = [1,1]
    recursive = []
    if lengthOfSequence <= 0:
        return None
    elif lengthOfSequence == 1:
        return [1]
    elif lengthOfSequence == 2:
        return [1, 1]
    else:
        recursive = [1,1]
        for j in range(2, lengthOfSequence):
            j = recursive[j-1] + recursive[j-2]
            recursive.append(j)
        return recursive

def isPrime(input):
    if input <= 0:
        return False
    array1 = range(1, input + 1)
    divisors = [i for i in array1 if input % i == 0]
    if len(divisors) == 2 and divisors[0] == 1 and divisors[1] == input:
        return True
    else:
        return False


def listPrimes(fibList):
    newList = []
    for i in fibList:
        if isPrime(i):
            newList.append(i)
    return newList


length = int(input("Enter your desired number Of fibonacci numbers you baka head\n"))
arrayFib = fibonacciSequence(length)
listPrimeAndFib = listPrimes(arrayFib)
print(fibonacciSequence(length))
print(listPrimeAndFib)
# End timer and print result
end = time.time()
print("Your prgrams run time period was: ", end - start)
